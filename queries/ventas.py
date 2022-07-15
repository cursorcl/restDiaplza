import graphene
from graphene import Field, String, ObjectType
from sqlalchemy import cast, func, Table, DATE, extract

from sqlserver.basedipalza import Session
from sqlserver.db_name import t_ENCABEZADOCUMENTO, t_MSOCLIENTES, t_TOTALDOCUMENTO, t_MSOVENDEDOR, t_MSOSTTABLAS


def query_by_day(fecha_inicial, fecha_final):
    t: Table = t_TOTALDOCUMENTO
    e: Table = t_ENCABEZADOCUMENTO
    c: Table = t_MSOCLIENTES
    session = Session()
    sellers = session.query(
        func.sum(t.c.TotalNeto).label("totalNeto"),
        c.c.Vendedor.label("vendedor"),
        c.c.Ruta.label("ruta"),
        func.year(e.c.Fecha).label("year"),
        cast(e.c.Fecha, DATE).label("periodo")
    ) \
        .join(e, t.c.Id == e.c.Id).filter(e.c.Vigente == 1) \
        .join(c, e.c.Rut == c.c.Rut and e.c.Codigo == c.c.Codigo) \
        .filter(t.c.TipoId == '06').filter(e.c.Fecha.between(fecha_inicial, fecha_final)) \
        .group_by(c.c.Vendedor, c.c.Ruta, func.year(e.c.Fecha), cast(e.c.Fecha, DATE)).all()
    return sellers


def query_by_week(fecha_inicial, fecha_final):
    t: Table = t_TOTALDOCUMENTO
    e: Table = t_ENCABEZADOCUMENTO
    c: Table = t_MSOCLIENTES
    session = Session()
    sellers = session.query(
        func.sum(t.c.TotalNeto).label("totalNeto"),
        c.c.Vendedor.label("vendedor"),
        c.c.Ruta.label("ruta"),
        func.year(e.c.Fecha).label("year"),
        extract('week', e.c.Fecha).label("periodo")
    ) \
        .join(e, t.c.Id == e.c.Id).filter(e.c.Vigente == 1) \
        .join(c, e.c.Rut == c.c.Rut and e.c.Codigo == c.c.Codigo) \
        .filter(t.c.TipoId == '06').filter(e.c.Fecha.between(fecha_inicial, fecha_final)) \
        .group_by(c.c.Vendedor, c.c.Ruta, func.year(e.c.Fecha), extract('week', e.c.Fecha)).all()
    return sellers


def query_by_month(fecha_inicial, fecha_final):
    t: Table = t_TOTALDOCUMENTO
    e: Table = t_ENCABEZADOCUMENTO
    c: Table = t_MSOCLIENTES
    session = Session()
    sellers = session.query(
        func.sum(t.c.TotalNeto).label("totalNeto"),
        c.c.Vendedor.label("vendedor"),
        c.c.Ruta.label("ruta"),
        func.year(e.c.Fecha).label("year"),
        extract('month', e.c.Fecha).label("periodo")
    ) \
        .join(e, t.c.Id == e.c.Id).filter(e.c.Vigente == 1) \
        .join(c, e.c.Rut == c.c.Rut and e.c.Codigo == c.c.Codigo) \
        .filter(t.c.TipoId == '06').filter(e.c.Fecha.between(fecha_inicial, fecha_final)) \
        .group_by(c.c.Vendedor, c.c.Ruta, func.year(e.c.Fecha), extract('month', e.c.Fecha)).all()
    return sellers


def query_by_quarter(fecha_inicial, fecha_final):
    t: Table = t_TOTALDOCUMENTO
    e: Table = t_ENCABEZADOCUMENTO
    c: Table = t_MSOCLIENTES
    session = Session()
    sellers = session.query(
        func.sum(t.c.TotalNeto).label("totalNeto"),
        c.c.Vendedor.label("vendedor"),
        c.c.Ruta.label("ruta"),
        func.year(e.c.Fecha).label("year"),
        extract('quarter', e.c.Fecha).label("periodo")
    ) \
        .join(e, t.c.Id == e.c.Id).filter(e.c.Vigente == 1) \
        .join(c, e.c.Rut == c.c.Rut and e.c.Codigo == c.c.Codigo) \
        .filter(t.c.TipoId == '06').filter(e.c.Fecha.between(fecha_inicial, fecha_final)) \
        .group_by(c.c.Vendedor, c.c.Ruta, func.year(e.c.Fecha), extract('quarter', e.c.Fecha)).all()
    return sellers


def query_by_year(fecha_inicial, fecha_final):
    t: Table = t_TOTALDOCUMENTO
    e: Table = t_ENCABEZADOCUMENTO
    c: Table = t_MSOCLIENTES
    session = Session()
    sellers = session.query(
        func.sum(t.c.TotalNeto).label("totalNeto"),
        c.c.Vendedor.label("vendedor"),
        c.c.Ruta.label("ruta"),
        func.year(e.c.Fecha).label("year"),
        func.year(e.c.Fecha).label("year")
    ) \
        .join(e, t.c.Id == e.c.Id).filter(e.c.Vigente == 1) \
        .join(c, e.c.Rut == c.c.Rut and e.c.Codigo == c.c.Codigo) \
        .filter(t.c.TipoId == '06').filter(e.c.Fecha.between(fecha_inicial, fecha_final)) \
        .group_by(c.c.Vendedor, c.c.Ruta, func.year(e.c.Fecha), func.year(e.c.Fecha)).all()
    return sellers


class Vendedor(ObjectType):
    id = graphene.String()
    nombre = graphene.String()


class Ruta(ObjectType):
    id = graphene.String()
    nombre = graphene.String()


