from collections import UserList
import base64
import datetime
from sqlalchemy import Date

from typing import List

import uvicorn

import logging

from fastapi import FastAPI, HTTPException
import logging

from fastapi.responses import ORJSONResponse
from sqlalchemy import func, sql
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from exceptions.dipalza_exception import DipalzaException
from utils.process_functions import  DBProcessor
from utils.util import to_array_of_json, to_item_json, to_RegistroOutput
import hashlib

from sqlserver.basedipalza import Base, engine, session
from sqlserver.db_name import t_MSOVENDEDOR, t_MSOSTTABLAS, t_MSOCLIENTES, t_ENCABEZADOCUMENTO, \
    t_DETALLEDOCUMENTO, t_NUMERADOS, t_View_Stock, t_EOS_USUARIOS, t_ARTICULO, t_ARTICULOSNUMERADOS, t_INVDETALLEPARTES, \
    t_EOS_REGISTROS
from models.user_model import User, Seller, Route, Client, Product, Piece, Pieces, \
    Encabezado_listado, Detalle_Listado, UserLogin, RegistroOutput, RegistroInput, SellCondition, SaleConfirmByClient, \
    SaleConfirmBySeller, FProduct, ResumenVenta

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


Base.metadata.create_all(engine)
app = FastAPI(
    title="Ventas Dipalza",
    description="Sistema de ventas en línea de DIPALZA Ltda.",
    version="1.0.0",
)

@app.exception_handler(DipalzaException)
async def unicorn_exception_handler(request: Request, exc: DipalzaException):
    return JSONResponse(
        status_code=418,
        content={"mensaje": f"[EOS-ERROR]! {exc.name}!"},
    )

dbProcessor = DBProcessor(session)

@app.post('/login', response_model=User)
def login(user: UserLogin):
    """
    Valida el acceso del user al sistema.
    :param user: Usuario que tiene los atributos rut y password
    @return: User que contiene la información requerida
    """
    r = user.rut.strip().replace(".", "").replace("-", "")
    r = r.rjust(10, '0')
    vendedor = session.query(t_MSOVENDEDOR).filter(t_MSOVENDEDOR.c.rut == r, t_MSOVENDEDOR.c.tipo == 1).all()
    clave = session.query(t_EOS_USUARIOS).filter(t_EOS_USUARIOS.c.rut == r).all()

    if vendedor and clave:
        password_bytes = base64.b64decode(user.password)
        password = password_bytes.decode('ascii')
        m = hashlib.sha1(password.encode('utf-8'))
        if m.digest() == clave[0].password:
            return User(code=vendedor[0].codigo, name=vendedor[0].nombre, rut=r, token="123")
        else:
            raise HTTPException(status_code=400, detail="Clave incorrecta")

    raise HTTPException(status_code=400, detail="Usuario No encontrado")

@app.get('/routes', response_model=List[Route])
def read_routes():
    """
    Obitiene la lista de rutas que existentes en el sistema.
    """
    try:
        rutas = session.query(t_MSOSTTABLAS).filter(t_MSOSTTABLAS.columns.tabla == "008").all()
        result = to_array_of_json(rutas, t_MSOSTTABLAS, columns=("codigo", "descripcion"))
        return result
    except:
        logger.error("Error al tratar de obtener listado de rutas")
        raise HTTPException(status_code=400, detail="No existen rutas")

@app.get('/sellers', response_model=List[Seller])
def read_sellers():
    """
    Obtiene la lista de vendedores existentes en el sistema.
    """
    sellers = session.query(t_MSOVENDEDOR).filter(t_MSOVENDEDOR.c.tipo == 1).all()
    return to_array_of_json(sellers, t_MSOVENDEDOR, columns=("codigo", "nombre", "rut"))

