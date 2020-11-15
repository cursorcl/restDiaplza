from typing import List

import uvicorn

from fastapi import FastAPI, HTTPException
from restDiaplza.utils.util  import to_array_of_json, to_item_json


from restDiaplza.sqlserver.basedipalza import Base, engine,session
from  restDiaplza.sqlserver.db_name import t_MSOVENDEDOR, NUMERADO,t_MSOSTTABLAS, t_MSOCLIENTES, t_VIEW_STOCK
from restDiaplza.models.user_model import User, Seller, Route, Client, Product, Piece

Base.metadata.create_all(engine)
app = FastAPI(
    title="Ventas Dipalza",
    description="Sistema de ventas en línea de DIPALZA Ltda.",
    version="1.0.0",
)


@app.get('/login', response_model=User)
def login(rut: str, password: str):
    """
    Valida el acceso del user al sistema.
    @param rut: El rut del usuario válido en el sistema.
    @param password:  Clave de acceso del usuario.
    @return: Verdadero en caso que usuario se válido.
    """
    return True

@app.get('/routes', response_model=List[Route])
def read_routes():
    """
    Obitiene la lista de rutas que existentes en el sistema.
    @return: JSON con la lista de rutas.
    """
    rutas = session.query(t_MSOSTTABLAS).filter(t_MSOSTTABLAS.columns.tabla == "008").values("codigo", "descripcion")
    columns=("codigo", "descripcion")
    return to_array_of_json(rutas, t_MSOSTTABLAS, columns=columns)

@app.get('/sellers', response_model=List[Seller])
def read_sellers():
    """
    Obtiene la lista de vendedores existentes en el sistema.
    @return: JSON con la lista de vendedores.
    """
    sellers = session.query(t_MSOVENDEDOR).filter( t_MSOVENDEDOR.c.tipo == 1).values(t_MSOVENDEDOR.c.codigo, t_MSOVENDEDOR.c.nombre, t_MSOVENDEDOR.c.rut)
    return to_array_of_json(sellers, t_MSOVENDEDOR, columns=("codigo", "nombre", "rut"))


@app.get('/seller/rut/{rut}', response_model=Seller)
def read_seller_by_rut(rut: str):
    """
    Obtiene el vendedor asociado al rut
    @param rut: Rut del vendedor
    @return: Datos del vendedor asociado al rut
    """
    r = rut.strip().replace(".","").replace("-","")
    r = r.rjust(10,'0')
    vendedores = session.query(t_MSOVENDEDOR).filter( t_MSOVENDEDOR.c.rut ==  r, t_MSOVENDEDOR.c.tipo ==  1).values(t_MSOVENDEDOR.c.codigo, t_MSOVENDEDOR.c.nombre, t_MSOVENDEDOR.c.rut)
    columns = ("codigo", "nombre", "rut")
    return to_item_json(vendedores, t_MSOVENDEDOR, columns=columns)


@app.get('/clients/seller/{seller}/route/{route}', response_model=List[Client])
def read_clients_of_seller_and_route(seller: str, route: str):
    """
    Obtiene lista de clientes asociados al par vendedor-ruta
    @param seller: Vendedor del que se quieren los clientes
    @param route:  Ruta de donde se obtienen los clientes
    @return: JSON con la lista de clientes, con los campos rut, codigo, razon, telefono, direccion, ciudad.
    """
    clients = session.query(t_MSOCLIENTES).filter(t_MSOCLIENTES.columns.vendedor == seller, t_MSOCLIENTES.columns.ruta == route).values('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad')
    return to_array_of_json(clients, t_MSOCLIENTES, columns=('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad'))


@app.get('/client/rut/{rut}', response_model=List[Client])
def read_client_by_rut(rut: str ):
    """
    Obtiene lista de clientes que cumplen un rut
    @param rut:  Rut del usuario que se busca
    @return: Datos del cliente
    """
    r = rut.strip().replace(".","").replace("-","")
    r = r.rjust(10,'0')
    client = session.query(t_MSOCLIENTES).filter(t_MSOCLIENTES.columns.rut == r).values('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad')
    return to_array_of_json(client, t_MSOCLIENTES, columns=('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad'))

@app.get('/client/code/{code}/rut/{rut}', response_model=Client)
def read_client_by_rut_and_code(rut: str, code: str ):
    """
    Obtiene el cliente que tiene el rut y codigo correspondiente
    @param rut: El rut del cliente
    @param code: Código asignado al cliente
    @return: Cliente asociado a los parámetros
    """
    client = session.query(t_MSOCLIENTES).filter(t_MSOCLIENTES.columns.rut == rut, t_MSOCLIENTES.columns.codigo == code).values('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad')
    return to_item_json(client, t_MSOCLIENTES, columns=('rut', 'codigo', 'razon', 'telefono', 'direccion', 'ciudad'))

@app.get('/pieces/code/{code}', response_model=List[Piece])
def read_pieces_by_code(code: str):
    """
    Obtiene la lista de piezas asociadas al código de producto.
    @param code: El código de producto
    @return:  JSON con la lista de piezas asociadas al código de producto
    """
    numbered = session.query(NUMERADO).filter( NUMERADO.c.articulo == code).all()
    return to_array_of_json(numbered, NUMERADO)

@app.get('/products', response_model=List[Product])
def read_products():
    """
    Obtiene lista de productos con su stocks
    @return: Lista de productos
    """
    products = session.query(t_VIEW_STOCK).all()
    return to_array_of_json(products, t_VIEW_STOCK)

@app.get('/product/code/{code}',response_model=Product)
def read_product_by_code(code: str):
    """
    Obtiene el producto que corresponde al código ingresado
    @param code: Código con el que se identifica el producto
    @return:  El producto con su stock.
    """
    products = session.query(t_VIEW_STOCK).filter( t_VIEW_STOCK.c.articulo == code).all()
    return to_item_json(products, t_VIEW_STOCK)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8099)