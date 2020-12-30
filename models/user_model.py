from typing import Optional, List, Dict
from pydantic import BaseModel
from datetime import datetime

from pydantic.schema import date


class UserLogin(BaseModel):
    """
    Usuario de entrada en el login
    """
    rut: str
    password: str


class User(BaseModel):
    """
    Usuario de salida del login
    """
    code: str
    name: str
    rut: str
    token: str


class Client(BaseModel):
    """
    Resultado de cliente
    """
    Rut: str
    Codigo: str
    Razon: str
    Direccion: str
    Telefono: str
    Ciudad: str


class Seller(BaseModel):
    Codigo: str
    Rut: str
    Nombre: str


class Route(BaseModel):
    codigo: str
    descripcion: str


class Piece(BaseModel):
    articulo: str
    correlativo: int
    peso: float
    numero: int
    narticulo: int

    class Config:
        orm_mode = True


class Pieces(BaseModel):
    __root__: List[Piece]


class Product(BaseModel):
    Articulo: str
    Descripcion: str
    VentaNeto: float
    PorcIla: float
    PorcCarne: float
    Unidad: str
    Stock: float
    Pieces: int
    Numbered: bool

class FProduct(BaseModel):
    Articulo: str
    Descripcion: str
    VentaNeto: float
    PorcIla: float
    PorcCarne: float
    Unidad: str


class Encabezado_listado(BaseModel):
    """
    Corresponde al encabezado que de ventas utilizado para mostrar el listado de ventas.
    """
    rut: str
    codigo: str
    fecha: datetime
    id: str  # número de identificación en la BD
    numero: str  # número de factura


class Detalle_Listado(BaseModel):
    """
    Corresponde al cada una de ls filas del detalle de ventas utilizado para mostrar el listado de ventas.
    """
    articulo: str
    descripcion: str
    cantidad: float
    totallinea: float
    precioventa: float
    linea: str


class ResumenVenta(BaseModel):
    """
    Corresponde al resumen de una venta asociada a un vendedor y cliente.
    """
    rut: str
    codigo: str
    fecha: date
    neto: Optional[float]
    descuento: Optional[float]
    totalila: Optional[float]
    carne: Optional[float]
    iva: Optional[float]


class RegistroInput(BaseModel):
    """
    Corresponde al detalle de ventas que debe enviar el vendedor cuando quiere registrar un item.
    """
    indice: int # el correlativo que le asigna la BD para crear no, debe ser 0
    fila: int # el número de orden en el registro de pedidos
    rut: str # el rut del usuario al que se le está realizando la venta
    codigo: str # el código asociado al cliente si es que hay más de uno con el mismo rut
    vendedor: str # el código del vendedor que está realizando la venta
    articulo: str  # código del producto
    cantidad: float  # cantidad vendida (en el caso que es numerado corresponde al peso)
    descuento: float  # porcentaje de descuento aplicado
    esnumerado: bool  # indicador si el producto es numerado
    sobrestock: bool  # indicador si el vendedor está solicitando más productos que los que existen.
    fecha: datetime # fecha de la venta

class RegistroOutput(BaseModel):
    """
    Es el valor restornado por el servicio una vez que ha registrado el item de venta.
    """
    indice: int # el correlativo que le asigna la BD para crear no, debe ser 0
    rut: str # el rut del usuario al que se le está realizando la venta
    codigo: str  # el código asociado al cliente si es que hay más de uno con el mismo rut
    vendedor: str # el código del vendedor que está realizando la venta
    fila: int  # número de fila del prodcuto.
    articulo: str  # código del producto
    cantidad: float  # cantidad vendida (en el caso que es numerado corresponde al peso)
    neto: float  # total neto del registro sin descuentos
    descuento: float  # valor del descuento aplicado
    codigo_ila: str # código del ila aplicado
    ila: float  # porcentaje de ila aplicado
    carne: float  # valor del impuesto por carne de la venta
    iva: float  # valor del impuesto iva de la venta
    precio: float  # precio de venta del producto en el registro
    numeros: str  # números de producto numerado asociados de acuerdo a la cantidad solicitada. Separadaso por ;
    correlativos: str  # correlativos del producto numerado asociados de acuerdo a la cantidad solicitada. Separadaso por ;
    pesos: str # los peso de los productos numerados
    fecha: datetime # fecha y hora de la operación

class SellCondition(BaseModel):
    """
    Listado de condición de venta
    """
    codigo: str
    descripcion: str
    valor: float


class SaleConfirmByClient(BaseModel):
    """
        Confirmación de las ventas de un cliente
    """
    rut: str # corresponde al rut del cliente al que se le quiere registrar la venta en el sistema final
    codigo: str # el código del cliente si es que tiene un código
    vendedor: str # código del vendedor que está realizando la venta
    condicion_venta: str # números de días de la condición de venta
    fecha: datetime

class SaleConfirmBySeller(BaseModel):
    """
        Confirmación de todas las ventas de un vendedor.
    """
    vendedor: str # código del vendedor que está realizando la venta

class PositionRegister(BaseModel):
    """
        Confirmación de todas las ventas de un vendedor.
    """
    vendedor: str # código del vendedor que está realizando la venta
    fecha: datetime
    latitude: float
    longitude: float
    velocidad: float

class PositionRegisterOutput(BaseModel):
    """
        Confirmación de todas las ventas de un vendedor.
    """
    indice: int
    vendedor: str # código del vendedor que está realizando la venta
    fecha: datetime
    latitude: float
    longitude: float
    velocidad: float
