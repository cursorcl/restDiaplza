from passlib.context import CryptContext
from models.user_model import RegistroOutput
from sqlserver.db_name import t_EOS_REGISTROS
import datetime

import re


# Clase de poyo al proceso de rectificación de unidades en la venta
class Registro_Rectificado:
   def __init__(self, dict: dict):
       self.codigo = dict['codigo']
       self.vendedor = dict['vendedor']
       self.fila = dict['fila']
       self.fecha = dict['fecha']
       self.articulo = dict['articulo']
       self.cantidad = dict['cantidad']
       self.neto = dict['neto']
       self.descuento = dict['descuento']
       self.codigoila = dict['codigoila']
       self.ila = dict['ila']
       self.rut = dict['rut']
       self.carne = dict['carne']
       self.iva = dict['iva']
       self.precio = dict['precio']
       self.numeros = dict['numeros']
       self.correlativos = dict['correlativos']
       self.pesos = dict['pesos']
       self.esnumerado = dict['esnumerado']
       self.totalila = dict['totalila']
       self.Costo = dict['Costo']
       self.Descripcion = dict['Descripcion']


pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)


def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

def to_array_of_json(items, table, **attributes):
    """
    Retorna los items asociados a la table como un elemento json o un arreglo json
    @param items: Valores que se quieren transformar a json
    @param table: Tabla de donde se obtienen los nombres de campo
    @return: Items transformados a json.
    """
    result = []
    columns = attributes["columns"] if "columns" in attributes else None
    if columns is None:
        for item in items:
            rowRegister = {}
            colNumber = 0
            for column in table.columns:
                rowRegister[column.name] = item[colNumber]
                colNumber = colNumber + 1
            result.append(rowRegister)
        return result

    for item in items:
        rowRegister = {}
        colNumber = 0
        table_columns = table.columns
        n = 0
        upper_columnns = [x.upper() for x in columns]
        for column in table_columns:
            if column.name.upper() in upper_columnns:
                idx =  upper_columnns.index(column.name.upper())
                rowRegister[column.name] = item[colNumber]
            colNumber = colNumber + 1

        result.append(rowRegister)
    return result

def to_item_json(items, table, **attributes):
    """
    Retorna el primer item asociado a la table como un elemento json
    @param items: Valores que se quieren transformar a json
    @param table: Tabla de donde se obtienen los nombres de campo
    @return: Items transformados a json.
    """
    columns = attributes["columns"] if "columns" in attributes else None
    if columns is None:
        for item in items:
            rowRegister = {}
            colNumber = 0
            for column in table.columns:
                rowRegister[column.name] = item[colNumber]
                colNumber = colNumber + 1
            return rowRegister

    for item in items:
        rowRegister = {}
        colNumber = 0
        table_columns = table.columns
        for column in table_columns:
            if column.name in columns:
                rowRegister[column.name] = item[colNumber]
            colNumber = colNumber + 1

        return rowRegister

def to_RegistroOutput(register: t_EOS_REGISTROS):
    r = RegistroOutput(
        indice= register.indice,
        rut=register.rut,
        codigo=register.codigo,
        vendedor=register.vendedor,
        fila=register.fila,
        fecha=register.fecha,
        articulo=register.articulo,
        cantidad=register.cantidad,
        neto=register.neto,
        descuento=register.descuento,
        ila=register.ila,
        carne=register.carne,
        iva=register.iva,
        precio=register.precio,
        numeros=register.numeros,
        correlativos=register.correlativos,
        pesos=register.pesos,
        esnumerado=register.esnumerado
    )
    return r

def format_rut_with_points(rut:str):
    str_rut = rut.strip().replace(".","").replace("-","").upper()
    verification_number= str_rut[-1]
    value_number = str_rut[:-1]
    str_number = re.sub('\D', "", value_number)
    number = int(str_number)
    str_number =f"{number:,}".replace(",", ".")
    return f"{str_number}-{verification_number}"

def format_position(latitude: float, longitude: float):
    lat = float_lat_to_str(latitude)
    lon = float_lon_to_str(longitude)
    return f"{lat} {lon}"

def float_lat_to_str(lat: float):
    h = "S" if lat < 0 else "N"
    l = abs(lat)
    g = int(l)
    l = (l - g) * 60
    m = int(l)
    l = (l - m) * 60
    s = l
    return f"{g:02}º{m:02}'{s:05.02f}''[{h}]"

def float_lon_to_str(lon: float):
    h = "W" if lon < 0 else "E"
    l = abs(lon)
    g = int(l)
    l = (l - g) * 60
    m = int(l)
    l = (l - m) * 60
    s = l
    return f"{g:03}º{m:02}'{s:05.02f}''[{h}]"