@app.get('/seller/rut/{rut}', response_model=Seller)
def read_seller_by_rut(rut: str):
    """
    Obtiene el vendedor asociado al rut
    @param rut: Rut del vendedor
    @return: Datos del vendedor asociado al rut
    """
    r = rut.strip().replace(".", "").replace("-", "")
    r = r.rjust(10, '0')
    vendedores = session.query(t_MSOVENDEDOR).filter(t_MSOVENDEDOR.c.rut == r, t_MSOVENDEDOR.c.tipo == 1).all()
    columns = ("codigo", "nombre", "rut")
    return to_item_json(vendedores, t_MSOVENDEDOR, columns=columns)

@app.get('/sellconditions', response_model=List[SellCondition])
def get_sell_conditions():
    condtions = t_MSOSTTABLAS.filter(t_MSOSTTABLAS.c.tabla == "009").values("codigo", "descripcion", "valor")
    result = to_array_of_json(condtions, t_MSOSTTABLAS, columns=("codigo", "descripcion", "valor"))
    return result

@app.get('/clients/seller/{seller}/route/{route}', response_model=List[Client])
def read_clients_of_seller_and_route(seller: str, route: str):
    """
    Obtiene lista de clientes asociados al par vendedor-ruta
    @param seller: Vendedor del que se quieren los clientes
    @param route:  Ruta de donde se obtienen los clientes
    @return: JSON con la lista de clientes, con los campos rut, codigo, razon, telefono, direccion, ciudad.
    """
    t = t_MSOCLIENTES
    clients = session.query(t).filter(t.c.Vendedor == seller, t.c.Ruta == route).all()
    return to_array_of_json(clients, t,
                            columns=('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad'))

@app.get('/client/rut/{rut}', response_model=List[Client])
def read_client_by_rut(rut: str):
    """
    Obtiene lista de clientes que cumplen un rut
    @param rut:  Rut del usuario que se busca
    @return: Datos del cliente
    """
    r = rut.strip().replace(".", "").replace("-", "")
    r = r.rjust(10, '0')
    client = session.query(t_MSOCLIENTES).filter(t_MSOCLIENTES.columns.rut == r).all()
    return to_array_of_json(client, t_MSOCLIENTES,
                            columns=('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad'))

@app.get('/client/code/{code}/rut/{rut}', response_model=Client)
def read_client_by_rut_and_code(rut: str, code: str):
    """
    Obtiene el cliente que tiene el rut y codigo correspondiente
    @param rut: El rut del cliente
    @param code: Código asignado al cliente
    @return: Cliente asociado a los parámetros
    """
    client = session.query(t_MSOCLIENTES).filter(t_MSOCLIENTES.columns.rut == rut,
                                                 t_MSOCLIENTES.columns.codigo == code).all()
    return to_item_json(client, t_MSOCLIENTES, columns=('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad'))

@app.get('/pieces/code/{code}', response_model=Pieces)
def read_pieces_by_code(code: str):
    """
    Obtiene la lista de piezas asociadas al código de producto.
    @param code: El código de producto
    @return:  JSON con la lista de piezas asociadas al código de producto
    """
    numbered = session.query(t_NUMERADOS).filter(t_NUMERADOS.articulo == code).all()
    return Pieces.parse_obj(numbered)

@app.delete('/pieces/code/{correlative}', response_model=Pieces)
def delete_pieces_by_correlative(correlative: int):
    numbered = session.query(t_NUMERADOS).filter(t_NUMERADOS.correlativo == correlative).delete()
    session.flush()
    session.commit()
    return Pieces.parse_obj(numbered)

@app.get('/fproducts', response_model=List[FProduct])
def read_fast_prodcuts():
    products = session.query(t_ARTICULO).all()
    return to_array_of_json(products, t_ARTICULO)

