import datetime
import decimal
import logging

from sqlalchemy import func, Integer, cast

from models.user_model import RegistroInput, RegistroOutput, SaleConfirmByClient
from sqlserver.db_name import t_NUMERADOS, t_EOS_REGISTROS, t_MSOGENERAL, t_ENCABEZADOCUMENTO, \
    t_MSOSTTABLAS, t_PARAMETROS, t_FOLIOS, t_TOTALDOCUMENTO, t_MSOSTVENTASILA, t_DETALLEDOCUMENTO, t_ARTICULO, \
    t_MSOVENDEDOR, t_CTADOCTO, t_MSOCLIENTES

logger = logging.getLogger(__name__)


class DBProcessor:

    def __init__(self, session):
        self.session = session
        register = self.session.query(t_MSOGENERAL).first()
        self.iva = register[1]
        self.electronic_bill_enabled = True
        self.numero_lineas_factura = 3
        self.local = "000"
        self.tipo_documento = "06"
        self.paridad = 1.0
        self.electronic_bill = "E" if self.electronic_bill_enabled else " "

    def agregar_registro_numerado(self, input: RegistroInput):
        """
        Este método siempre va a agregar un registro de un producto numerado
        @param input:  El registro con los valores de entrada a procesar
        @return: Registro de la BD con todo procesado.
        """
        # product = self.session.query(t_View_Stock).filter(t_View_Stock.c.articulo == input.articulo).first()
        t = t_ARTICULO
        products = self.session.query(t).filter(t.c.Articulo == input.articulo).all()
        if not products or len(products) == 0:
            return None
        product = products[0]
        numbered = self.session.query(t_NUMERADOS).filter(t_NUMERADOS.c.articulo == input.articulo).all()

        peso = 0
        # Estos valores son para poder revertir el proceso si es que se arrepiente
        numeros = ""
        correlativos = ""
        pesos = ""
        nroRegister = int(input.cantidad)
        articulos =[]
        for n in range(nroRegister):
            # valor por defecto para los elementos
            rpeso = 0
            rnumero = 0
            rcorrelativo = 0
            if n < len(numbered):
                # solo si n es menor la cantidad de numerados existentes
                reg = numbered[n]
                rpeso = reg.peso
                rnumero = reg.numero
                rcorrelativo = reg.correlativo
                stmt = t_NUMERADOS.delete().where(t_NUMERADOS.c.articulo == numbered[n].articulo)
                self.session.execute(stmt)
                self.session.commit()

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
                                              esnumerado=input.esnumerado, codigoila=codigo_ila, sobrestock=input.sobrestock)
        r = self.session.execute(ins)
        self.session.commit()


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
            codigo_ila=codigo_ila
        )
        return registrostmt

    def agregar_registro_no_numerado(self, input: RegistroInput):
        # product = self.session.query(t_View_Stock).filter(t_View_Stock.c.Articulo == input.articulo).first()
        t = t_ARTICULO
        products = self.session.query(t).filter(t.c.Articulo == input.articulo).all()
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
        fecha = input.fecha
        ins = t_EOS_REGISTROS.insert().values(rut=input.rut, codigo=code,
                                              vendedor=input.vendedor, fila=input.fila, fecha=fecha,
                                              articulo=input.articulo, cantidad=cantidad, neto=vneto, descuento=dscto,
                                              ila=ila,
                                              carne=carne, iva=iva, precio=precio, numeros="", correlativos="",
                                              pesos="",
                                              esnumerado=input.esnumerado, codigoila=codigo_ila, sobrestock=input.sobrestock)

        r = self.session.execute(ins)
        self.session.commit()

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
            codigo_ila=codigo_ila
        )

    def __num_dias_condicion_venta(self, condicion_venta: int):
        """
        Retorna el número de dias de una condicion de venta.
        @return:
        """
        t = t_MSOSTTABLAS
        cond_venta = f"{condicion_venta}".rjust(3, '0')
        generator = self.session.query(t).filter(t.c.tabla == "009", t.c.codigo == cond_venta).values(t.c.valor)
        num_dias = next(generator)
        if num_dias:
            return float(num_dias[0]);
        return 0

    def __siguiente_id(self):
        """
        Se obtiene el id más grande de la tabla encabezado documento, el que corresponde al número a asignarle a la siguiente venta.
        @return: el id que debe establecerse a la venta
        """
        t = t_ENCABEZADOCUMENTO
        max_id = self.session.query(func.max(cast(t.c.Id, Integer))).scalar()
        max_id = int(max_id) + 1
        s_max_id = f"{max_id}".rjust(10, "0")
        return s_max_id

    def __siguiente_numero_factura(self):
        tipo1 = self.electronic_bill
        t = t_FOLIOS
        numero_factura = self.session.query(func.max(t.c.Numero)).filter(t.c.Tipo == "06", t.c.TIPO1 == tipo1).scalar()
        sgte_numero_factura = int(numero_factura) + 1
        s_numero_factura = f"{sgte_numero_factura}".rjust(7, "0")
        return s_numero_factura

    def __obtener_conduccion(self, rut: str):
        t = t_MSOCLIENTES
        generator = self.session.query(t).filter(t.c.Rut == rut).values(t.c.Ruta)
        register = next(generator, None)

        if not register:
            return  None

        ruta = register[0]
        codigo = "9997"
        if ruta == "001":
            codigo = "9999"
        if ruta == "003":
            codigo = "9998"

        t = t_MSOSTTABLAS
        generator = self.session.query(t).filter(t.c.Tabla == "015", t.c.Codigo == codigo).values(t.c.Codigo, t.c.Descripcion, t.c.Valor)
        register = next(generator, None)
        if not register:
            return None
        return {"codigo": register[0].Codigo, "descripcion": register[0].Descripcion, "valor": register[0].valor}

    def __obtener_diccionario_tipo_ilas(self):
        t = t_MSOSTTABLAS
        result = dict()
        try:
            ilas = self.session.query(t).filter(t.c.descripcion.like("%ILA %")).values(t.c.codigo, t.c.valor)
        except:
            logger.warning(f"No se ha encontrado valores ILA en la tabla t_MSOSTTABLAS")
            return result

        for ila in ilas:
            result[ila[0]] = {"codigo": ila[0], "porcentaje": ila[1], "suma": 0}
        return result

    def eliminar_registro(self, indice: int):
        """
        Al borrar un registro de ventas temporal, se procede a realizar la inserción de los artículos numerados que utiliza
        @param indice: Indice en la BD del registro que se quiere eliminar
        @return:
        """
        register = self.session.query(t_EOS_REGISTROS).filter(t_EOS_REGISTROS.c.indice == indice).first()
        if register is None:
            return None

        if register.esnumerado:
            numeros = register.numeros.split(";")
            pesos = register.pesos.split(";")
            correlativos = register.correlativos.split(";")
            for n in range(len(numeros)):
                insert_stmt = t_NUMERADOS.insert().values(
                    articulo=register.articulo,
                    correlativo=int(correlativos[n]),
                    peso=float(pesos[n]),
                    numero=numeros[n],
                    narticulo=int(register.articulo))
                self.session.execute(insert_stmt)

        stmt = t_EOS_REGISTROS.delete().where(t_EOS_REGISTROS.c.indice == indice)
        self.session.execute(stmt)
        self.session.flush()
        self.session.commit()
        return register

    def comision_vendedor(self, confirmation: SaleConfirmByClient):
        t = t_MSOVENDEDOR

        try:
            result = self.session.query(t).filter(t.c.codigo == confirmation.vendedor).values(t.c.comision)
            r = next(result)
            comision = r[0]
        except:
            logger.warning(f"No se ha encontrado el valor de la comision del vendedor {confirmation.codigo}")
            return 0

        return comision

    def process_venta(self, confirmation: SaleConfirmByClient):
        # generar map de los códigos de ILA
        ilas_dict_vacio = self.__obtener_diccionario_tipo_ilas()
        condicion_venta = confirmation.condicion_venta
        __num_dias_condicion_venta = self.__num_dias_condicion_venta(condicion_venta)
        fecha_operacion = confirmation.fecha
        fecha_vencimiento = fecha_operacion + datetime.timedelta(days=__num_dias_condicion_venta)
        factura_electronica = self.electronic_bill
        comision_vendedor = self.comision_vendedor(confirmation)

        r = t_EOS_REGISTROS
        p = t_ARTICULO

        # Se obtienen los registros asociados al vendedor, ruta y fecha indicada en el parámetro.
        # La cantidad de registros puede exceder la cantidad de elementos definidos para una factura.
        registros = self.session.query(r, p). \
            filter(p.c.Articulo == r.c.articulo). \
            filter(r.c.rut == confirmation.rut, r.c.codigo == confirmation.codigo,
                   r.c.vendedor == confirmation.vendedor).values(
            r.c.rut, r.c.codigo, r.c.vendedor, r.c.fila, r.c.fecha, r.c.articulo, r.c.cantidad, r.c.neto, r.c.descuento,
            r.c.codigoila, r.c.ila, r.c.carne, r.c.iva, r.c.precio, r.c.numeros, r.c.correlativos, r.c.pesos,
            r.c.esnumerado, r.c.totalila, p.c.Costo, p.c.Descripcion)

        nro_lineas = 0
        facturas = dict()
        correlativo = 0
        # obtengo los registros de cada venta y aprovecho de realizar cálculos
        for registro in registros:
            if nro_lineas % self.numero_lineas_factura == 0:
                correlativo = correlativo + 1
                ilas_venta_dict = ilas_dict_vacio.copy()
                neto_venta = 0
                iva_venta = 0
                carne_venta = 0
                descuento_venta = 0
                facturas[correlativo] = { "id": "", "factura": "", "condicion_venta": condicion_venta,
                    "fecha": fecha_operacion, "fecha_vencimiento": fecha_vencimiento, "afecto": "A",
                    "rut": confirmation.rut, "codigo": confirmation.codigo, "local": "000",
                    "tipo": "06", "tipo1": factura_electronica, "ilas": ilas_venta_dict,
                    "total_neto": 0, "total_iva": 0, "total_carne": 0, "total_descuento": 0,
                    "comision_vendedor": comision_vendedor, "vendedor": confirmation.vendedor, "registros": [] }

            neto_venta = neto_venta + registro.neto
            iva_venta = iva_venta + registro.iva
            carne_venta = carne_venta + registro.carne
            descuento_venta = descuento_venta + registro.descuento
            if registro.ila > 0:
                ilas_venta_dict[registro.codigoila]["porcentaje"] = registro.ila
                ilas_venta_dict[registro.codigoila]["suma"] = ilas_venta_dict[registro.codigoila]["suma"] + registro.ila

            facturas[correlativo]["registros"].append(registro)
            facturas[correlativo]["total_neto"] = neto_venta
            facturas[correlativo]["total_iva"] = iva_venta
            facturas[correlativo]["total_carne"] = carne_venta
            facturas[correlativo]["total_descuento"] = descuento_venta
            nro_lineas = nro_lineas + 1

            # Se agrega registro de conducción.
            conduccion =  self.__obtener_conduccion()
            if conduccion is None:
                return

            factura = facturas[correlativo]
            nro_lineas = len(factura["registros"])
            if nro_lineas % self.numero_lineas_factura == 0:
                neto_venta = 0
                iva_venta = 0
                carne_venta = 0
                descuento_venta = 0
                facturas[correlativo] = { "id": "", "factura": "", "condicion_venta": condicion_venta,
                    "fecha": fecha_operacion, "fecha_vencimiento": fecha_vencimiento, "afecto": "A",
                    "rut": confirmation.rut, "codigo": confirmation.codigo, "local": "000",
                    "tipo": "06", "tipo1": factura_electronica, "ilas": ilas_venta_dict,
                    "total_neto": 0, "total_iva": 0, "total_carne": 0, "total_descuento": 0,
                    "comision_vendedor": comision_vendedor, "vendedor": confirmation.vendedor, "registros": [] }

            neto_venta = conduccion["valor"]
            facturas[correlativo]["registros"].append(conduccion)
            facturas[correlativo]["total_neto"] = neto_venta


        for factura in facturas.values():
            # obtengo aquí el número para obtener el último número justo antes de grabar
            factura["id"] = self.__siguiente_id()
            factura["factura"] = self.__siguiente_numero_factura()
            # Grabo de inmediato el folio para no perderlo
            self.grabar_folios(factura)
            self.grabar_encabezado(factura)
            self.grabar_detalle_factura(factura)
            self.grabar_parametro(factura)
            self.grabar_total_documento(factura)
            self.grabar_cuenta_documento(factura)
            self.grabar_folios(factura)
            self.grabar_ila(factura)

    def grabar_encabezado(self, factura):
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
                                                  PublicadoNro=numero_factura)
        # try:
        self.session.execute(ins)
        self.session.commit()
        # except:
        #    return False

        return True

    def grabar_detalle_factura(self, factura):
        t = t_DETALLEDOCUMENTO
        linea = 1
        for registro in factura["registros"]:
            texto_descripcion = registro.Descripcion
            if registro.numeros != None and registro.numeros.strip() != "":
                texto_descripcion = f"{texto_descripcion} [{registro.numeros}]"
            if type(registro) == t_EOS_REGISTROS:
                ins = t.insert().values(
                    PrecioVenta=registro.precio,
                    TotalLinea=registro.neto,
                    Paridad=self.paridad,
                    PrecioCosto=registro.precio,
                    Cantidad=registro.cantidad,
                    Id=factura["id"],
                    Linea=f"{linea:03}",
                    Tipoid=self.tipo_documento,
                    Local=self.local,
                    Articulo=registro.articulo,
                    Variacion=-registro.descuento,
                    Descripcion=texto_descripcion
                )
            else:
                ins = t.insert().values(
                    PrecioVenta=registro["valor"],
                    TotalLinea=registro["valor"],
                    Paridad=self.paridad,
                    PrecioCosto=registro["valor"],
                    Cantidad=1,
                    Id=factura["id"],
                    Linea=f"{linea:03}",
                    Tipoid=self.tipo_documento,
                    Local=self.local,
                    Articulo=registro["codigo"],
                    Variacion=0,
                    Descripcion=registro["descripcion"]
                )
            # try:
            self.session.execute(ins)
            linea = linea + 1
            # except:
            #    continue
        self.session.commit()
        return True

    def grabar_total_documento(self, factura):
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
        # try:
        self.session.execute(ins)
        self.session.commit()
        # except:
        #    return False

        return True

    def grabar_cuenta_documento(self, factura):
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
        # try:
        self.session.execute(ins)
        self.session.commit()
        # except:
        #    return False

        return True

    def grabar_parametro(self, factura):
        t = t_PARAMETROS
        upd = t.update().values(FolioDocumento=factura["id"]).returning(t.c.FolioDocumento)
        self.session.execute(upd)
        self.session.commit()

    def grabar_folios(self, factura):
        t = t_FOLIOS
        # try:
        ins = t.insert().values(Numero=factura["factura"], Tipo=factura["tipo"], TIPO1=self.electronic_bill)
        self.session.execute(ins)
        self.session.commit()
        # except:
        #    return False

        return True

    def grabar_ila(self, factura):
        """
        Debe almacenar un registro de ila por cada código diferente que haya en la venta
        @param registro:
        @return:
        """
        t = t_MSOSTVENTASILA
        for ila in factura["ilas"]:
            # try:
            ins = t.insert().values(tipo=self.electronic_bill, TIPO1=factura.tipo, codigo=ila["codigo"],
                                    valor=ila["suma"], numero=factura["factura"], ila=ila["porcentaje"])
            self.session.execute(ins)
            self.session.commit()
            # except:
            #    continue
        pass

    def procesar_rebajar_ventas(self):
        pass
