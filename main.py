import asyncio
import base64
import datetime
import hashlib
import logging
import queue
import sys

from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi.responses import ORJSONResponse
from sqlalchemy import Date, text, func
from sse_starlette.sse import EventSourceResponse

from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from exceptions.dipalza_exception import DipalzaException
from models.user_model import User, Seller, Route, Client, Product, Pieces, \
    Encabezado_listado, Detalle_Listado, UserLogin, RegistroOutput, RegistroInput, SellCondition, FProduct, ResumenVenta, PositionRegister, \
    PositionRegisterOutput, PositionIem, ResumenVentaWeb, SellerCode, LogRegister
from sqlserver.basedipalza import Base, engine, Session
from sqlserver.db_name import t_MSOVENDEDOR, t_MSOSTTABLAS, t_MSOCLIENTES, t_ENCABEZADOCUMENTO, \
    t_DETALLEDOCUMENTO, t_NUMERADOS, t_EOS_USUARIOS, t_ARTICULO, t_EOS_REGISTROS, t_EOS_CONFIGURACION, t_EOS_POSITIONS, t_EOS_LOGVENTAS
from utils.messages import Message, ERROR
from utils.process_functions import DBProcessor
from utils.util import to_array_of_json, to_item_json, format_rut_with_points, format_position

import graphene
from starlette.graphql import GraphQLApp

from queries.ventas import QueryVenta, QueryEncabezado



# create logger with log app
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

dbProcessor = None
queue = queue.Queue()

Base.metadata.create_all(engine)

