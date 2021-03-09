import json

# información general
# Message(INFO, título, descripción)
INFO = "INFO"

# error en el procesamiento
# Message(ERROR, título, descripción)
ERROR = "ERROR"

# indicador de avance
# Message(PROGRESS, título, descripción, nro_registro=[nro. registro en proceso], nro_total_registros=[total de registros a procesar])
PROGRESS = "PROGRESS"

# mensaje cuando se prcesa una factura
# Message(BILL, título, descripción, nro_factura=[número de factura], nro_id=[identificador])
BILL = "BILL"

# mensaje que indica inicio de procesamiento de vendedor
# Message(INIT, título, descripción)
INIT = "INIT"

# mensaje que indica fin de procesamiento de vendedor
# Message(FINISH, título, descripción)
FINISH = "FINISH"

# mensaje que indica la ausencia de un producto
# Message(MISSING, título, descripción, requirement_diff=[faltantes], product_code=[código producto])
MISSING = "MISSING"



class Message:
    def __init__(self, type: str, seller_code: str, title: str, description: str, **kwargs):
        self.code =  seller_code
        self.type = type
        self.title = title
        self.description =  description
        # transforma los argumentos en variables con el valor que viene asignado
        self.extra_params = kwargs

        self.__dict__.update(kwargs)

    def toJson(self):
        return json.dumps(self.__dict__)