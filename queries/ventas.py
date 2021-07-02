import graphene
from graphene import Field, String

from sqlserver.basedipalza import Session
from sqlserver.db_name import t_EOS_REGISTROS, t_ENCABEZADOCUMENTO


class Venta(graphene.ObjectType):
    rut = graphene.String()
    vendedor = graphene.String()
    fecha = graphene.DateTime()
    articulo = graphene.String()


class QueryVenta(graphene.ObjectType):
    ventas = graphene.List(Venta)

    @staticmethod
    def resolve_ventas(self, info):
        records = []
        session = Session()
        sellers = session.query(t_EOS_REGISTROS).all()

        for c in sellers:
            records.append({'rut': c[0], 'vendedor': c[1], 'fecha': c[2], 'articulo': c[3]})

        return records



class Encabezado(graphene.ObjectType):
    rut = graphene.String()
    id = graphene.String()
    fecha = graphene.DateTime()
    numero = graphene.String()


class QueryEncabezado(graphene.ObjectType):
    encabezados = Field(graphene.List(Encabezado), id=String(), tipo=String())


    def resolve_encabezados(self, info, id=None, tipo=None):
        records = []
        session = Session()
        sellers = None
        if(id and tipo):
            sellers = session.query(t_ENCABEZADOCUMENTO).filter(t_ENCABEZADOCUMENTO.c.Id == id, t_ENCABEZADOCUMENTO.c.Tipo == tipo).all()
        else:
            sellers = session.query(t_ENCABEZADOCUMENTO).all()
        for c in sellers:
            records.append({'rut': c[3], 'id': c[31], 'fecha': c[5], 'numero': c[33]})
        return records