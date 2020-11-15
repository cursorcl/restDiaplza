from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    code:str
    name:str
    rut:str
    token:str

class Client(BaseModel):
    rut: str
    codigo: str
    razon: str
    direccion: str
    telefono: str
    ciudad: str

class Seller(BaseModel):
    codigo: str
    rut: str
    nombre: str


class Route(BaseModel):
    codigo: str
    descripcion: str

class Piece(BaseModel):
    articulo: str
    numero: int
    correlativo: int
    peso: float
    narticulo: int

class Product(BaseModel):
    articulo: str
    descripcion: str
    ventaneto: float
    porcila: float
    porccarne: float
    unidad: str
    stock: float
    pieces: int
    numbered: bool