class VentaAgrupadaVendedor(ObjectType):
    vendedor = Vendedor
    year = graphene.Int()
    periodo = graphene.String()
    totalNeto = graphene.Float()


class VentaAgrupadaRuta(ObjectType):
    ruta = graphene.String()
    year = graphene.Int()
    periodo = graphene.String()
    totalNeto = graphene.Float()


class Venta(ObjectType):
    vendedor = graphene.String()
    ruta = graphene.String()
    year = graphene.Int()
    periodo = graphene.String()
    totalNeto = graphene.Float()


class QueryVendedores(ObjectType):
    vendedores = graphene.List(Vendedor, id=graphene.String(), nombre=graphene.String())

    @staticmethod
    def resolve_vendedores(self, info, id=None, nombre=None):
        result = [];
        t = t_MSOVENDEDOR
        session = Session()
        vendedores = session.query(t).filter(t.c.comision == 3).values(t.c.codigo.label('id'),
                                                                       t.c.nombre.label('nombre'))
        for vendedor in vendedores:
            result.append({'id': vendedor.id, 'nombre': vendedor.nombre})

        return result


class QueryRutas(ObjectType):
    rutas = graphene.List(Ruta, id=graphene.String(), nombre=graphene.String())

    @staticmethod
    def resolve_rutas(parent, info, id=None, nombre=None):
        result = []
        t = t_MSOSTTABLAS

        session = Session()
        rutas = session.query(t).filter(t.columns.tabla == "017").values(t.c.codigo.label('id'),
                                                                         t.c.descripcion.label('nombre'))
        for ruta in rutas:
            result.append({'id': ruta.id, 'nombre': ruta.nombre})

        return result


def arreglo_resultados(ventas):
    records = []
    for s in ventas:
        records.append(
            {'vendedor': s.vendedor, 'ruta': s.ruta, 'year': s.year, 'periodo': s.periodo, 'totalNeto': s.totalNeto})

    return records


class QueryVentas(ObjectType):
    ventas_vendedor_dia = graphene.List(Venta, desde=graphene.Date(), hasta=graphene.Date())

    @staticmethod
    def resolve_ventas_vendedor_dia(parent, info, desde=graphene.Date(required=True),
                                    hasta=graphene.Date(required=True)):
        ventas = query_by_day(desde, hasta)
        return arreglo_resultados(ventas)

    ventas_vendedor_semana = graphene.List(Venta, desde=graphene.Date(), hasta=graphene.Date())

    @staticmethod
    def resolve_ventas_vendedor_semana(parent, info, desde=graphene.Date(required=True),
                                       hasta=graphene.Date(required=True)):
        ventas = query_by_week(desde, hasta)
        return arreglo_resultados(ventas)

    ventas_vendedor_mes = graphene.List(Venta, desde=graphene.Date(), hasta=graphene.Date())

    @staticmethod
    def resolve_ventas_vendedor_mes(parent, info, desde=graphene.Date(required=True),
                                    hasta=graphene.Date(required=True)):
        ventas = query_by_month(desde, hasta)
        return arreglo_resultados(ventas)

    ventas_vendedor_trimestre = graphene.List(Venta, desde=graphene.Date(), hasta=graphene.Date())

    @staticmethod
    def resolve_ventas_vendedor_trimestre(parent, info, desde=graphene.Date(required=True),
                                          hasta=graphene.Date(required=True)):
        ventas = query_by_quarter(desde, hasta)
        return arreglo_resultados(ventas)

    ventas_vendedor_anno = graphene.List(Venta, desde=graphene.Date(), hasta=graphene.Date())

    @staticmethod
    def resolve_ventas_vendedor_anno(parent, info, desde=graphene.Date(required=True),
                                     hasta=graphene.Date(required=True)):
        ventas = query_by_year(desde, hasta)
        return arreglo_resultados(ventas)

    ventas_ruta_dia = graphene.List(Venta, desde=graphene.Date(), hasta=graphene.Date())

    @staticmethod
    def resolve_ventas_ruta_dia(parent, info, desde=graphene.Date(required=True), hasta=graphene.Date(required=True)):
        ventas = query_by_day(desde, hasta)
        return arreglo_resultados(ventas)

    ventas_ruta_semana = graphene.List(Venta, desde=graphene.Date(), hasta=graphene.Date())

    @staticmethod
    def resolve_ventas_ruta_semana(parent, info, desde=graphene.Date(required=True),
                                   hasta=graphene.Date(required=True)):
        ventas = query_by_week(desde, hasta)
        return arreglo_resultados(ventas)

    ventas_ruta_mes = graphene.List(Venta, desde=graphene.Date(), hasta=graphene.Date())

    @staticmethod
    def resolve_ventas_ruta_mes(parent, info, desde=graphene.Date(required=True), hasta=graphene.Date(required=True)):
        ventas = query_by_month(desde, hasta)
        return arreglo_resultados(ventas)

    ventas_ruta_trimestre = graphene.List(Venta, desde=graphene.Date(), hasta=graphene.Date())

    @staticmethod
    def resolve_ventas_ruta_trimestre(parent, info, desde=graphene.Date(required=True),
                                      hasta=graphene.Date(required=True)):
        ventas = query_by_quarter(desde, hasta)
        return arreglo_resultados(ventas)

    ventas_ruta_anno = graphene.List(Venta, desde=graphene.Date(), hasta=graphene.Date())

    @staticmethod
    def resolve_ventas_ruta_anno(parent, info, desde=graphene.Date(required=True), hasta=graphene.Date(required=True)):
        ventas = query_by_year(desde, hasta)
        return arreglo_resultados(ventas)