@app.get('/fproduct/code/{code}', response_model=Product)
def read_fast_product_by_code(code: str):
    """
    Obtiene el producto que corresponde al código ingresado
    @param code: Código con el que se identifica el producto
    @return:  El producto con su stock.
    """

    t = t_ARTICULO
    products = session.query(t).filter(t.c.Articulo == code).all()
    pr = products[0]

    p = Product(Articulo = pr.Articulo, Descripcion = pr.Descripcion, VentaNeto = pr.VentaNeto, PorcIla = pr.PorcIla, PorcCarne = pr.PorcCarne, Unidad = pr.Unidad, Stock = 0, Pieces = 0, Numbered = False)

    t = t_ARTICULOSNUMERADOS
    exists = session.query(t).filter(t.c.articulo == code).scalar() is not None
    if exists:
        # es numerado
        t = t_NUMERADOS
        wc = session.query(func.sum(t.c.peso), func.count(t.c.peso)).filter(t.c.articulo == code).all()
        if wc and len(wc) > 0:
            p.Stock = wc[0][0]
            p.Pieces = wc[0][1]
    else:

        d = t_DETALLEDOCUMENTO
        e = t_ENCABEZADOCUMENTO
        t = t_INVDETALLEPARTES
        suma = session.query(func.coalesce(func.sum(t.c.Cantidad), 0)).filter(t.c.Articulo == code, t.c.Tipoid == 17, t.c.Local == '000').scalar()
        resta = session.query(func.coalesce(func.sum(t.c.Cantidad), 0)).filter(t.c.Articulo == code, t.c.Tipoid == 18, t.c.Local == '000').scalar()

        suma_1 = session.query(func.coalesce(func.sum(d.c.Cantidad), 0)).select_from(e).join(d, d.c.Id == e.c.Id).filter( d.c.Tipoid == '09', d.c.Local == '000', e.c.Vigente == 1, d.c.Articulo == code).scalar()
        resta_1 = session.query(func.coalesce(func.sum(d.c.Cantidad), 0)).select_from(e).join(d, d.c.Id == e.c.Id).filter( d.c.Tipoid.in_(['06', '10']),
                                                                              d.c.Local == '000', e.c.Vigente == 1, d.c.Articulo == code).scalar()
        p.Stock = suma - resta + suma_1 - resta_1

    return p


@app.get('/products', response_model=List[Product])
def read_products():
    """
    Obtiene lista de productos con su stocks
    @return: Lista de productos
    """
    products = session.query(t_View_Stock).all()
    return to_array_of_json(products, t_View_Stock)

@app.get('/product/code/{code}', response_model=Product)
def read_product_by_code(code: str):
    """
    Obtiene el producto que corresponde al código ingresado
    @param code: Código con el que se identifica el producto
    @return:  El producto con su stock.
    """
    products = session.query(t_View_Stock).filter(t_View_Stock.c.articulo == code).all()
    return to_item_json(products, t_View_Stock)

@app.get('/sales/code/{code}/rut/{rut}/quantity/{quantity}', response_model=List[Encabezado_listado])
def read_header_of_sales_of_client(code: str, rut: str, quantity: int):
    """
    Obtiene el encabezado de las últimas (quantity) ventas realizadas al cliente.
    La lista es ordenada de la más nueva a la más antigua.
    :param code: Código del cliente
    :param rut: Rut del cliente
    :param quantity: Cantidad de ventas que quiere revisar.
    :return: Lista de cantidad de ventas
    """
    sales = session.query(t_ENCABEZADOCUMENTO). \
        filter(t_ENCABEZADOCUMENTO.c.rut == rut, t_ENCABEZADOCUMENTO.c.codigo == code,
               t_ENCABEZADOCUMENTO.c.tipo == '06', t_ENCABEZADOCUMENTO.c.vigente == 1). \
        order_by(t_ENCABEZADOCUMENTO.c.fecha.desc()). \
        limit(quantity)
    return to_array_of_json(sales, t_ENCABEZADOCUMENTO, columns=("rut", "codigo", "fecha", "id", "numero"))

@app.get('/sales/id/{id}', response_model=List[Detalle_Listado])
def read_detail_of_sales_of_client(id: str):
    """
    Obtiene el detalle de ventas del id.
    :param id: Id del encabezado de ventas
    :return: Lista de cantidad de ventas
    """
    details = session.query(t_DETALLEDOCUMENTO).filter(t_DETALLEDOCUMENTO.c.id == id).order_by("linea")
    return to_array_of_json(details, t_DETALLEDOCUMENTO,
                            columns=("articulo", "cantidad", "totallinea", "descripcion", "precioventa", "linea"))

