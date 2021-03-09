import json
import os

config = {}
if (os.path.exists('config.json')):
    with open('config.json') as config_file:
        config = json.load(config_file)

electronic_bill_enabled = config['factura_electronica'] if config['factura_electronica'] else True
numero_lineas_factura = config['numero_lineas_factura'] if config['numero_lineas_factura'] else 25
local = config['local'] if config['local'] else "000"
tipo_documento = config['tipo_documento'] if config['tipo_documento'] else "06"
paridad = config['paridad'] if config['paridad'] else 1.0
database_ip = config['database_ip'] if config['database_ip'] else "localhost"
database_port = config['database_port'] if config['database_port'] else "1433"
database_user = config['database_user'] if config['database_user'] else "c2E"
database_password = config['database_password'] if config['database_password'] else "X2wyajFyczI"
database_name = config['database_name'] if config['database_name'] else "TUFTVEVSU09GVA=="
validar_stock = config['validar_stock'] if config['validar_stock'] else False