import datetime, decimal, json, logging, os, sys, base64

from queue import Queue
from sqlalchemy import func, Integer, cast, Date
from models.user_model import RegistroInput, RegistroOutput, SaleConfirmByClient, Product
from sqlserver.basedipalza import Session
from sqlserver.db_name import t_NUMERADOS, t_EOS_REGISTROS, t_MSOGENERAL, t_ENCABEZADOCUMENTO, \
    t_MSOSTTABLAS, t_PARAMETROS, t_FOLIOS, t_TOTALDOCUMENTO, t_MSOSTVENTASILA, t_DETALLEDOCUMENTO, t_ARTICULO, \
    t_MSOVENDEDOR, t_CTADOCTO, t_MSOCLIENTES, t_INVDETALLEPARTES, t_ARTICULOSNUMERADOS, t_EOS_LOGVENTAS, t_EOS_FALTANTES
from utils.messages import Message, PROGRESS, BILL, ERROR, FINISH, INIT, MISSING
from utils.util import format_rut_with_points, Registro_Rectificado
from utils import configuration

logger = logging.getLogger(__name__)


class DBProcessor:

    def __init__(self, session: Session, queue: Queue):

        self.queue = queue
        register = session.query(t_MSOGENERAL).first()
        self.iva = register[1]

        self.electronic_bill_enabled = configuration.electronic_bill_enabled
        self.numero_lineas_factura = configuration.numero_lineas_factura
        self.local = configuration.local
        self.tipo_documento = configuration.tipo_documento
        self.paridad = configuration.paridad

        self.electronic_bill = "E" if self.electronic_bill_enabled else " "
        self.ilas_dict_vacio = self.__obtener_diccionario_tipo_ilas(session)

    def get_product_by_code(self, code, session):
        t = t_ARTICULO
        products = session.query(t).filter(t.c.Articulo == code).all()
        pr = products[0]

        p = Product(Articulo=pr.Articulo, Descripcion=pr.Descripcion, VentaNeto=pr.VentaNeto, PorcIla=pr.PorcIla,
                    PorcCarne=pr.PorcCarne, Unidad=pr.Unidad, Stock=0, Pieces=0, Numbered=False, CodigoIla=pr.CodigoIla)

        t = t_ARTICULOSNUMERADOS
        exists = session.query(t).filter(t.c.articulo == code).scalar() is not None
        if exists:
            # es numerado
            p.Numbered = True
            result = session.execute(f"EXEC dbo.calcularStockNumerado @id={code}")
            try:
                v = result.first()
                p.Stock = v[1]
                p.Pieces = v[2]
            except:
                p.Stock = 0
                p.Pieces = 0
        else:

            result = session.execute(f"EXEC dbo.calcularStock @id={code}")
            try:
                v = result.first()
                p.Stock = v[0]
            except:
                p.Stock = 0

        return p

    def agregar_registro_numerado(self, input: RegistroInput, session: Session):
        """
        Este método siempre va a agregar un registro de un producto numerado.
        En el caso de solicitar más unidades que las existentes se va a colocar valores 0 tanto en el número, correlativo y peso.
        @param input:  El registro con los valores de entrada a procesar
        @param session:  La sesión con la que se está procesando la transacción.
        @return: Registro de la BD con todo procesado.
        """

        # Se verifica si existe el producto en la BD.
        t = t_ARTICULO
        products = session.query(t).filter(t.c.Articulo == input.articulo).all()
        if not products or len(products) == 0:
            return None

        # Se extrae solamente el primer producto por si ha trae más elementos.
        product = products[0]
        numbered = session.query(t_NUMERADOS).filter(t_NUMERADOS.c.articulo == input.articulo).all()

        # Inicialización de valores
        peso = 0
        numeros = ""
        correlativos = ""
        pesos = ""
        nroRegister = int(input.cantidad)
        articulos = []
        for n in range(nroRegister):
            # Estos valores se utilizarán cuando el número de registros es mayor que el stock existente del producto
            rpeso = 0
            rnumero = 0
            rcorrelativo = 0
            if n < len(numbered):
                reg = numbered[n]
                rpeso = reg.peso
                rnumero = reg.numero
                rcorrelativo = reg.correlativo
                stmt = t_NUMERADOS.delete().where(t_NUMERADOS.c.correlativo == reg.correlativo)
                session.execute(stmt)

            peso = peso + rpeso
            numeros = f"{numeros};{rnumero}"
            correlativos = f"{correlativos};{rcorrelativo}"
            pesos = f"{pesos};{rpeso}"

        # se saca el primer ";"
        numeros = numeros[1:]
        correlativos = correlativos[1:]
        pesos = pesos[1:]

        precio = product.VentaNeto
        neto = peso * precio
        dscto = neto * decimal.Decimal(input.descuento / 100);
        neto = neto - dscto

        vneto = neto if neto > 0 else 0
        iva = vneto * self.iva / 100
        carne = vneto * decimal.Decimal(product.PorcCarne / 100)
        ila = vneto * decimal.Decimal(product.PorcIla / 100)
        codigo_ila = product.CodigoIla

        code = input.codigo.strip().replace(".", "").replace("-", "")
        code = code.rjust(3, ' ')

        fecha = input.fecha

        ins = t_EOS_REGISTROS.insert().values(rut=input.rut, codigo=code,
                                              vendedor=input.vendedor, fila=input.fila, fecha=fecha,
                                              articulo=input.articulo, cantidad=peso, neto=vneto, descuento=dscto,
                                              ila=ila,
                                              carne=carne, iva=iva, precio=precio, numeros=numeros,
                                              correlativos=correlativos, pesos=pesos,
                                              esnumerado=input.esnumerado, codigoila=codigo_ila, sobrestock=input.sobrestock, condicionventa = input.condicionventa)
        r = session.execute(ins)

        return RegistroOutput(
            indice=r.inserted_primary_key[0],
            rut=input.rut,
            codigo=code,
            vendedor=input.vendedor,
            fila=input.fila,
            fecha=fecha,
            articulo=input.articulo,
            cantidad=peso,
            neto=vneto,
            descuento=dscto,
            ila=ila,
            carne=carne,
            iva=iva,
            precio=precio,
            numeros=numeros,
            correlativos=correlativos,
            pesos=pesos,
            esnumerado=input.esnumerado,
            codigo_ila=codigo_ila,
            condicionventa=input.condicionventa
        )

    def agregar_registro_no_numerado(self, input: RegistroInput, session: Session):

        t = t_ARTICULO

        products = session.query(t).filter(t.c.Articulo == input.articulo).all()
        if not products or len(products) == 0:
            return None

        product = products[0]

        cantidad = input.cantidad
        precio = product.VentaNeto
        neto = decimal.Decimal(cantidad) * product.VentaNeto
        dscto = neto * decimal.Decimal(input.descuento / 100);
        neto = neto - dscto

        vneto = neto if neto > 0 else 0
        iva = vneto * self.iva / 100
        carne = vneto * decimal.Decimal(product.PorcCarne / 100)
        ila = vneto * decimal.Decimal(product.PorcIla / 100)
        codigo_ila = product.CodigoIla

        code = input.codigo.strip().replace(".", "").replace("-", "")
        code = code.rjust(3, ' ')
        fecha = input.fecha.strftime('%Y-%m-%d %H:%M:%S')
        ins = t_EOS_REGISTROS.insert().values(rut=input.rut, codigo=code,
                                              vendedor=input.vendedor, fila=input.fila, fecha=fecha,
                                              articulo=input.articulo, cantidad=cantidad, neto=float(vneto), descuento=float(dscto),
                                              ila=ila,
                                              carne=carne, iva=float(iva), precio=float(precio), numeros="", correlativos="",
                                              pesos="",
                                              esnumerado=input.esnumerado, codigoila=codigo_ila, sobrestock=input.sobrestock, condicionventa=input.condicionventa)

        r = session.execute(ins)
        return RegistroOutput(
            indice=r.inserted_primary_key[0],
            rut=input.rut,
            codigo=code,
            vendedor=input.vendedor,
            fila=input.fila,
            fecha=fecha,
            articulo=input.articulo,
            cantidad=cantidad,
            neto=vneto,
            descuento=dscto,
            ila=ila,
            carne=carne,
            iva=iva,
            precio=precio,
            numeros="",
            correlativos="",
            pesos="",
            esnumerado=input.esnumerado,
            codigo_ila=codigo_ila,
            condicionventa=input.condicionventa

        )

    def __num_dias_condicion_venta(self, condicion_venta: int, session: Session):
        """
        Retorna el número de dias de una condicion de venta.
        @return:
        """
        t = t_MSOSTTABLAS
        cond_venta = f"{condicion_venta}".rjust(3, '0')
        generator = session.query(t).filter(t.c.tabla == "009", t.c.codigo == cond_venta).values(t.c.valor)
        num_dias = next(generator)
        if num_dias:
            return float(num_dias[0]);
        return 0

    def __siguiente_id(self, session: Session):
        """
        Se obtiene el id más grande de la tabla encabezado documento, el que corresponde al número a asignarle a la siguiente venta.
        @return: el id que debe establecerse a la venta
        """
        t = t_ENCABEZADOCUMENTO
        max_id = session.query(func.max(cast(t.c.Id, Integer))).scalar()
        max_id = int(max_id) + 1
        s_max_id = f"{max_id}".rjust(10, "0")
        return s_max_id

    def __siguiente_numero_factura(self, session: Session):
        tipo1 = self.electronic_bill
        t = t_FOLIOS
        numero_factura = session.query(func.max(t.c.Numero)).filter(t.c.Tipo == "06", t.c.TIPO1 == tipo1).scalar()
        sgte_numero_factura = int(numero_factura) + 1
        s_numero_factura = f"{sgte_numero_factura}".rjust(7, "0")
        return s_numero_factura

    def __obtener_conduccion(self, rut: str, session: Session):
        t = t_MSOCLIENTES
        generator = session.query(t).filter(t.c.Rut == rut).values(t.c.Ruta)
        register = next(generator, None)

        if not register:
            return None

        ruta = register[0]
        codigo = "9997"
        if ruta == "001":
            codigo = "9999"
        if ruta == "003":
            codigo = "9998"

        t = t_MSOSTTABLAS
        generator = session.query(t).filter(t.c.tabla == "015", t.c.codigo == codigo).values(t.c.codigo, t.c.descripcion.label('Descripcion'),
                                                                                             t.c.valor)
        register = next(generator, None)
        if not register:
            return None

        return register

    def __obtener_diccionario_tipo_ilas(self, session: Session):
        t = t_MSOSTTABLAS
        result = dict()
        try:
            ilas = session.query(t).filter(t.c.descripcion.like("%ILA %")).values(t.c.codigo, t.c.valor)
        except:
            logger.warning(f"No se ha encontrado valores ILA en la tabla t_MSOSTTABLAS")
            return result

        for ila in ilas:
            result[ila[0]] = {"codigo": ila[0], "porcentaje": ila[1], "suma": 0}
        return result

    def eliminar_registro(self, indice: int, session: Session):
        """
        Al borrar un registro de ventas temporal, se procede a realizar la inserción de los artículos numerados que utiliza
        @param indice: Indice en la BD del registro que se quiere eliminar
        @return:
        """
        try:
            register = session.query(t_EOS_REGISTROS).filter(t_EOS_REGISTROS.c.indice == indice).first()
            if register is None:
                return None

            if register.esnumerado:
                numeros = register.numeros.split(";")
                pesos = register.pesos.split(";")
                correlativos = register.correlativos.split(";")
                for n in range(len(numeros)):
                    insert_stmt = t_NUMERADOS.insert().values(
                        articulo=register.articulo,
                        #correlativo=int(correlativos[n]),
                        peso=float(pesos[n]),
                        numero=numeros[n],
                        narticulo=int(register.articulo))
                    session.execute(insert_stmt)
                    stmt = t_EOS_REGISTROS.delete().where(t_EOS_REGISTROS.c.indice == indice)
                    session.execute(stmt)
            #session.commit()
        except:
            print( sys.exc_info()[0])
            session.rollback()

        return register

    def comision_vendedor(self, confirmation: SaleConfirmByClient, session: Session):
        t = t_MSOVENDEDOR

        result = session.query(t).filter(t.c.codigo == confirmation.vendedor).values(t.c.comision)
        r = next(result)
        comision = r[0]

        return comision

    async def procesar_ventas(self, sale: str, session: Session):
        """
        Procesa todas las ventas que se encunentran en los registros para un vendedor.
        """
        try:

            self.grabar_log(Message(INIT, sale, "Ventas", f"Iniciando procesamiento de ventas para el vendedor {sale}"), session)
            t = t_EOS_REGISTROS
            stmt = session.query(t.c.rut.label('rut'), t.c.codigo.label('codigo'), t.c.fecha.cast(Date).label("fecha"), t.c.condicionventa.label('condicionventa')).filter(
                t.c.vendedor == sale).distinct()

            result = session.execute(stmt)
            registros = list(result)
            nro_total_registros = len(registros)

            nro_registro = 1
            for registro in registros:
                self.grabar_log(Message(PROGRESS, sale, "Procesando Ventas",
                                       f"Procesando venta de cliente {format_rut_with_points(registro.rut)}",
                                       nro_registro=nro_registro, nro_total_registros=nro_total_registros), session)


                args = registro.fecha.timetuple()[:6]
                fecha = datetime.datetime(*args)
                item = SaleConfirmByClient(rut=registro.rut, codigo=registro.codigo, vendedor=sale,
                                           condicion_venta=registro.condicionventa, fecha=fecha)
                self.process_venta(item, session)
                # Notificando
                nro_registro = nro_registro + 1
            session.query(t).filter(t.c.vendedor == sale).delete(synchronize_session=False)
            self.grabar_log(Message(FINISH, sale, "Ventas",
                              f"Finalizado el proceso de registro de ventas para el vendedor {sale}"), session)
            #session.commit()

        except Exception as ex:
            self.grabar_log(Message(ERROR, sale, "Error en Procesamiento de Ventas",
                                   f"Error en el proceso: {sys.exc_info()[0]}"), session)
            session.rollback()
            raise
            return False

        return True

    def process_venta(self, confirmation: SaleConfirmByClient, session: Session):

        # generar map de los códigos de ILA
        condicion_venta = confirmation.condicion_venta
        __num_dias_condicion_venta = self.__num_dias_condicion_venta(condicion_venta, session)
        fecha_operacion = confirmation.fecha
        fecha_vencimiento = fecha_operacion + datetime.timedelta(days=__num_dias_condicion_venta)
        factura_electronica = self.electronic_bill
        comision_vendedor = self.comision_vendedor(confirmation, session)

        r = t_EOS_REGISTROS
        p = t_ARTICULO

        # Se obtienen los registros asociados al vendedor, ruta y fecha indicada en el parámetro.
        # La cantidad de registros puede exceder la cantidad de elementos definidos para una factura.
        registros = session.query(r, p). \
            filter(p.c.Articulo == r.c.articulo). \
            filter(r.c.rut == confirmation.rut, r.c.codigo == confirmation.codigo,
                   r.c.vendedor == confirmation.vendedor).values(
            r.c.rut, r.c.codigo, r.c.vendedor, r.c.fila, r.c.fecha, r.c.articulo, r.c.cantidad, r.c.neto, r.c.descuento,
            r.c.codigoila, r.c.ila, r.c.carne, r.c.iva, r.c.precio, r.c.numeros, r.c.correlativos, r.c.pesos,
            r.c.esnumerado, r.c.totalila, p.c.Costo, p.c.Descripcion)

        facturas = dict()
        correlativo = 0
        # obtengo los registros de cada venta y aprovecho de realizar cálculos
        nro_lineas = 0
        for registro in registros:

            # Se reevalua la cantidad de productos
            register_rectified = self.get_register_rectified_with_real_stock(registro, session)
            if register_rectified is None:
                # quiere decir que el producto no tiene el stock, por tanto pasamos al siguiente.
                continue

            if nro_lineas % self.numero_lineas_factura == 0:
                nro_lineas = 1
                correlativo = correlativo + 1
                ilas_venta_dict = self.ilas_dict_vacio.copy()
                neto_venta = 0
                iva_venta = 0
                carne_venta = 0
                descuento_venta = 0
                facturas[correlativo] = {"id": "", "factura": "", "condicion_venta": condicion_venta,
                                         "fecha": fecha_operacion, "fecha_vencimiento": fecha_vencimiento, "afecto": "A",
                                         "rut": confirmation.rut, "codigo": confirmation.codigo, "local": "000",
                                         "tipo": "06", "tipo1": factura_electronica, "ilas": ilas_venta_dict,
                                         "total_neto": 0, "total_iva": 0, "total_carne": 0, "total_descuento": 0,
                                         "comision_vendedor": comision_vendedor, "vendedor": confirmation.vendedor, "registros": []}


            neto_venta = neto_venta + (0 if registro.neto is None else registro.neto)
            iva_venta = iva_venta + (0 if registro.iva is None else registro.iva)
            carne_venta = carne_venta + (0 if registro.carne is None else registro.carne)
            descuento_venta = descuento_venta + (0 if not registro.descuento else registro.descuento)

            if (not registro.ila is None) and registro.ila > 0:
                codigo_ila = registro.codigoila.strip()
                ilas_venta_dict[codigo_ila]["porcentaje"] = codigo_ila
                ilas_venta_dict[codigo_ila]["suma"] = ilas_venta_dict[codigo_ila]["suma"] + registro.ila

            facturas[correlativo]["registros"].append(registro)
            facturas[correlativo]["total_neto"] = neto_venta
            facturas[correlativo]["total_iva"] = iva_venta
            facturas[correlativo]["total_carne"] = carne_venta
            facturas[correlativo]["total_descuento"] = descuento_venta
            nro_lineas = nro_lineas + 1

        # Se agrega registro de conducción.
        conduccion = self.__obtener_conduccion(confirmation.rut, session)
        if conduccion is None:
            pass
        else:
            if correlativo in facturas.keys():
                factura = facturas[correlativo]
                neto_venta = factura["total_neto"]
                if nro_lineas >= self.numero_lineas_factura:
                    correlativo = correlativo + 1
                    facturas[correlativo] = {"id": "", "factura": "", "condicion_venta": condicion_venta,
                                             "fecha": fecha_operacion, "fecha_vencimiento": fecha_vencimiento, "afecto": "A",
                                             "rut": confirmation.rut, "codigo": confirmation.codigo, "local": "000",
                                             "tipo": "06", "tipo1": factura_electronica, "ilas": ilas_venta_dict,
                                             "total_neto": 0, "total_iva": 0, "total_carne": 0, "total_descuento": 0,
                                             "comision_vendedor": comision_vendedor, "vendedor": confirmation.vendedor, "registros": []}

                neto_venta = neto_venta + conduccion[2]
                facturas[correlativo]["registros"].append(conduccion)
                facturas[correlativo]["total_neto"] = neto_venta

        if len(facturas) == 0:
            return False

        for factura in facturas.values():
            # obtengo aquí el número para obtener el último número justo antes de grabar
            factura["id"] = self.__siguiente_id(session)
            factura["factura"] = self.__siguiente_numero_factura(session)
            # Grabo de inmediato el folio para no perderlo
            self.grabar_folios(factura, session)
            self.grabar_encabezado(factura, session)
            self.grabar_detalle_factura(factura, session)
            self.grabar_parametro(factura, session)
            self.grabar_total_documento(factura, session)
            self.grabar_cuenta_documento(factura, session)
            self.grabar_ila(factura, session)

            self.grabar_log(Message(BILL, confirmation.vendedor, "Facturas", f"Factura Nro: {factura['factura']}", nro_factura=factura['factura'], nro_id=factura['id']), session)

        return True

    def get_register_rectified_with_real_stock(self, registro_original, session):

        rectificated_register = Registro_Rectificado(registro_original._asdict())

        product = self.get_product_by_code(rectificated_register.articulo, session)
        if product.Numbered:
            # Obtengo todos los elementos que tienen un 0, ya que fue pedido pero no había stock
            # Con el fin de volver a revisar si ahora hay stock
            zero_numbers = list(filter(lambda x: x.strip() == "0", rectificated_register.numeros.split(";")))
            len_zero_numbers = len(zero_numbers)

            # Tiene el total de su pedido completo
            if len_zero_numbers == 0:
                return rectificated_register

            # Se filtran los números, correlativos y pesos que son mayores que 0 y se vuelven a convertir en string separado por ';'
            rectificated_register.numeros = ";".join(list(filter(lambda x: x.strip() != "0", rectificated_register.numeros.split(";"))))
            rectificated_register.correlativos = ";".join(list(filter(lambda x: x.strip() != "0", rectificated_register.correlativos.split(";"))))
            rectificated_register.pesos = ";".join(list(filter(lambda x: x.strip() != "0", rectificated_register.pesos.split(";"))))

            # Se ha pedido más productos de los que habían
            database_numbered = session.query(t_NUMERADOS).filter(t_NUMERADOS.c.articulo == rectificated_register.articulo).all()
            len_database_numbered = len(database_numbered)

            requirement_diff = len_zero_numbers - len_database_numbered;

            if (requirement_diff > 0):
                # Significa que hay unidades que no podrán ser entregadas.
                self.grabar_log(Message(MISSING, rectificated_register.vendedor, "Faltan unidades ",
                                       f"Faltan {requirement_diff:.2f} del producto {rectificated_register.articulo} {rectificated_register.Descripcion}",
                                       requirement_diff=float(requirement_diff), product_code=rectificated_register.articulo), session)

                # Aquí debo agregar registro de faltante de stock
                t_EOS_FALTANTES.insert().values(
                    rut=rectificated_register.rut, codigo=rectificated_register.codigo,
                    vendedor=rectificated_register.vendedor, fila=rectificated_register.fila, fecha=fecha,
                    articulo=rectificated_register.articulo, cantidad=float(requirement_diff), neto=float(0), descuento=float(0),
                    ila=0,
                    carne=0, iva=float(0), precio=float(product.VentaNeto), numeros="", correlativos="",
                    pesos="",
                    esnumerado=input.esnumerado, codigoila="", sobrestock=input.sobrestock, condicionventa=input.condicionventa
                )

            generated_numbers = ""
            generated_correlatives = ""
            generated_weights = ""
            weight = 0

            for n in range(len(zero_numbers)):
                if n < len(database_numbered):
                    reg = database_numbered[n]
                    rpeso = reg.peso
                    rnumero = reg.numero
                    rcorrelativo = reg.correlativo
                    stmt = t_NUMERADOS.delete().where(t_NUMERADOS.c.articulo == database_numbered[n].articulo)
                    session.execute(stmt)
                    weight = weight + rpeso
                    generated_numbers = f"{generated_numbers};{rnumero}"
                    generated_correlatives = f"{generated_correlatives};{rcorrelativo}"
                    generated_weights = f"{generated_weights};{rpeso}"

            # se saca el primer ";"
            generated_numbers = generated_numbers[1:]
            generated_correlatives = generated_correlatives[1:]
            generated_weights = generated_weights[1:]

            precio = float(product.VentaNeto)
            neto = float(weight) * float(precio)
            dscto = neto * float(rectificated_register.descuento) / 100.0;
            neto = neto - dscto

            vneto = neto if neto > 0 else 0
            iva = vneto * float(self.iva) / 100.0
            carne = vneto * float(product.PorcCarne) / 100.0
            ila = vneto * float(product.PorcIla) / 100.0
            codigo_ila = product.CodigoIla

            rectificated_register.cantidad = float(rectificated_register.cantidad) + float(weight)
            rectificated_register.neto = float(rectificated_register.neto) + vneto
            rectificated_register.descuento = float(rectificated_register.descuento) + dscto
            rectificated_register.ila = float(rectificated_register.ila) + ila
            rectificated_register.carne = float(rectificated_register.carne) + carne
            rectificated_register.iva = float(rectificated_register.iva) + iva
            rectificated_register.inumeros = f"{rectificated_register.numeros};{generated_numbers}"
            rectificated_register.correlativos = f"{rectificated_register.correlativos};{generated_correlatives}"
            rectificated_register.pesos = f"{rectificated_register.pesos};{generated_weights}"

        else:

            requirement_diff = float(rectificated_register.cantidad) - product.Stock
            if requirement_diff > 0:
                # Significa que hay unidades que no podrán ser entregadas.
                self.grabar_log(Message(MISSING, rectificated_register.vendedor,  "Faltan unidades ",
                                       f"Fatan {requirement_diff} del producto {rectificated_register.articulo} {rectificated_register.Descripcion}",
                                       requirement_diff=float(requirement_diff), product_code=rectificated_register.articulo), session)

                # Aquí debo agregar registro de faltante de stock
                t_EOS_FALTANTES.insert().values(
                    rut=rectificated_register.rut, codigo=rectificated_register.codigo,
                    vendedor=rectificated_register.vendedor, fila=rectificated_register.fila, fecha=fecha,
                    articulo=rectificated_register.articulo, cantidad=float(requirement_diff), neto=float(0), descuento=float(0),
                    ila=0,
                    carne=0, iva=float(0), precio=float(product.VentaNeto), numeros="", correlativos="",
                    pesos="",
                    esnumerado=input.esnumerado, codigoila="", sobrestock=input.sobrestock, condicionventa=input.condicionventa
                )


            rectificated_register.cantidad = min(product.Stock, rectificated_register.cantidad)
            rectificated_register.TotalLinea = float(rectificated_register.precio) * float(rectificated_register.cantidad)
            rectificated_register.iva = float(rectificated_register.TotalLinea) * float(self.iva) / 100
            rectificated_register.ila = float(rectificated_register.TotalLinea) * float(product.PorcIla) / 100.0
            rectificated_register.descuento = float(rectificated_register.TotalLinea) * float(rectificated_register.descuento) / 100.0

        texto_descripcion = rectificated_register.Descripcion

        if rectificated_register.numeros is not None and rectificated_register.numeros.strip() != ";":

            texto_descripcion = f"{product.Descripcion} [{rectificated_register.numeros}]"

            """
            Cantidad=rectificated_register.cantidad if "cantidad" in rectificated_register.keys() else 0,
            Variacion=-rectificated_register.descuento if "descuento" in rectificated_register.keys() else 0,
            Descripcion=texto_descripcion
            """
        return rectificated_register if rectificated_register.cantidad != 0 else None

    def grabar_encabezado(self, factura, session: Session):
        """
        Graba el encabezado de una venta completa
        @param factura: Datos calculados durante el inicio de la facturación.
        @return:
        """
        fecha_vencimiento = factura["fecha_vencimiento"]
        rut_cliente = factura["rut"]
        codigo_cliente = factura["codigo"]
        id = factura["id"]
        numero_factura = factura["factura"]
        es_factura_electronica = factura["tipo1"]
        fecha_operacion = factura["fecha"]
        es_afecto = factura["afecto"]

        ins = t_ENCABEZADOCUMENTO.insert().values(Fecha=fecha_operacion, Vence=fecha_vencimiento,
                                                  AfectoExento=es_afecto, Rut=rut_cliente,
                                                  Local=self.local, Id=id, Tipo=self.tipo_documento,
                                                  Numero=numero_factura,
                                                  Codigo=codigo_cliente, TIPO1=es_factura_electronica,
                                                  Publicado=0,
                                                  PublicadoNro=numero_factura)
        session.execute(ins)

        return True

    def grabar_detalle_factura(self, factura, session: Session):
        t = t_DETALLEDOCUMENTO
        linea = 1
        for registro in factura["registros"]:
            texto_descripcion = registro.Descripcion

            if texto_descripcion == "CONDUCCION":
                ins = t.insert().values(
                    PrecioVenta=registro.precio if "precio" in registro.keys() else 0,
                    TotalLinea=registro.neto if "neto" in registro.keys() else 0,
                    Paridad=self.paridad,
                    PrecioCosto=registro.precio if "precio" in registro.keys() else 0,
                    Cantidad=registro.cantidad if "cantidad" in registro.keys() else 0,
                    Id=factura["id"],
                    Linea=f"{linea:03}",
                    Tipoid=self.tipo_documento,
                    Local=self.local,
                    Articulo=registro.articulo if "articulo" in registro.keys() else "000",
                    Variacion=-registro.descuento if "descuento" in registro.keys() else 0,
                    Descripcion=texto_descripcion
                )
            else:
                if "numeros" in registro.keys() and registro.numeros != None and registro.numeros.strip() != "":
                    texto_descripcion = f"{texto_descripcion} [{registro.numeros}]"

                ins = t.insert().values(
                    PrecioVenta=registro.precio if "precio" in registro.keys() else 0,
                    TotalLinea=registro.neto if "neto" in registro.keys() else 0,
                    Paridad=self.paridad,
                    PrecioCosto=registro.precio if "precio" in registro.keys() else 0,
                    Cantidad=registro.cantidad if "cantidad" in registro.keys() else 0,
                    Id=factura["id"],
                    Linea=f"{linea:03}",
                    Tipoid=self.tipo_documento,
                    Local=self.local,
                    Articulo=registro.articulo if "articulo" in registro.keys() else "000",
                    Variacion=-registro.descuento if "descuento" in registro.keys() else 0,
                    Descripcion=texto_descripcion
                )

            session.execute(ins)
            linea = linea + 1
        return True

    def grabar_total_documento(self, factura, session: Session):
        """
        Almacena el total del documento que se está almacenando
        @param factura: Datos calculados durante el inicio de la facturación.
        @return: Verdadero si el registro fue grabado exitosamente.
        """
        t = t_TOTALDOCUMENTO
        total_ila = 0
        for ila in factura["ilas"]:
            total_ila = total_ila + factura["ilas"][ila]["suma"]
        total = factura["total_neto"] + factura["total_iva"] + total_ila
        ins = t.insert().values(TotalDetalle=factura["total_neto"],
                                TotalIva=factura["total_iva"],
                                TotalIla=total_ila,
                                TotalNeto=factura["total_neto"],
                                Total=total,
                                Id=factura['id'],
                                TipoId=factura["tipo"])
        session.execute(ins)

        return True

    def grabar_cuenta_documento(self, factura, session: Session):
        t = t_CTADOCTO
        total_ila = 0
        for ila in factura["ilas"]:
            total_ila = total_ila + factura["ilas"][ila]["suma"]

        total_bruto = factura["total_neto"] + factura["total_iva"] + total_ila

        ins = t.insert().values(
            Rut_cliente=factura["rut"],
            fecha_vencimiento=factura["fecha_vencimiento"],
            comision=factura["comision_vendedor"],
            fecha_ingreso=factura["fecha"],
            vendedor=factura["vendedor"],
            valor_bruto=total_bruto,
            valor_iva=factura["total_iva"],
            valor_neto=factura["total_neto"],
            Tipo=factura["tipo"],
            Numero=factura["factura"],
            codigo_cliente=factura["codigo"],
            local_venta=factura["local"],
            valor_ila=total_ila,
            TIPO1=self.electronic_bill
        )
        session.execute(ins)

        return True

    def grabar_parametro(self, factura, session: Session):
        t = t_PARAMETROS
        try:
            upd = t.update().values(FolioDocumento=factura["id"]).returning(t.c.FolioDocumento)
            session.execute(upd)
            session.commit()
        except:
            session.rollback()

    def grabar_folios(self, factura, session: Session):
        t = t_FOLIOS

        ins = t.insert().values(Numero=factura["factura"], Tipo=factura["tipo"], TIPO1=self.electronic_bill)
        session.execute(ins)
        return True

    def grabar_ila(self, factura, session: Session):
        """
        Debe almacenar un registro de ila por cada código diferente que haya en la venta
        @param registro:
        @return:
        """
        t = t_MSOSTVENTASILA
        for ila in factura["ilas"].values():
            # try:

            ins = t.insert().values(tipo=factura["tipo"], TIPO1=self.electronic_bill, codigo=ila["codigo"],
                                    valor=ila["suma"], numero=factura["factura"], ila=ila["porcentaje"])
            session.execute(ins)
            # except:
            #    continue

    def procesar_rebajar_ventas(self, session: Session):
        pass

    def grabar_log(self, message: Message, session: Session):
        self.queue.put(message)
        params = json.dumps(message.extra_params)
        t = t_EOS_LOGVENTAS
        ins = t.insert().values(fecha= datetime.date.today(), vendedor = message.code, tipo = message.type, titulo = message.title, mensaje = message.description, json_parameters = params)
        session.execute(ins)