@app.post('/registeritem/', response_model=RegistroOutput)
def register_item_temporal_sale(registro: RegistroInput):
    """
    Almacena el registro de ventas en forma temporal en la BD
    :param registro: Registro con la información asociado a una venta.
    :return:
    """
    if registro.indice != 0:
        dbProcessor.eliminar_registro(registro.indice)

    if registro.esnumerado:
        register = dbProcessor.agregar_registro_numerado(registro)
        if not register:
            return Response("Hay 0 item de este producto", status_code=405)
        logger.info(f"EOS--> {type(register)}")
        return register

    register = dbProcessor.agregar_registro_no_numerado(registro)
    if register is None:
        return Response("Hay 0 item de este producto", status_code=405)
    return register

@app.delete('/removeregisteritem/')
def delete_register_item_temporal_sale(registro: RegistroInput):
    """
    Elimina el registro temporal desde la BD
    @param registro:  El registro que se quiere eliminar
    @return:  el registro eliminado
    """
    register = dbProcessor.eliminar_registro(registro.indice, response_class=ORJSONResponse)
    return [{"result": register}]

@app.delete('/removeregisteritem/{indice}')
def delete_register_item_temporal_sale(indice: int, response_class=ORJSONResponse):
    """
    Elimina el registro temporal desde la BD
    @param indice:  El indice de BD del elemento
    @return:  el registro eliminado
    """
    register = dbProcessor.eliminar_registro(indice)
    return [{"result": register}]


@app.post('/registersale')
def register_sales_by_client(register : SaleConfirmByClient):
    """
    Registra una venta realizada, esto corresponde a generar la o las facturas correspondientes a la venta que tiene el vendedor.

    @param code:
    @return:
    """
    dbProcessor.process_venta(register)

@app.post('/registersale/{sale}')
def register_sale_by_seller(sale: str):
    """
    Registra todas las ventas realizadas, esto corresponde a generar las facturas correspondientes a la venta que tiene el vendedor.
    @param sale: El vendedor que registra la venta.
    @return:
    """
    dbProcessor.procesar_ventas(sale)

@app.get('/listsales/sale/{sale}', response_model=List[ResumenVenta])
def list_sales_by_sale(sale: str):


    t = t_EOS_REGISTROS
    stmt = session.query(
        t.c.rut.label('rut'), t.c.codigo.label('codigo'), t.c.fecha.cast(Date).label("fecha"), func.sum(t.c.neto).label('neto'),
        func.sum(t.c.descuento).label('descuento'), func.sum(t.c.totalila).label('totalila'),
        func.sum(t.c.carne).label('carne'), func.sum(t.c.iva).label('iva'))\
        .filter(t.c.vendedor == sale).group_by(t.c.rut, t.c.codigo, t.c.fecha.cast(Date))

    result = session.execute(stmt)


    lst = []
    for row in result:
        d = dict(zip(row.keys(), row))

        lst.append(d)

    return lst

@app.get('/listsales/sale/{sale}/rut/{rut}/date/{date}')
def list_sale_by_sale_by_rut_by_date(sale: str, rut: str, date:int):
    t = t_EOS_REGISTROS

    fechai = datetime.datetime.fromtimestamp(date)
    details = session.query(t).filter(t.c.rut == rut,  t.c.vendedor == sale, t.c.fecha.cast(Date) == fechai).order_by("fila").all()
    return to_array_of_json(details, t_EOS_REGISTROS)

@app.get('/listsales/sale/{sale}/rut/{rut}/code/{code}/date/{date}')
def list_sale_by_sale_by_rut_by_date(sale: str, rut: str, code:str, date:int):
    t = t_EOS_REGISTROS
    fechai = datetime.datetime.fromtimestamp(date)
    details = session.query(t).filter(t.c.rut == rut, t.c.codigo == code, t.c.vendedor == sale, t.c.fecha.cast(Date) == fechai).order_by("fila")

    return to_array_of_json(details, t_EOS_REGISTROS)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)
