import decimal, datetime
import json
from collections import OrderedDict

from passlib.context import CryptContext
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
                rowRegister[column.name] = item[idx]
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
        n = 0
        for column in table_columns:
            if column.name in columns:
                idx =  columns.index(column.name)
                rowRegister[column.name] = item[idx]
                colNumber = colNumber + 1

        return rowRegister