app = FastAPI(
    title="Ventas Dipalza",
    description="Sistema de ventas en línea de DIPALZA Ltda.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


# Dependency
def get_db():
    try:
        session = Session()
        yield session
    finally:
        session.close()


@app.exception_handler(DipalzaException)
async def unicorn_exception_handler(request: Request, exc: DipalzaException):
    return JSONResponse(
        status_code=418,
        content={"mensaje": f"[EOS-ERROR]! {exc.name}!"},
    )


def get_dbProcessor():
    global dbProcessor, queue
    if dbProcessor:
        return dbProcessor

    session = next(get_db())
    dbProcessor = DBProcessor(session, queue)

    return dbProcessor


@app.post('/login', response_model=User)
async def login(user: UserLogin):
    """
    Valida el acceso del usuario al sistema.
    :param user Usuario que se quiere conectar,  tiene atributos rut y password
    @return:  User que contiene la información requerida y el tokn correspondiente.
    """
    session = next(get_db())
    r = user.rut.strip().replace(".", "").replace("-", "")
    r = r.rjust(10, '0')
    vendedor = session.query(t_MSOVENDEDOR).filter(t_MSOVENDEDOR.c.rut == r, t_MSOVENDEDOR.c.tipo == 1).all()
    clave = session.query(t_EOS_USUARIOS).filter(t_EOS_USUARIOS.c.rut == r).all()

    if vendedor and clave:
        password_bytes = base64.b64decode(user.password)
        password = password_bytes.decode('ascii')
        m = hashlib.sha1(password.encode('utf-8'))
        if m.digest() == clave[0].password:
            upd = t_EOS_USUARIOS.update().where(t_EOS_USUARIOS.c.rut == r).values(lastlogin = datetime.datetime.now())
            session.execute(upd)
            return User(code=vendedor[0].codigo, name=vendedor[0].nombre, rut=r, token="123")
        else:
            raise HTTPException(status_code=400, detail="Clave incorrecta")

    raise HTTPException(status_code=400, detail="Usuario No encontrado")


@app.get('/routes', response_model=List[Route])
async def read_routes():
    """
    Obitiene listado de rutas que existentes en el sistema.
    """
    try:
        session = next(get_db())
        rutas = session.query(t_MSOSTTABLAS).filter(t_MSOSTTABLAS.columns.tabla == "017").all()
        result = to_array_of_json(rutas, t_MSOSTTABLAS, columns=("codigo", "descripcion"))
        return result
    except:
        logger.error("Error al tratar de obtener listado de rutas")
        raise HTTPException(status_code=400, detail="No existen rutas")



@app.get('/sellers', response_model=List[Seller])
async def read_sellers():
    """
    Obtiene listado de vendedores existentes en el sistema.
    """
    session = next(get_db())
    sellers = session.query(t_MSOVENDEDOR).all()
    # sellers = session.query(t_MSOVENDEDOR).filter(t_MSOVENDEDOR.c.tipo == 1).all()
    return to_array_of_json(sellers, t_MSOVENDEDOR, columns=("codigo", "nombre", "rut"))


@app.get('/seller/rut/{rut}', response_model=Seller)
async def read_seller_by_rut(rut: str):
    """
    Obtiene el vendedor asociado al rut.
    :param rut Rut del vendedor
    @return:  Datos del vendedor asociado al rut
    """
    session = next(get_db())
    r = rut.strip().replace(".", "").replace("-", "")
    r = r.rjust(10, '0')
    vendedores = session.query(t_MSOVENDEDOR).filter(t_MSOVENDEDOR.c.rut == r, t_MSOVENDEDOR.c.tipo == 1).all()
    columns = ("codigo", "nombre", "rut")
    return to_item_json(vendedores, t_MSOVENDEDOR, columns=columns)


@app.get('/sellconditions', response_model=List[SellCondition])
async def get_sell_conditions():
    """
    Obtiene listado de condiciones de venta.
    """
    session = next(get_db())
    t = t_MSOSTTABLAS
    condtions = session.query(t).filter(t.c.tabla == "009").values("codigo", "descripcion")

    lst = []
    for r in condtions:
        d = SellCondition(
            codigo=r[0],
            descripcion=r[1]
        )
        lst.append(d)

    return lst

@app.get('/sellcondition/{code}', response_model=SellCondition)
async def get_sell_condition(code: str):
    """
    Obtiene la condicion de venta con el código.
    """
    session = next(get_db())
    t = t_MSOSTTABLAS
    items = session.query(t).filter(t.c.tabla == "009", t.c.codigo == code).values("codigo", "descripcion")
    for r in items:
        condition = SellCondition(
            codigo=r[0],
            descripcion=r[1]
        )
        break
    return condition

@app.get('/clients/seller/{seller}/route/{route}', response_model=List[Client])
async def read_clients_of_seller_and_route(seller: str, route: str):
    """
    Obtiene listado de clientes asociados al par (vendedor, ruta).
    :param seller Vendedor del que se quieren los clientes.
    :param route  Ruta de donde se obtienen los clientes.
    @return JSON listado de clientes.
    """
    session = next(get_db())
    t = t_MSOCLIENTES
    clients = session.query(t).filter(t.c.Vendedor == seller, t.c.Ruta == route).all()
    return to_array_of_json(clients, t, columns=('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad'))


@app.get('/client/rut/{rut}', response_model=List[Client])
async def read_client_by_rut(rut: str):
    """
    Obtiene listado de clientes que cumplen un rut.
    Un cliente puede tener varias sucursales, cada una tiene el mismo rut y diferente código.
    :param rut Rut del usuario que se busca
    @return:  Datos del cliente
    """
    session = next(get_db())
    r = rut.strip().replace(".", "").replace("-", "")
    r = r.rjust(10, '0')
    client = session.query(t_MSOCLIENTES).filter(t_MSOCLIENTES.columns.rut == r).all()
    return to_array_of_json(client, t_MSOCLIENTES,
                            columns=('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad'))


@app.get('/client/code/{code}/rut/{rut}', response_model=Client)
async def read_client_by_rut_and_code(rut: str, code: str):
    """
    Obtiene el cliente que tiene el rut y codigo correspondiente
    :param rut El rut del cliente
    :param code Código asignado al cliente
    @return:  Cliente asociado a los parámetros
    """
    session = next(get_db())
    client = session.query(t_MSOCLIENTES).filter(t_MSOCLIENTES.columns.rut == rut,
                                                 t_MSOCLIENTES.columns.codigo == code).all()
    return to_item_json(client, t_MSOCLIENTES, columns=('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad'))


@app.get('/pieces/code/{code}', response_model=Pieces)
async def read_pieces_by_code(code: str):
    """
    Obtiene listado de piezas de productos numerados asociadas al código de producto.
    :param code El código de producto
    @return: JSON con la lista de piezas asociadas al código de producto.
    """
    session = next(get_db())
    numbered = session.query(t_NUMERADOS).filter(t_NUMERADOS.c.articulo == code).all()
    return Pieces.parse_obj(numbered)


@app.delete('/pieces/code/{correlative}', response_model=Pieces)
async def delete_pieces_by_correlative(correlative: int):
    """
    Elimina la piezas asociada al correlativo.
    :param correlative (int): Correlativo del producto numerado que se quiere eliminar.
    @return:  JSON: Pieza borrada
    """
    session = next(get_db())
    numbered = session.query(t_NUMERADOS).filter(t_NUMERADOS.correlativo == correlative).delete()
    return Pieces.parse_obj(numbered)

@app.get('/products', response_model=List[FProduct])
async def read_products():
    """
    Obtiene listado de productos desde la BD.
    @return: listado de FProduct
    """
    session = next(get_db())
    products = session.query(t_ARTICULO).all()
    return to_array_of_json(products, t_ARTICULO)

@app.get('/fproducts', response_model=List[FProduct])
async def read_fast_products():
    """
    Obtiene listado de productos.

    @return:  List[FProduct] El listado de productos, sin calcular el stock.
    """
    session = next(get_db())
    products = session.query(t_ARTICULO).all()
    return to_array_of_json(products, t_ARTICULO)


@app.get('/product/code/{code}', response_model=Product)
async def read_product_by_code(code: str):
    """
    Obtiene el producto asociado el código
    @param code:  Código de producto
    @return:  Producto asociado al códigp
    """
    session = next(get_db())
    p = get_dbProcessor().get_product_by_code(code, session)
    return p

@app.get('/fproduct/code/{code}', response_model=Product)
async def read_fast_product_by_code(code: str):
    """
    Obtiene el producto que corresponde al código ingresado
    :param code Código con el que se identifica el producto
    @return:  El producto con su stock.
    """
    session = next(get_db())
    p = get_dbProcessor().get_product_by_code(code, session)
    return p


@app.get('/sales/code/{code}/rut/{rut}/quantity/{quantity}', response_model=List[Encabezado_listado])
async def read_header_of_sales_of_client(code: str, rut: str, quantity: int):
    """
    Obtiene el encabezado de las últimas (quantity) ventas realizadas al cliente.
    La lista es ordenada de la más nueva a la más antigua.
    :param code Código del cliente
    :param rut Rut del cliente
    :param quantity Cantidad de ventas que quiere revisar.
    :return: Lista de cantidad de ventas
    """
    session = next(get_db())
    sales = session.query(t_ENCABEZADOCUMENTO). \
        filter(t_ENCABEZADOCUMENTO.c.rut == rut, t_ENCABEZADOCUMENTO.c.codigo == code,
               t_ENCABEZADOCUMENTO.c.tipo == '06', t_ENCABEZADOCUMENTO.c.vigente == 1). \
        order_by(t_ENCABEZADOCUMENTO.c.fecha.desc()). \
        limit(quantity)
    return to_array_of_json(sales, t_ENCABEZADOCUMENTO, columns=("rut", "codigo", "fecha", "id", "numero"))


@app.get('/sales/id/{id}', response_model=List[Detalle_Listado])
async def read_detail_of_sales_of_client(id: str):
    """
    Obtiene el detalle de ventas del id.
    :param id: Id del encabezado de ventas
    :return Lista de cantidad de ventas
    """
    session = next(get_db())
    details = session.query(t_DETALLEDOCUMENTO).filter(t_DETALLEDOCUMENTO.c.id == id).order_by("linea")
    return to_array_of_json(details, t_DETALLEDOCUMENTO,
                            columns=("articulo", "cantidad", "totallinea", "descripcion", "precioventa", "linea"))


@app.post('/registeritem/', response_model=RegistroOutput)
async def register_item_temporal_sale(registro: RegistroInput):
    """
    Almacena el registro de ventas en forma temporal en la BD
    :param : registro (RegistroInput): Registro con la información asociado a una venta.
    @return:  RegistroOutput: el registro almacenado
    """

    session = next(get_db())
    if registro.indice != 0:
        get_dbProcessor().eliminar_registro(registro.indice, session)

    if registro.esnumerado:
        register = get_dbProcessor().agregar_registro_numerado(registro, session)
        if not register:
            return Response("Hay 0 item de este producto", status_code=405)
        logger.info(f"EOS--> {type(register)}")
        return register

    register = get_dbProcessor().agregar_registro_no_numerado(registro, session)
    if register is None:
        return Response("Hay 0 item de este producto", status_code=405)
    return register


@app.delete('/removeregisteritem/')
async def delete_register_item_temporal_sale(registro: RegistroInput):
    """
    Elimina el registro temporal desde la BD
    :param registro (RegistroInput): El registro que se quiere eliminar
    @return:  RegistroInput: el registro eliminado
    """
    session = next(get_db())
    register = get_dbProcessor().eliminar_registro(registro.indice, session, response_class=ORJSONResponse)
    return register


@app.delete('/removeregisteritem/{indice}')
async def delete_register_item_temporal_sale(indice: int):
    """
    Elimina el registro temporal desde la BD
    :param indice:  El indice de BD del elemento
    @return: ORJSONResponse: el registro eliminado
    """

    session = next(get_db())
    register = get_dbProcessor().eliminar_registro(indice, session)
    json_compatible_item_data = jsonable_encoder(register)
    return JSONResponse(content=json_compatible_item_data)


@app.post('/registersale')
async def register_sales_by_sale(sale: SellerCode):
    """
    Registra todas las ventas realizadas, y sin confirmar del vendedor
    :param sale: vendedor al que se le quiere registrar todas sus ventas.
    """
    global queue

    session = next(get_db())
    result = await get_dbProcessor().procesar_ventas(sale.codigo, session)

    return result


@app.get('/listsales', response_model=List[ResumenVentaWeb])
async def list_sales():
    """Listado de todas las ventas pendientes, que no han sido confiradas.
    @return:  List[ResumenVentaWeb]: Listado con las ventas que han sido confirmadas.
    """
    session = next(get_db())
    v = t_MSOVENDEDOR
    # result = session.query(v).filter(v.c.tipo == 1).all()
    result = session.query(v).all()
    vendedores = {}
    for r in result:
        vendedores[r.codigo] = f"{r.codigo} {r.nombre}"

    c = t_MSOCLIENTES
    result = session.query(c).all()
    clientes = {}
    for r in result:
        # clientes[f"{r.Rut}-{r.Codigo}|"] = {"nombre": r.Razon, "rut": r.Rut, "codigo": r.Codigo}
        clientes[r.Rut] = r.Razon

    t = t_EOS_REGISTROS
    stmt = session.query(
        t.c.rut.label('rut'), t.c.codigo.label('codigo'), t.c.fecha.cast(Date).label("fecha"),
        t.c.vendedor.label("codigo_vendedor"),t.c.condicionventa.label('condicionventa'), func.sum(t.c.neto).label('neto'),
        func.sum(t.c.descuento).label('descuento'), func.sum(t.c.totalila).label('totalila'),
        func.sum(t.c.carne).label('carne'), func.sum(t.c.iva).label('iva')) \
        .group_by(t.c.rut, t.c.codigo, t.c.fecha.cast(Date), t.c.vendedor, t.c.condicionventa).order_by(t.c.fecha.cast(Date), t.c.vendedor, t.c.rut)

    result = session.execute(stmt)

    lst = []
    codigo_vendedor = ""
    rut = ""
    for r in result:
        if not r.codigo_vendedor in vendedores.keys():
            continue
        # nombre_cliente = clientes[f"{r.rut}-{r.codigo}|"]["nombre"]
        try:
            codigo_vendedor = r.codigo_vendedor
            nombre_vendedor = vendedores[r.codigo_vendedor]
            rut = r.rut
            nombre_cliente = clientes[rut]


            d = ResumenVentaWeb(
                rut=r.rut,
                codigo=r.codigo,
                nombre=nombre_cliente,
                fecha=r.fecha,
                condicionventa=r.condicionventa,
                neto=r.neto,
                descuento=r.descuento,
                totalila=r.totalila,
                carne=r.carne,
                iva=r.iva,
                codigo_vendedor=r.codigo_vendedor,
                nombre_vendedor=nombre_vendedor
            )
            lst.append(d)
        except:
            get_dbProcessor().grabar_log(Message(ERROR, codigo_vendedor, "El rut {rut} no existe en el sistema.", f"Error en el proceso: {sys.exc_info()[0]}"), session)

    return lst


@app.get('/listsales/sale/{sale}', response_model=List[ResumenVenta])
async def list_sales_by_sale(sale: str):
    """Registra todas las ventas del vendedor en el servidor de Dipalza.
    Se consideran todos los registros que se ha ingresado hasta el momento de la solicitud y que no han sido enviado previamente.
    :param sale (str): Código de vendedoro que solicita confirmar la venta.
    @return:  List[ResumenVenta]: Listado con las ventas que han sido confirmadas.
    """
    session = next(get_db())
    c = t_MSOCLIENTES
    result = session.query(c).all()
    clientes = {}
    for r in result:
        # clientes[f"{r.Rut}-{r.Codigo}|"] = {"nombre": r.Razon, "rut": r.Rut, "codigo": r.Codigo}
        clientes[r.Rut] = r.Razon

    t = t_EOS_REGISTROS
    stmt = session.query(
        t.c.rut.label('rut'), t.c.codigo.label('codigo'), t.c.fecha.cast(Date).label("fecha"),t.c.condicionventa.label('condicionventacode'),
        func.sum(t.c.neto).label('neto'),
        func.sum(t.c.descuento).label('descuento'), func.sum(t.c.totalila).label('totalila'),
        func.sum(t.c.carne).label('carne'), func.sum(t.c.iva).label('iva')) \
        .filter(t.c.vendedor == sale).group_by(t.c.rut, t.c.codigo, t.c.fecha.cast(Date), t.c.condicionventa)

    result = session.execute(stmt)

    lst = []
    for r in result:
        # nombre_cliente = clientes[f"{r.rut}-{r.codigo}|"]["nombre"]
        nombre_cliente = clientes[r.rut]

        d = ResumenVenta(
            rut=r.rut,
            codigo=r.codigo,
            nombre=nombre_cliente,
            fecha=r.fecha,
            condicionventacode = r.condicionventacode,
            neto=r.neto,
            descuento=r.descuento,
            totalila=r.totalila,
            carne=r.carne,
            iva=r.iva,
        )
        lst.append(d)

    return lst


@app.get('/listsales/sale/{sale}/rut/{rut}/date/{date}')
async def list_sale_by_sale_by_rut_by_date(sale: str, rut: str, date: int):
    """Listado de todos los registros de ventas por vendedor y cliente en una fecha determinada.
    :param sale (str): Código del vendedor
    :param rut (str): Rut del cliente.
    :param date (int): Fecha, el sistema considera solo la fecha. No considera hora, minutos y segundos.
    @return:  JSON: Listado de registros de ventas
    """

    session = next(get_db())
    t = t_EOS_REGISTROS

    fechai = datetime.datetime.fromtimestamp(date)
    details = session.query(t).filter(t.c.rut == rut, t.c.vendedor == sale, t.c.fecha.cast(Date) == fechai).order_by(
        "fila").all()
    return to_array_of_json(details, t_EOS_REGISTROS)


@app.get('/listonesale/{sale}/{rut}/{code}/{date}', response_model=List[RegistroOutput])
async def list_one_sale_by_sale_by_rut_by_date(sale: str, rut: str, code: str, date: str):
    """
    Listado de todos los registros de ventas por vendedor y cliente-código en una fecha determinada.
    :param sale (str): Código del vendedor
    :param rut (str): Rut del cliente.
    :param code (str): Código del cliente.
    :param date (int): Fecha, el sistema considera solo la fecha. No considera hora, minutos y segundos.
    @return:  JSON: Listado de registros de ventas
    """
    session = next(get_db())
    t = t_EOS_REGISTROS
    # fechai = datetime.datetime.fromtimestamp(date/1000)
    details = session.query(t).filter(t.c.rut == rut, t.c.codigo == code, t.c.vendedor == sale,
                                      t.c.fecha.cast(Date) == date).order_by("fila")
    results = []
    for r in details:
        d = RegistroOutput(
            indice=r.indice,
            rut=r.rut,
            codigo=r.codigo,
            vendedor=r.vendedor,
            fila=r.fila,
            articulo=r.articulo,
            cantidad=r.cantidad,
            neto=r.neto,
            descuento=r.descuento,
            codigo_ila=r.codigoila,
            ila=r.ila,
            carne=r.carne,
            iva=r.iva,
            precio=r.precio,
            numeros=r.numeros if r.numeros != None else "",
            correlativos=r.correlativos if r.correlativos != None else "",
            pesos=r.pesos if r.pesos != None else "",
            fecha=r.fecha,
            condicionventa=r.condicionventa)
        results.append(d)
    return results


@app.get('/listsales/sale/{sale}/rut/{rut}/code/{code}/date/{date}')
async def list_sale_by_sale_by_rut_by_date(sale: str, rut: str, code: str, date: int):
    """
    Listado de todos los registros de ventas por vendedor y cliente-código en una fecha determinada.

    :param sale (str): Código del vendedor
    :param rut (str): Rut del cliente.
    :param code (str): Código del cliente.
    :param date (int): Fecha, el sistema considera solo la fecha. No considera hora, minutos y segundos.

    @return:  JSON: Listado de registros de ventas
    """
    session = next(get_db())
    t = t_EOS_REGISTROS
    fechai = datetime.datetime.fromtimestamp(date / 1000)
    details = session.query(t).filter(t.c.rut == rut, t.c.codigo == code, t.c.vendedor == sale,
                                      t.c.fecha.cast(Date) == fechai).order_by("fila")

    return to_array_of_json(details, t_EOS_REGISTROS)


@app.get('/configuration')
async def get_configuration():
    session = next(get_db())
    t = t_EOS_CONFIGURACION
    details = session.query(t).all()
    return to_array_of_json(details, t)


@app.put('/regsiter/position', response_model=PositionRegisterOutput)
async def register_position(pos: PositionRegister):
    session = next(get_db())
    t = t_EOS_POSITIONS
    stmt = t.insert().values(vendedor=pos.vendedor, fecha=pos.fecha, latitude=pos.latitude, longitude=pos.longitude,
                             velocidad=pos.velocidad)
    r = session.execute(stmt)
    indice = r.inserted_primary_key[0]
    return PositionRegisterOutput(
        indice=indice,
        vendedor=pos.vendedor,
        fecha=pos.fecha,
        latitude=pos.latitude,
        longitude=pos.longitude,
        velocidad=pos.velocidad
    )


@app.get('/lastpositions', response_model=List[PositionIem])
async def list_last_positions():
    session = next(get_db())

    p = t_EOS_POSITIONS
    v = t_MSOVENDEDOR
    result = []

    stmt = text(
        "select p.indice, v.codigo, v.rut, v.nombre, p.fecha, p.latitude, p.longitude, p.velocidad from MSOVENDEDOR as v, EOS_POSITIONS as p "
        "where v.codigo = p.vendedor and v.tipo = 0  and p.fecha = (select max(fecha) from EOS_POSITIONS where vendedor = v.codigo)")
    registers = session.query("indice", "codigo", "rut", "nombre", "fecha", "latitude", "longitude",
                              "velocidad").from_statement(stmt).all()

    for register in registers:
        rut = format_rut_with_points(register[2])
        pos = format_position(register[5], register[6])
        output = PositionIem(
            code=register[1],
            rut=rut,
            name=register[3],
            date=register[4],
            latitude=register[5],
            longitude=register[6],
            position=pos,
            speed=register[7]
        )
        result.append(output)
    return result


@app.get('/positions/{code}', response_model=List[PositionIem])
async def positions(code: str):
    session = next(get_db())

    p = t_EOS_POSITIONS
    v = t_MSOVENDEDOR
    result = []
    registers = session.query(p.c.indice, v.c.codigo, v.c.rut, v.c.nombre, p.c.fecha, p.c.latitude, p.c.longitude,
                              p.c.velocidad).filter(v.c.codigo == p.c.vendedor, v.c.tipo == 0, v.c.codigo == code).all()
    for register in registers:
        rut = format_rut_with_points(register[2])
        pos = format_position(register[5], register[6])
        output = PositionIem(
            code=register[1],
            rut=rut,
            name=register[3],
            date=register[4],
            latitude=register[5],
            longitude=register[6],
            position=pos,
            speed=register[7]
        )
        result.append(output)
    return result


@app.get('/streamventa')
async def message_stream(request: Request):
    global queue

    async def event_generator():
        while True:
            # If client was closed the connection
            if await request.is_disconnected():
                break
            if queue.empty():
                await asyncio.sleep(1)
                continue
            m = queue.get()
            yield m.toJson()
            await asyncio.sleep(0.1)

    return EventSourceResponse(event_generator())


@app.get('/registerslog', response_model=List[LogRegister])
async def registers_log():
    """
    Listado de logs de ventas
    """
    result = []
    t = t_EOS_LOGVENTAS
    session = next(get_db())
    logs = session.query(t).all()
    if logs:
        for log in logs:
            l = LogRegister(id=log.id, vendedor=log.vendedor, mensaje=log.mensaje, fecha=log.fecha, tipo = log.tipo, titulo = log.titulo, json_parameters=log.json_parameters)
            result.append(l)

    return result


@app.get('/registerslogvendedor/{code}', response_model=List[LogRegister])
async def registers_log_vendedor(code: str):
    """
    Listado de logs de ventas
    """
    result = []
    t = t_EOS_LOGVENTAS
    session = next(get_db())
    logs = session.query(t).filter(t.c.vendedor == code).all()
    if logs:
        for log in logs:
            l = LogRegister(id=log.id, vendedor=log.vendedor, mensaje=log.mensaje, fecha=log.fecha, tipo = log.tipo, titulo = log.titulo, json_parameters=log.json_parameters)
            result.append(l)

    return result


@app.get('/registerslogfecha/{date}', response_model=List[LogRegister])
async def registers_log_fecha(date: datetime.datetime):
    """
    Listado de logs de ventas
    """
    result = []
    t = t_EOS_LOGVENTAS
    session = next(get_db())
    logs = session.query(t).filter(t.c.fecha.cast(Date) == date.date()).all()
    if logs:
        for log in logs:
            l = LogRegister(id=log.id, vendedor=log.vendedor, mensaje=log.mensaje, fecha=log.fecha, tipo = log.tipo, titulo = log.titulo, json_parameters=log.json_parameters)

            result.append(l)

    return result


@app.get('/registerslogvendedorfecha/{code}/{date}', response_model=List[LogRegister])
async def registers_log_code_fecha(code: str, date: datetime.datetime):
    """
    Listado de logs de ventas
    """

    session = next(get_db())

    result = []
    t = t_EOS_LOGVENTAS
    session = next(get_db())
    logs = session.query(t).filter(t.c.vendedor == code, t.c.fecha.cast(Date) == date.date()).all()
    if logs:
        for log in logs:
            l = LogRegister(id=log.id, vendedor=log.vendedor, mensaje=log.mensaje, fecha=log.fecha, tipo = log.tipo, titulo = log.titulo, json_parameters=log.json_parameters)

            result.append(l)

    return result






app.add_route("/graphqlventas", GraphQLApp(schema=graphene.Schema(query=QueryVenta)))
app.add_route("/graphqlencabezado", GraphQLApp(schema=graphene.Schema(query=QueryEncabezado)))



if __name__ == "__main__":
    get_dbProcessor()
    uvicorn.run(app, host="0.0.0.0", port=8888, debug=True)
