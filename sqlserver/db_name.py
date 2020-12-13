# coding: utf-8
from sqlalchemy import BINARY, BigInteger, CHAR, Column, DateTime, Float, ForeignKey, Index, Integer, LargeBinary, MetaData, NCHAR, Numeric, SmallInteger, String, TEXT, Table, text
from sqlalchemy.dialects.mssql import BIT, IMAGE, MONEY, SMALLMONEY, TINYINT, UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

t_ALTERNATIVO = Table(
    'ALTERNATIVO', metadata,
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Alternativo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', Integer, index=True, server_default=text("((0))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'Articulo', 'Atributo', 'Especificacion', 'Alternativo', unique=True)
)


t_ARTICULO = Table(
    'ARTICULO', metadata,
    Column('MonedaImportado', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ConversionVolumen', Float(53), server_default=text("((0))")),
    Column('Moneda', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CtaResultado', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Kit', String(1, 'Modern_Spanish_CI_AS'), server_default=text("('N')")),
    Column('CostoCentro', String(4, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CostoCuenta', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Importado', BIT, server_default=text("((0))")),
    Column('Auxiliar', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CentroCosto', String(4, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PorcCarne', Float(53), server_default=text("((0))")),
    Column('ImpuestoEspecifico', SMALLMONEY, server_default=text("((0))")),
    Column('CostoItem', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Activo', String(1, 'Modern_Spanish_CI_AS'), server_default=text("('S')")),
    Column('Ar_NoFacturable', BIT, server_default=text("((0))")),
    Column('ItemGasto', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Familia', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('StockReal', MONEY, server_default=text("((0))")),
    Column('PorcIla', Float(53), server_default=text("((0))")),
    Column('Costo', MONEY, server_default=text("((0))")),
    Column('CostoEconomico', MONEY, server_default=text("((0))")),
    Column('VentaNeto', MONEY, server_default=text("((0))")),
    Column('VentaBruto', MONEY, server_default=text("((0))")),
    Column('Inicio', DateTime, server_default=text("(space((0)))")),
    Column('CostoAuxiliar', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Imagen', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('DescuentoPromocional', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ganado', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('DescuentoInicio', DateTime, server_default=text("(space((0)))")),
    Column('Comision', SMALLMONEY, server_default=text("((0))")),
    Column('Rut_Proveedor', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('DescuentoFinal', DateTime, server_default=text("(space((0)))")),
    Column('Ubicacion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CodigoIla', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('StockMinimo', Float(53), server_default=text("((0))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), unique=True, server_default=text("(space((0)))")),
    Column('Descripcion', String(40, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Nivel', String(3, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Unidad', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('ARTICULO03', 'Familia', 'Articulo')
)


t_ARTICULOSNUMERADOS = Table(
    'ARTICULOSNUMERADOS', metadata,
    Column('articulo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("('')"))
)


t_ARTXLOCAL = Table(
    'ARTXLOCAL', metadata,
    Column('Fecha', DateTime, server_default=text("(space((0)))")),
    Column('Kardex', Integer, server_default=text("((0))")),
    Column('StockInicial', MONEY, server_default=text("((0))")),
    Column('Stock', MONEY, server_default=text("((0))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('StockCalculo', MONEY, server_default=text("((0))")),
    Column('Salida', DateTime, server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('ARTXLOCAL01', 'Articulo', 'Atributo', 'Especificacion'),
    Index('PKPrimaryKey', 'Local', 'Articulo', 'Atributo', 'Especificacion', unique=True)
)


t_ARTXLOCALLINEA = Table(
    'ARTXLOCALLINEA', metadata,
    Column('Stockinicial', Integer, server_default=text("((0))")),
    Column('Stock', Integer, server_default=text("((0))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Iden', String(8, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_ATRIBUTO = Table(
    'ATRIBUTO', metadata,
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'Articulo', 'Atributo', unique=True)
)


t_BITACORA = Table(
    'BITACORA', metadata,
    Column('Numero', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fecha', DateTime, server_default=text("(space((0)))")),
    Column('Hora', DateTime, server_default=text("(space((0)))")),
    Column('Sistema', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Descripcion', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Formulario', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Clave', String(70, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tabla', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Criterio', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Computador', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('FechaMOv', DateTime, server_default=text("(space((0)))"))
)


t_CARTOLA = Table(
    'CARTOLA', metadata,
    Column('Tipo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Origen', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Destino', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Entrada', MONEY, server_default=text("((0))")),
    Column('Referencia', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('StockInicial', MONEY, server_default=text("((0))")),
    Column('Fecha', DateTime),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Salida', MONEY, server_default=text("((0))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Iden', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_CARTOLAVALORIZADA = Table(
    'CARTOLAVALORIZADA', metadata,
    Column('SaldoDH', MONEY, server_default=text("((0))")),
    Column('Haber', MONEY, server_default=text("((0))")),
    Column('Debe', MONEY, server_default=text("((0))")),
    Column('StockInicial', MONEY, server_default=text("((0))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PrecioUnCompra', MONEY, server_default=text("((0))")),
    Column('Iden', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Costo', MONEY, server_default=text("((0))")),
    Column('Origen', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Destino', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Entrada', MONEY, server_default=text("((0))")),
    Column('Salida', MONEY, server_default=text("((0))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fecha', DateTime),
    Column('Referencia', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('Iden', 'Iden', 'Id', 'Linea', 'Tipo', 'Numero')
)


t_CODIGOBARRAART = Table(
    'CODIGOBARRAART', metadata,
    Column('Velocidad', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Secuencia', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Impresora', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Puerto', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Temperatura', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Retardo', MONEY, server_default=text("((0))")),
    Column('Linea', String(60, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Descripcion', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_CONDUCCION = Table(
    'CONDUCCION', metadata,
    Column('codigo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("('')")),
    Column('ruta', String(50, 'Modern_Spanish_CI_AS'), server_default=text("('')")),
    Column('precio', Integer, server_default=text("((0))")),
    Column('articulo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("('')"))
)


t_CORRELATIVONUMERADOS = Table(
    'CORRELATIVONUMERADOS', metadata,
    Column('Id', Integer, server_default=text("((0))")),
    Column('correlativo', Integer, server_default=text("((0))"))
)


t_CPOABONOS = Table(
    'CPOABONOS', metadata,
    Column('cargomon', MONEY, server_default=text("((0))")),
    Column('codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('numero', String(9, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('correlativo', SmallInteger, server_default=text("((0))")),
    Column('cargo', MONEY, server_default=text("((0))")),
    Column('abono', MONEY, server_default=text("((0))")),
    Column('cancela', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('AbonoTotal', BIT, server_default=text("((0))")),
    Column('abonomon', MONEY, server_default=text("((0))")),
    Column('rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cargo1', MONEY, server_default=text("((0))"))
)


t_CPOARCHIVOPLANO = Table(
    'CPOARCHIVOPLANO', metadata,
    Column('BANCO', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('LINEA', String(4, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TABLA', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CAMPO', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TIPO', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('LARGO', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('INICIO', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CABECERA', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'BANCO', 'LINEA', unique=True)
)


t_CPOCLA = Table(
    'CPOCLA', metadata,
    Column('clave2', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cantidadfilas', Integer, server_default=text("((0))")),
    Column('atributo4', BIT, server_default=text("((0))")),
    Column('atributo3', BIT, server_default=text("((0))")),
    Column('atributo2', BIT, server_default=text("((0))")),
    Column('atributo1', BIT, server_default=text("((0))")),
    Column('password', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave3', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave1', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('atributo5', BIT, server_default=text("((0))")),
    Column('clave5', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave4', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MargenIzquierdo', TINYINT, server_default=text("((0))")),
    Column('usuario', String(40, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))"))
)


t_CPODOCTO = Table(
    'CPODOCTO', metadata,
    Column('Valor_Ilamon', MONEY, server_default=text("((0))")),
    Column('Retencion', Float(53), server_default=text("((0))")),
    Column('cancela', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('emitido', BIT, server_default=text("((0))")),
    Column('fueraPlazo', BIT, server_default=text("((0))")),
    Column('FechaC', DateTime),
    Column('FechaR', DateTime),
    Column('FechaD', DateTime),
    Column('Valor_brutomon', MONEY, server_default=text("((0))")),
    Column('Valor_Importacion', MONEY, server_default=text("((0))")),
    Column('Valor_NetoMon', MONEY, server_default=text("((0))")),
    Column('valor_abono', MONEY, server_default=text("((0))")),
    Column('Valor_ivamon', MONEY, server_default=text("((0))")),
    Column('Valor_abonoMon', MONEY, server_default=text("((0))")),
    Column('ImpuestoespMon', MONEY, server_default=text("((0))")),
    Column('Moneda', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Paridad', MONEY, server_default=text("((0))")),
    Column('Retencionmon', MONEY, server_default=text("((0))")),
    Column('Rut_Provee', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Valor_ExentoMon', MONEY, server_default=text("((0))")),
    Column('estado', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Correlativo', SmallInteger, server_default=text("((0))")),
    Column('codigo_Provee', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Glosa', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fecha_ingreso', DateTime),
    Column('fecha_vencimiento', DateTime),
    Column('fecha_inicial', DateTime),
    Column('Mesdeclaracion', String(6, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Valor_ImportacionMon', MONEY, server_default=text("((0))")),
    Column('banco', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('LitrosComb', Float(53), server_default=text("((0))")),
    Column('vigencia', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cambio', DateTime),
    Column('valor_bruto', MONEY, server_default=text("((0))")),
    Column('valor_exento', MONEY, server_default=text("((0))")),
    Column('valor_neto', MONEY, server_default=text("((0))")),
    Column('valor_ila', MONEY, server_default=text("((0))")),
    Column('valor_iva', MONEY, server_default=text("((0))")),
    Column('ImpuestoEsp', MONEY, server_default=text("((0))")),
    Column('CentroCosto', String(4, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Valor_IvaImportacion', MONEY, server_default=text("((0))")),
    Column('TipoFactura', String(4, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Porc_Rete', TINYINT, server_default=text("((0))")),
    Column('Valor_IvaImportacionMon', MONEY, server_default=text("((0))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(9, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Folio', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('cpodocto01', 'Tipo', 'Folio', 'Numero', 'Correlativo'),
    Index('PKPrimaryKey', 'Rut_Provee', 'codigo_Provee', 'Tipo', 'Numero', 'Correlativo', unique=True),
    Index('Cpodocto02', 'Rut_Provee', 'codigo_Provee', 'Tipo', 'Folio', 'Numero', 'Correlativo')
)


t_CPONOMINAPAGO = Table(
    'CPONOMINAPAGO', metadata,
    Column('ValorPago', MONEY, server_default=text("((0))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ValorAbono', MONEY, server_default=text("((0))")),
    Column('Pago', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Razon', String(60, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Vence', DateTime),
    Column('Emision', DateTime),
    Column('Glosa', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Sucursal', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ValorBruto', MONEY, server_default=text("((0))")),
    Column('ValorIva', MONEY, server_default=text("((0))")),
    Column('ValorNeto', MONEY, server_default=text("((0))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('FechaPago', DateTime),
    Column('Comentario', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Banco', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Egreso', String(6, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))"))
)


t_CPOROTULO = Table(
    'CPOROTULO', metadata,
    Column('Cancelacion', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('yearSgte', SmallInteger, server_default=text("((1990))")),
    Column('MSArturo', String(18, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('FacturaImportacion', BIT, server_default=text("((0))")),
    Column('MonedaTrabajo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MonedaAlternativa', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MonedaLocal', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('DobleMoneda', BIT, server_default=text("((0))")),
    Column('Retencion', TINYINT, server_default=text("((0))")),
    Column('nombre1', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ConeccionContabilidad', BIT, server_default=text("((0))")),
    Column('nombre2', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PathDos', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ConectaCompVtas', BIT, server_default=text("((0))")),
    Column('ILA', BIT, server_default=text("((0))")),
    Column('FoliosInternos', BIT, server_default=text("((0))")),
    Column('ImpuestoEspecifico', MONEY, server_default=text("((0))")),
    Column('ImpEspecifico', BIT, server_default=text("((0))")),
    Column('EmpresaConstructora', BIT, server_default=text("((0))")),
    Column('tipoCuenta', BIT, server_default=text("((1))")),
    Column('valorIVA', SMALLMONEY, server_default=text("((0))")),
    Column('folioUnico', BIT, server_default=text("((1))")),
    Column('comuna', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('titulo1', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fechadeldia', DateTime, server_default=text("(space((0)))")),
    Column('titulocon', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nombrecon', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('titulogg', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nombregg', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fechaver', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('version', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nomrepleg', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('titulo2', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ciudad', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PorcCarnes', SMALLMONEY, server_default=text("((0))")),
    Column('direccion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('rutemp', String(14, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('giro', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('sigla', String(25, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('empresa', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('serie', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CvtCtaCarnes', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((8)))")),
    Column('yearProceso', SmallInteger, server_default=text("((1990))")),
    Column('yearActual', SmallInteger, server_default=text("((1990))")),
    Column('ImpuestoCarnes', BIT, server_default=text("((0))")),
    Column('rutrepleg', String(14, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TempField0', BIT, server_default=text("((0))"))
)


t_CTAABONOS = Table(
    'CTAABONOS', metadata,
    Column('Tipo1', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cancela', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('saldo', MONEY, server_default=text("((0))")),
    Column('saldomon', MONEY, server_default=text("((0))")),
    Column('abono', MONEY, server_default=text("((0))")),
    Column('abonomon', MONEY, server_default=text("((0))")),
    Column('cargo', MONEY, server_default=text("((0))")),
    Column('cargomon', MONEY, server_default=text("((0))")),
    Column('correlativo', SmallInteger, server_default=text("((0))")),
    Column('numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigo', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('AbonoTotal', BIT, server_default=text("((0))")),
    Column('rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_CTABOLETIN = Table(
    'CTABOLETIN', metadata,
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Monto', MONEY, server_default=text("((0))")),
    Column('Fecha', DateTime, server_default=text("(space((0)))")),
    Column('Boletin', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipo', String(4, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Situacion', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Carpeta', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'Carpeta', 'Linea', unique=True)
)


t_CTACLA = Table(
    'CTACLA', metadata,
    Column('usuario', String(40, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('password', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave1', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave2', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave3', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave4', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('atributo1', BIT, server_default=text("((0))")),
    Column('atributo2', BIT, server_default=text("((0))")),
    Column('atributo3', BIT, server_default=text("((0))")),
    Column('atributo4', BIT, server_default=text("((0))")),
    Column('cantidadfilas', Integer, server_default=text("((0))")),
    Column('MargenIzquierdo', TINYINT, server_default=text("((0))"))
)


t_CTACREDITO = Table(
    'CTACREDITO', metadata,
    Column('MasDatos', TEXT(2147483647, 'Modern_Spanish_CI_AS'), server_default=text("(space((1)))")),
    Column('fecha', DateTime, server_default=text("(space((0)))")),
    Column('NotasPedido', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Observacion3', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Observacion2', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Compra', MONEY, server_default=text("((0))")),
    Column('Vendedor', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Observacion1', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Razon', String(60, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Condicion', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fax', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('RepLegal', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fonos', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Comite', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Carpeta', String(8, 'Modern_Spanish_CI_AS'), unique=True, server_default=text("(space((0)))"))
)


t_CTADOCTO = Table(
    'CTADOCTO', metadata,
    Column('FechaR', DateTime, server_default=text("(space((0)))")),
    Column('FechaP', DateTime, server_default=text("(space((0)))")),
    Column('FechaC', DateTime, server_default=text("(space((0)))")),
    Column('fueraPlazo', BIT, server_default=text("((0))")),
    Column('valor_abono', MONEY, server_default=text("((0))")),
    Column('vigente', BIT, server_default=text("((1))")),
    Column('Recuperacion', MONEY, server_default=text("((0))")),
    Column('deuda_directa', BIT, server_default=text("((0))")),
    Column('glosa_directa', String(25, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cancela', String(8, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('FechaE', DateTime, server_default=text("(space((0)))")),
    Column('Valor_NetoMOn', MONEY, server_default=text("((0))")),
    Column('PorcRecuperacion', SMALLMONEY, server_default=text("((0))")),
    Column('comision', SMALLMONEY, server_default=text("((0))")),
    Column('emitido', BIT, server_default=text("((0))")),
    Column('Valor_IvaMon', MONEY, server_default=text("((0))")),
    Column('TIPO1', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('valor_iva', MONEY, server_default=text("((0))")),
    Column('ImpuestoEspecificoMon', MONEY, server_default=text("((0))")),
    Column('Caja', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Paridad', MONEY, server_default=text("((0))")),
    Column('Valor_BrutoMon', MONEY, server_default=text("((0))")),
    Column('Valor_AbonoMon', MONEY, server_default=text("((0))")),
    Column('FechaD', DateTime, server_default=text("(space((0)))")),
    Column('Valor_IlaMon', MONEY, server_default=text("((0))")),
    Column('Valor_ExentoMOn', MONEY, server_default=text("((0))")),
    Column('RecuperacionMon', MONEY, server_default=text("((0))")),
    Column('ImpuestoEspecifico', MONEY, server_default=text("((0))")),
    Column('LitrosCombustible', Float(53), server_default=text("((0))")),
    Column('cambio', DateTime, server_default=text("(space((0)))")),
    Column('Moneda', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ciudad', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('valor_ila', MONEY, server_default=text("((0))")),
    Column('boleta_hasta', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Rut_cliente', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigo_cliente', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fecha_ingreso', DateTime, server_default=text("(space((0)))")),
    Column('fecha_vencimiento', DateTime, server_default=text("(space((0)))")),
    Column('fecha_inicial', DateTime, server_default=text("(space((0)))")),
    Column('vendedor', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cobrador', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('local_venta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('NroCtaCte', String(25, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('banco', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('glosa', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('estado', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('vigencia', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cartola', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('rut_endoso', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigo_endoso', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nombre_endoso', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('valor_bruto', MONEY, server_default=text("((0))")),
    Column('valor_exento', MONEY, server_default=text("((0))")),
    Column('valor_neto', MONEY, server_default=text("((0))")),
    Column('plaza', BIT, server_default=text("((1))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Correlativo', SmallInteger, server_default=text("((0))")),
    Column('TipoSII', Integer),
    Index('CTADOCTO01', 'Rut_cliente', 'codigo_cliente', 'cartola', 'fecha_ingreso'),
    Index('PKPrimaryKey', 'Tipo', 'Numero', 'Correlativo', 'TIPO1', unique=True)
)


t_CTAROTULO = Table(
    'CTAROTULO', metadata,
    Column('ImpEspecifico', BIT, server_default=text("((0))")),
    Column('valorIVA', SMALLMONEY, server_default=text("((0))")),
    Column('EmpresaConstructora', BIT, server_default=text("((0))")),
    Column('ILA', BIT, server_default=text("((0))")),
    Column('ConectaCompVtas', BIT, server_default=text("((0))")),
    Column('Cancelacion', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ConeccionContabilidad', BIT, server_default=text("((0))")),
    Column('yearActual', SmallInteger, server_default=text("((1990))")),
    Column('ImpuestoEspecifico', MONEY, server_default=text("((0))")),
    Column('yearProceso', SmallInteger, server_default=text("((1990))")),
    Column('yearSgte', SmallInteger, server_default=text("((1990))")),
    Column('nombre1', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('FoliosInternos', BIT, server_default=text("((0))")),
    Column('folioUnico', BIT, server_default=text("((1))")),
    Column('PathDos', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Doblemoneda', BIT, server_default=text("((0))")),
    Column('MonedaLocal', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MonedaTrabajo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MonedaAlternativa', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('titulo2', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('serie', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('tipoCuenta', BIT, server_default=text("((0))")),
    Column('sigla', String(25, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CvtCtaCarnes', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((8)))")),
    Column('ImpuestoCarnes', BIT, server_default=text("((0))")),
    Column('nombre2', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MSArturo', String(18, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PorcCarnes', SMALLMONEY, server_default=text("((0))")),
    Column('empresa', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('giro', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('rutemp', String(14, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('direccion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('comuna', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ciudad', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nombrecon', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fechadeldia', DateTime, server_default=text("(space((0)))")),
    Column('titulo1', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('rutrepleg', String(14, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('titulocon', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('titulogg', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nombregg', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fechaver', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('version', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nomrepleg', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_DATOSCLIENTE = Table(
    'DATOSCLIENTE', metadata,
    Column('Despacho', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CondicionVenta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Dias', SmallInteger, server_default=text("((0))")),
    Column('Ruta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Lista', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoVenta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ciudad', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Giro', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Razon', String(60, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Direccion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Comuna', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Telefono', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ComisionCobrador', MONEY, server_default=text("((0))")),
    Column('Transporte', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ComisionVendedor', MONEY, server_default=text("((0))")),
    Column('Vendedor', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('tipoid', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cobrador', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'Id', 'tipoid', unique=True)
)


t_DESCUENTORECARGO = Table(
    'DESCUENTORECARGO', metadata,
    Column('MontoMon', MONEY, server_default=text("((0))")),
    Column('Tipo', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Valor', MONEY, server_default=text("((0))")),
    Column('tipoid', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ValorMOn', MONEY, server_default=text("((0))")),
    Column('Monto', MONEY, server_default=text("((0))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('DESCUENTORECARGO01', 'tipoid', 'Id'),
    Index('PKPrimaryKey', 'Id', 'Linea', unique=True)
)


t_DETALLEDOCUMENTO = Table(
    'DETALLEDOCUMENTO', metadata,
    Column('Pedido', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cantidad', MONEY, server_default=text("((0))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TotalLinea', MONEY, server_default=text("((0))")),
    Column('PrecioVentaMon', MONEY, server_default=text("((0))")),
    Column('PrecioCostoMOn', MONEY, server_default=text("((0))")),
    Column('Variacion', MONEY, server_default=text("((0))")),
    Column('TotalLineaMOn', MONEY, server_default=text("((0))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PrecioCosto', MONEY, server_default=text("((0))")),
    Column('ParidadMOn', MONEY, server_default=text("((0))")),
    Column('PrecioVenta', MONEY, server_default=text("((0))")),
    Column('Paridad', MONEY, server_default=text("((0))")),
    Column('Subpedido', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Indiceoc', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('DatosKit', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Alternativo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Caja', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CompletoIncompleto', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipoid', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Descripcion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('DETALLEDOCUMENTO01', 'Tipoid', 'Id'),
    Index('PKPrimaryKey', 'Id', 'Linea', unique=True),
    Index('DETALLEDOCUMENTO05', 'Local', 'Articulo', 'Atributo', 'Especificacion'),
    Index('DETALLEDOCUMENTO02', 'Pedido', 'Articulo', 'Atributo', 'Especificacion')
)


t_ENCABEZADOCUMENTO = Table(
    'ENCABEZADOCUMENTO', metadata,
    Column('FueraPlazo', BIT, server_default=text("((0))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('LocalDes', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fecha', DateTime, server_default=text("(space((0)))")),
    Column('Vence', DateTime, server_default=text("(space((0)))")),
    Column('Pedido', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('OrdenCompra', String(11, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Factura', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('AfectoExento', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Comentario', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TIPO1', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('NetooBruto', BIT, server_default=text("((1))")),
    Column('FacFlete', Integer, server_default=text("((0))")),
    Column('Caja', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Transporte', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('VenceOC', DateTime, server_default=text("(space((0)))")),
    Column('DoctoMinera', BIT, server_default=text("((0))")),
    Column('traspasado', BIT, server_default=text("((0))")),
    Column('Impreso', BIT, server_default=text("((0))")),
    Column('Subpedido', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoRelacionador', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CompletoIncompleto', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoMoneda', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('FacturaAnticipo', String(1, 'Modern_Spanish_CI_AS'), server_default=text("('N')")),
    Column('Facturado', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Emitido', BIT, server_default=text("((0))")),
    Column('Vigente', BIT, server_default=text("((1))")),
    Column('NumeroRelacionador', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Mov', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), unique=True, server_default=text("(space((0)))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fec_Carga', DateTime, server_default=text("(space((0)))")),
    Column('Foliocarga', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fec_Anula', DateTime, server_default=text("(space((0)))")),
    Column('Publicado', BIT, nullable=False, server_default=text("((0))")),
    Column('PublicadoNro', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoSII', Integer),
    Index('ENCABEZADOCUMENTO01', 'Tipo', 'Numero'),
    Index('encabezadocumento02', 'Rut', 'Codigo', 'Fecha')
)


t_EOS_DETALLE = Table(
    'EOS_DETALLE', metadata,
    Column('correlativo', BigInteger, primary_key=True, nullable=False),
    Column('articulo', String(50, 'Modern_Spanish_CI_AS'), primary_key=True, nullable=False),
    Column('ncorrelativo', Integer),
    Column('cantidad', MONEY),
    Column('neto', MONEY),
    Column('descuento', MONEY),
    Column('ila', MONEY),
    Column('carne', MONEY),
    Column('iva', MONEY),
    Column('precio', MONEY),
    Column('numero', Integer),
    Column('esnumerado', BIT)
)


t_EOS_ENCABEZADO = Table(
    'EOS_ENCABEZADO', metadata,
    Column('correalitvo', UNIQUEIDENTIFIER, primary_key=True),
    Column('rut', String(10, 'Modern_Spanish_CI_AS')),
    Column('code', String(50, 'Modern_Spanish_CI_AS')),
    Column('fecha', DateTime),
    Column('neto', MONEY),
    Column('valoriva', MONEY),
    Column('valorila', MONEY),
    Column('valorporcarne', MONEY)
)


t_EOS_REGISTROS = Table(
    'EOS_REGISTROS', metadata,
    Column('indice', BigInteger, primary_key=True),
    Column('rut', String(10, 'Modern_Spanish_CI_AS'), nullable=False),
    Column('codigo', String(19, 'Modern_Spanish_CI_AS'), nullable=False),
    Column('vendedor', String(10, 'Modern_Spanish_CI_AS'), nullable=False),
    Column('fila', Integer, nullable=False),
    Column('fecha', DateTime, nullable=False),
    Column('articulo', String(10, 'Modern_Spanish_CI_AS')),
    Column('cantidad', SMALLMONEY),
    Column('neto', SMALLMONEY),
    Column('descuento', SMALLMONEY),
    Column('codigoila', String(3, 'Modern_Spanish_CI_AS'), nullable=False),
    Column('ila', SMALLMONEY),
    Column('carne', SMALLMONEY),
    Column('iva', SMALLMONEY),
    Column('precio', SMALLMONEY),
    Column('numeros', String(512, 'Modern_Spanish_CI_AS')),
    Column('correlativos', String(512, 'Modern_Spanish_CI_AS')),
    Column('pesos', String(1024, 'Modern_Spanish_CI_AS')),
    Column('esnumerado', BIT),
    Column('totalila', SMALLMONEY),
    Column('sobrestock', BIT)
)


t_EOS_USUARIOS = Table(
    'EOS_USUARIOS', metadata,
    Column('rut', String(10, 'Modern_Spanish_CI_AS'), primary_key=True),
    Column('password', LargeBinary),
    Column('lastlogin', DateTime)
)


t_ESPECIALES = Table(
    'ESPECIALES', metadata,
    Column('id', Numeric(18, 0), nullable=False),
    Column('productoinicio', String(50, 'Modern_Spanish_CI_AS'), nullable=False),
    Column('productofinal', String(50, 'Modern_Spanish_CI_AS'), nullable=False)
)


t_EosTest = Table(
    'EosTest', metadata,
    Column('id', Numeric(18, 0), nullable=False),
    Column('name', NCHAR(50))
)


t_FACELECTERR = Table(
    'FACELECTERR', metadata,
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fecha', DateTime),
    Column('Comentario', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Error', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_FACTURACION = Table(
    'FACTURACION', metadata,
    Column('Iden', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('NetooBruto', BIT, server_default=text("((1))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TIPO1', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Pedido', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('Iden', 'Rut', 'Codigo', 'Local', 'Pedido', 'Iden')
)


t_FACTURACIONDES = Table(
    'FACTURACIONDES', metadata,
    Column('Iden', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipo', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Monto', MONEY, server_default=text("((0))")),
    Column('Valor', MONEY, server_default=text("((0))"))
)


t_FOLIOS = Table(
    'FOLIOS', metadata,
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TIPO1', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'Tipo', 'Numero', 'TIPO1', unique=True)
)


t_FORMATO = Table(
    'FORMATO', metadata,
    Column('Sensor', BIT, server_default=text("((0))")),
    Column('Lineas', SmallInteger, server_default=text("((0))")),
    Column('SeparacionLineas', SMALLMONEY, server_default=text("((0))")),
    Column('FormularioContinuo', BIT, server_default=text("((0))")),
    Column('Cantidad', Integer, server_default=text("((0))")),
    Column('Impresora', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoFecha', TINYINT, server_default=text("((0))")),
    Column('AnchoDoc', SMALLMONEY, server_default=text("((0))")),
    Column('MM2año', SMALLMONEY, server_default=text("((0))")),
    Column('Largo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MM2dia', SMALLMONEY, server_default=text("((0))")),
    Column('LargoDoc', SMALLMONEY, server_default=text("((0))")),
    Column('Separacion', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Decimal', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Matriz', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Letra', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('SeparacionTallas', SMALLMONEY, server_default=text("((0))")),
    Column('Imprimir', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Mm2', SMALLMONEY, server_default=text("((0))")),
    Column('Mm1', SMALLMONEY, server_default=text("((0))")),
    Column('Texto', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Nombre', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fecha', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MM2mes', SMALLMONEY, server_default=text("((0))")),
    Column('Ancho', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ila1', SMALLMONEY, server_default=text("((0))")),
    Column('Ila15', SMALLMONEY, server_default=text("((0))")),
    Column('Ila14', SMALLMONEY, server_default=text("((0))")),
    Column('Ila13', SMALLMONEY, server_default=text("((0))")),
    Column('Ila12', SMALLMONEY, server_default=text("((0))")),
    Column('Ila11', SMALLMONEY, server_default=text("((0))")),
    Column('Ila10', SMALLMONEY, server_default=text("((0))")),
    Column('ImprimeDescripcion', BIT, server_default=text("((0))")),
    Column('Ila2', SMALLMONEY, server_default=text("((0))")),
    Column('Ila8', SMALLMONEY, server_default=text("((0))")),
    Column('Ila7', SMALLMONEY, server_default=text("((0))")),
    Column('Ila6', SMALLMONEY, server_default=text("((0))")),
    Column('Ila5', SMALLMONEY, server_default=text("((0))")),
    Column('Ila4', SMALLMONEY, server_default=text("((0))")),
    Column('Ila3', SMALLMONEY, server_default=text("((0))")),
    Column('Ila9', SMALLMONEY, server_default=text("((0))"))
)


t_GEVCLA = Table(
    'GEVCLA', metadata,
    Column('usuario', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('password', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave1', String(50, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('clave2', String(50, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('clave3', String(50, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('clave4', String(50, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('clave5', String(50, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('cantidadfilas', Integer, server_default=text("((0))")),
    Column('MargenIzquierdo', TINYINT, server_default=text("((0))")),
    Column('Atributo1', BIT, server_default=text("((0))"))
)


t_GEVROTULO = Table(
    'GEVROTULO', metadata,
    Column('ConeccionContabilidad', BIT, server_default=text("((0))")),
    Column('fechadeldia', DateTime, server_default=text("(space((0)))")),
    Column('serie', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ConeccionCambiaCuentas', BIT, server_default=text("((0))")),
    Column('CvtCtaCarnes', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((8)))")),
    Column('MSArturo', String(18, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('RefundeGuias', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_HCTADOCTO = Table(
    'HCTADOCTO', metadata,
    Column('FechaD', DateTime, server_default=text("(space((0)))")),
    Column('Recuperacion', MONEY, server_default=text("((0))")),
    Column('FechaC', DateTime, server_default=text("(space((0)))")),
    Column('FechaR', DateTime, server_default=text("(space((0)))")),
    Column('FechaP', DateTime, server_default=text("(space((0)))")),
    Column('FechaE', DateTime, server_default=text("(space((0)))")),
    Column('glosa_directa', String(25, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fueraPlazo', BIT, server_default=text("((0))")),
    Column('comision', SMALLMONEY, server_default=text("((0))")),
    Column('emitido', BIT, server_default=text("((0))")),
    Column('PorcRecuperacion', SMALLMONEY, server_default=text("((0))")),
    Column('cambio', DateTime, server_default=text("(space((0)))")),
    Column('Caja', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('vigente', BIT, server_default=text("((1))")),
    Column('LitrosCombustible', Float(53), server_default=text("((0))")),
    Column('ImpuestoEspecifico', MONEY, server_default=text("((0))")),
    Column('Valor_BrutoMon', MONEY, server_default=text("((0))")),
    Column('Valor_ExentoMOn', MONEY, server_default=text("((0))")),
    Column('Valor_NetoMOn', MONEY, server_default=text("((0))")),
    Column('Valor_IlaMon', MONEY, server_default=text("((0))")),
    Column('Valor_IvaMon', MONEY, server_default=text("((0))")),
    Column('Valor_AbonoMon', MONEY, server_default=text("((0))")),
    Column('ImpuestoEspecificoMon', MONEY, server_default=text("((0))")),
    Column('fecha_ingreso', DateTime, server_default=text("(space((0)))")),
    Column('Paridad', MONEY, server_default=text("((0))")),
    Column('Moneda', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TIPO1', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('deuda_directa', BIT, server_default=text("((0))")),
    Column('RecuperacionMon', MONEY, server_default=text("((0))")),
    Column('banco', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fecha_inicial', DateTime, server_default=text("(space((0)))")),
    Column('NroCtaCte', String(25, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cancela', String(8, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('boleta_hasta', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Rut_cliente', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigo_cliente', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fecha_vencimiento', DateTime, server_default=text("(space((0)))")),
    Column('vendedor', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cobrador', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('plaza', BIT, server_default=text("((1))")),
    Column('ciudad', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('glosa', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('valor_bruto', MONEY, server_default=text("((0))")),
    Column('valor_abono', MONEY, server_default=text("((0))")),
    Column('valor_iva', MONEY, server_default=text("((0))")),
    Column('valor_ila', MONEY, server_default=text("((0))")),
    Column('local_venta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('valor_exento', MONEY, server_default=text("((0))")),
    Column('estado', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nombre_endoso', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigo_endoso', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('rut_endoso', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cartola', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('vigencia', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('valor_neto', MONEY, server_default=text("((0))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Correlativo', SmallInteger, server_default=text("((0))")),
    Index('PKPrimaryKey', 'Tipo', 'Numero', 'Correlativo', 'TIPO1', unique=True),
    Index('hctadocto01', 'Rut_cliente', 'codigo_cliente', 'cartola', 'fecha_ingreso')
)


t_HDATOSCLIENTE = Table(
    'HDATOSCLIENTE', metadata,
    Column('Direccion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoVenta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Giro', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Despacho', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Telefono', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Comuna', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ruta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Razon', String(60, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Vendedor', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ciudad', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('tipoid', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Lista', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ComisionVendedor', MONEY, server_default=text("((0))")),
    Column('Cobrador', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ComisionCobrador', MONEY, server_default=text("((0))")),
    Column('CondicionVenta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Dias', SmallInteger, server_default=text("((0))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Transporte', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'Id', 'tipoid', unique=True)
)


t_HDESCUENTORECARGO = Table(
    'HDESCUENTORECARGO', metadata,
    Column('ValorMOn', MONEY, server_default=text("((0))")),
    Column('MontoMon', MONEY, server_default=text("((0))")),
    Column('tipoid', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipo', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Valor', MONEY, server_default=text("((0))")),
    Column('Monto', MONEY, server_default=text("((0))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('HDESCUENTO01', 'tipoid', 'Id'),
    Index('PKPrimaryKey', 'Id', 'Linea', unique=True)
)


t_HDETALLEDOCUMENTO = Table(
    'HDETALLEDOCUMENTO', metadata,
    Column('DatosKit', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cantidad', MONEY, server_default=text("((0))")),
    Column('Pedido', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PrecioVenta', MONEY, server_default=text("((0))")),
    Column('PrecioCosto', MONEY, server_default=text("((0))")),
    Column('Variacion', MONEY, server_default=text("((0))")),
    Column('Paridad', MONEY, server_default=text("((0))")),
    Column('PrecioCostoMOn', MONEY, server_default=text("((0))")),
    Column('PrecioVentaMon', MONEY, server_default=text("((0))")),
    Column('TotalLineaMOn', MONEY, server_default=text("((0))")),
    Column('ParidadMOn', MONEY, server_default=text("((0))")),
    Column('Caja', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CompletoIncompleto', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Alternativo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Subpedido', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TotalLinea', MONEY, server_default=text("((0))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipoid', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Descripcion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('HDETALLEDOCUMENTO02', 'Articulo', 'Atributo', 'Especificacion'),
    Index('HDETALLEDOCUMENTO01', 'Pedido', 'Articulo', 'Atributo', 'Especificacion'),
    Index('HDETALLEDOCUMENTO03', 'Tipoid', 'Id'),
    Index('PKPrimaryKey', 'Id', 'Linea', unique=True),
    Index('HDETALLEDOCUMENTO04', 'Articulo', 'Tipoid', 'Pedido', 'Id'),
    Index('HDETALLEDOCUMENTO05', 'Local', 'Articulo', 'Atributo', 'Especificacion')
)


t_HENCABEZADOCUMENTO = Table(
    'HENCABEZADOCUMENTO', metadata,
    Column('LocalDes', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('NetooBruto', BIT, server_default=text("((1))")),
    Column('Subpedido', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Caja', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CompletoIncompleto', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoMoneda', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('FacturaAnticipo', String(1, 'Modern_Spanish_CI_AS'), server_default=text("('N')")),
    Column('Facturado', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Emitido', BIT, server_default=text("((0))")),
    Column('Vigente', BIT, server_default=text("((1))")),
    Column('NumeroRelacionador', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TIPO1', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('FueraPlazo', BIT, server_default=text("((0))")),
    Column('traspasado', BIT, server_default=text("((0))")),
    Column('Impreso', BIT, server_default=text("((0))")),
    Column('Comentario', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('AfectoExento', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Factura', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('OrdenCompra', String(11, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Pedido', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Vence', DateTime, server_default=text("(space((0)))")),
    Column('Fecha', DateTime, server_default=text("(space((0)))")),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoRelacionador', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), unique=True, server_default=text("(space((0)))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('hencabezadocumento02', 'Rut', 'Codigo', 'Fecha'),
    Index('hencabezadocumento01', 'Tipo', 'Numero')
)


t_HTOTALDOCUMENTO = Table(
    'HTOTALDOCUMENTO', metadata,
    Column('TotalExentoMon', MONEY, server_default=text("((0))")),
    Column('TotalImpuestoEspecificoMOn', MONEY, server_default=text("((0))")),
    Column('TotalDetalleMon', MONEY, server_default=text("((0))")),
    Column('TotalIvaMon', MONEY, server_default=text("((0))")),
    Column('TotalIlaMOn', MONEY, server_default=text("((0))")),
    Column('TotalDescuentosMon', MONEY, server_default=text("((0))")),
    Column('TotalRecargosMon', MONEY, server_default=text("((0))")),
    Column('TotalRecuperacionMOn', MONEY, server_default=text("((0))")),
    Column('TotalMOn', MONEY, server_default=text("((0))")),
    Column('Total', MONEY, server_default=text("((0))")),
    Column('TotalImpuestoEspecifico', MONEY, server_default=text("((0))")),
    Column('TotalNetoMon', MONEY, server_default=text("((0))")),
    Column('PorcRecuperacionMOn', MONEY, server_default=text("((0))")),
    Column('TotalNeto', MONEY, server_default=text("((0))")),
    Column('TotalIla', MONEY, server_default=text("((0))")),
    Column('TotalIvaCarne', MONEY, server_default=text("((0))")),
    Column('TotalDetalle', MONEY, server_default=text("((0))")),
    Column('TotalDescuentos', MONEY, server_default=text("((0))")),
    Column('TotalRecargos', MONEY, server_default=text("((0))")),
    Column('PorcRecuperacion', SmallInteger, server_default=text("((0))")),
    Column('TotalRecuperacion', MONEY, server_default=text("((0))")),
    Column('TotalExento', MONEY, server_default=text("((0))")),
    Column('TotalIva', MONEY, server_default=text("((0))")),
    Column('TotalIvaCarneMon', MONEY, server_default=text("((0))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), unique=True, server_default=text("(space((0)))")),
    Column('TipoId', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('HTOTALDOCUMENTO01', 'TipoId', 'Id')
)


t_INVCLA = Table(
    'INVCLA', metadata,
    Column('usuario', String(40, 'Modern_Spanish_CI_AS'), unique=True, server_default=text("(space((0)))")),
    Column('password', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave1', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave2', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave3', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave4', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('clave5', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cantidadfilas', Integer, server_default=text("((0))")),
    Column('MargenIzquierdo', TINYINT, server_default=text("((0))")),
    Column('Atributo1', BIT, server_default=text("((0))"))
)


t_INVDETALLEPARTES = Table(
    'INVDETALLEPARTES', metadata,
    Column('Variacion', MONEY, server_default=text("((0))")),
    Column('Paridad', MONEY, server_default=text("((0))")),
    Column('TotalLineaMOn', MONEY, server_default=text("((0))")),
    Column('PrecioVenta', MONEY, server_default=text("((0))")),
    Column('ParidadMOn', MONEY, server_default=text("((0))")),
    Column('Referencia', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PrecioCostoMon', MONEY, server_default=text("((0))")),
    Column('PrecioVentaMOn', MONEY, server_default=text("((0))")),
    Column('IdOriginal', String(10, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('TotalLinea', MONEY, server_default=text("((0))")),
    Column('PrecioCosto', MONEY, server_default=text("((0))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Descripcion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cantidad', MONEY, server_default=text("((0))")),
    Column('OrdenC', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipoid', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('INVDETALLEDOC01', 'Local', 'Articulo', 'Atributo', 'Especificacion'),
    Index('PKPrimaryKey', 'Id', 'Linea', unique=True)
)


t_INVENCABEZAPARTES = Table(
    'INVENCABEZAPARTES', metadata,
    Column('RutProvee', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Impreso', BIT, server_default=text("((0))")),
    Column('Fecha', DateTime),
    Column('FacturaCompra', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((20)))")),
    Column('Comentario', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ajuste', BIT, server_default=text("((0))")),
    Column('Total', MONEY, server_default=text("((0))")),
    Column('Referencia', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('OrdenC', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoMoneda', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CodProvee', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('IdOriginal', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MOv', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('LocalDes', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), unique=True, server_default=text("(space((0)))")),
    Column('TotalMOn', MONEY, server_default=text("((0))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('INVencabezaPartes01', 'Tipo', 'Numero')
)


t_INVHDETALLEPARTES = Table(
    'INVHDETALLEPARTES', metadata,
    Column('Referencia', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PrecioVenta', MONEY, server_default=text("((0))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Descripcion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PrecioVentaMOn', MONEY, server_default=text("((0))")),
    Column('Cantidad', MONEY, server_default=text("((0))")),
    Column('ParidadMon', MONEY, server_default=text("((0))")),
    Column('PrecioCosto', MONEY, server_default=text("((0))")),
    Column('Variacion', MONEY, server_default=text("((0))")),
    Column('TotalLinea', MONEY, server_default=text("((0))")),
    Column('Paridad', MONEY, server_default=text("((0))")),
    Column('OrdenC', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PrecioCostoMOn', MONEY, server_default=text("((0))")),
    Column('TotalLIneaMOn', MONEY, server_default=text("((0))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipoid', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'Id', 'Linea', unique=True)
)


t_INVHENCABEZAPARTES = Table(
    'INVHENCABEZAPARTES', metadata,
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoMoneda', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TotalMon', MONEY, server_default=text("((0))")),
    Column('OrdenC', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Referencia', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Total', MONEY, server_default=text("((0))")),
    Column('Ajuste', BIT, server_default=text("((0))")),
    Column('Comentario', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('FacturaCompra', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((20)))")),
    Column('Fecha', DateTime),
    Column('Localdes', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), unique=True, server_default=text("(space((0)))"))
)


t_INVROTULO = Table(
    'INVROTULO', metadata,
    Column('MSArturo', String(18, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fechadeldia', DateTime, server_default=text("(space((0)))")),
    Column('serie', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('UsaEmisionPartes', BIT, server_default=text("((0))")),
    Column('Informado', BIT, server_default=text("((0))")),
    Column('FechaCalculo', DateTime, server_default=text("(space((0)))")),
    Column('CvtCtaCarnes', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((8)))")),
    Column('PPP', BIT, server_default=text("((0))")),
    Column('ConeccionContabilidad', BIT, server_default=text("((0))")),
    Column('FechaCM', DateTime, server_default=text("(space((0)))")),
    Column('CantidadLector', BIT, server_default=text("((0))"))
)


t_KIT = Table(
    'KIT', metadata,
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CodigoKit', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('cantidad', MONEY, server_default=text("((0))")),
    Column('VentaNeto', MONEY, server_default=text("((0))")),
    Column('VentaBruto', MONEY, server_default=text("((0))")),
    Column('CodigoLIsta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('unidad', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_MATRIZ = Table(
    'MATRIZ', metadata,
    Column('Especificacion', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Descripcion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Nivel', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_MONEDA = Table(
    'MONEDA', metadata,
    Column('DESCRIPCION', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('VALOR', MONEY, server_default=text("((0))")),
    Column('FECHA', DateTime, server_default=text("(space((0)))")),
    Column('CODIGO', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'CODIGO', 'FECHA', unique=True)
)


t_MSOCLIENTES = Table(
    'MSOCLIENTES', metadata,
    Column('Despacho', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ingreso', DateTime, server_default=text("(space((0)))")),
    Column('Comentario', String(200, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Giro', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Credito', MONEY, server_default=text("((0))")),
    Column('Categoria', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Frecuencia', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Zona', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Rubro', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cobrador', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Vendedor', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Clasificacion', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Condicion', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Razon', String(60, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Contacto2', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PosArticuloCliente', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Contacto1', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Internet', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Telefono', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ciudad', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Comuna', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Direccion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Sigla', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CondicionCompra', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PosEspecificacionCliente', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('SUCURSAL', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Negativo', BIT, server_default=text("((0))")),
    Column('dias_actualiza', Integer, server_default=text("((0))")),
    Column('LargoCodigo', TINYINT, server_default=text("((1))")),
    Column('PosAtributoCliente', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Importado', BIT, server_default=text("((0))")),
    Column('ITEM', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CUENTACORRIENTE', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CUENTAC', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('BANCOC', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Descuento_final', DateTime, server_default=text("(space((0)))")),
    Column('fecha_actualiza', DateTime, server_default=text("(space((0)))")),
    Column('AUXILIAR', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Descuento', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Transporte', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoVenta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ruta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CreditoMon', MONEY, server_default=text("((0))")),
    Column('Centro', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MasDatos', TEXT(2147483647, 'Modern_Spanish_CI_AS'), server_default=text("(space((1)))")),
    Column('Descuento_inicial', DateTime, server_default=text("(space((0)))")),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((3)))")),
    Index('PKPrimaryKey', 'Rut', 'Codigo', unique=True)
)


t_MSOGENERAL = Table(
    'MSOGENERAL', metadata,
    Column('path', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('iva', SMALLMONEY, server_default=text("((0))"))
)


t_MSOSTCOMPRAS = Table(
    'MSOSTCOMPRAS', metadata,
    Column('ValorExento', MONEY, server_default=text("((0))")),
    Column('RetencionIVA', MONEY, server_default=text("((0))")),
    Column('Vigente', BIT, server_default=text("((1))")),
    Column('MesDeclaracion', String(6, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ValorTotal', MONEY, server_default=text("((0))")),
    Column('ValorILA', MONEY, server_default=text("((0))")),
    Column('ValorIVA', MONEY, server_default=text("((0))")),
    Column('Emitido', BIT, server_default=text("((0))")),
    Column('LitrosCombustible', Float(53), server_default=text("((0))")),
    Column('ValorNeto', MONEY, server_default=text("((0))")),
    Column('FechaEmision', DateTime),
    Column('Centro', String(4, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('NumeroInterno', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ImpuestoEspecifico', MONEY, server_default=text("((0))")),
    Column('TipoDocumento', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('RutProveedor', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('msostcompras04', 'MesDeclaracion', 'Centro'),
    Index('PKMsoStCompras01', 'TipoDocumento', 'RutProveedor', 'Codigo', 'Numero', unique=True),
    Index('msostcompras03', 'TipoDocumento', 'FechaEmision')
)


t_MSOSTCOMPRASILA = Table(
    'MSOSTCOMPRASILA', metadata,
    Column('CodigoIla', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((2)))")),
    Column('TipoDocumento', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('valor', MONEY, server_default=text("((0))")),
    Column('ila', SmallInteger, server_default=text("((0))")),
    Column('Numero', String(9, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Correlativo', SmallInteger, server_default=text("((0))")),
    Column('RutProveedor', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigo', String(10, 'Modern_Spanish_CI_AS'))
)


t_MSOSTLOCAL = Table(
    'MSOSTLOCAL', metadata,
    Column('ciudad', String(25, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('BonoMeta', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Facturable', BIT, server_default=text("((1))")),
    Column('Com_SubJefe', MONEY, server_default=text("((0))")),
    Column('jefe', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Com_Jefe', MONEY, server_default=text("((0))")),
    Column('Com_Local', MONEY, server_default=text("((0))")),
    Column('TipoBono', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Com_Gral', MONEY, server_default=text("((0))")),
    Column('N_Vende', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MetaMon', MONEY, server_default=text("((0))")),
    Column('Meta', MONEY, server_default=text("((0))")),
    Column('SubJefe', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fono', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('comuna', String(25, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('direccion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('descripcion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigo', String(3, 'Modern_Spanish_CI_AS'), unique=True, server_default=text("(space((0)))"))
)


t_MSOSTTABLAS = Table(
    'MSOSTTABLAS', metadata,
    Column('ValorMon', MONEY, server_default=text("((0))")),
    Column('VariacionSemestral', MONEY, server_default=text("((0))")),
    Column('tratamiento', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('valor', MONEY, server_default=text("((0))")),
    Column('descripcion', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('VariacionAnual', MONEY, server_default=text("((0))")),
    Column('tabla', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigo', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Email3', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Email2', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Email1', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Departamento', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Email5', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Email4', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Email6', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('sbif', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigosii', String(4, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'tabla', 'codigo', unique=True),
    Index('msosttablas01', 'tabla', 'descripcion')
)


t_MSOSTVENTASILA = Table(
    'MSOSTVENTASILA', metadata,
    Column('tipo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TIPO1', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigo', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((2)))")),
    Column('valor', MONEY, server_default=text("((0))")),
    Column('numero', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ila', SmallInteger, server_default=text("((0))"))
)


t_MSOVENDEDOR = Table(
    'MSOVENDEDOR', metadata,
    Column('comentario', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('tipo', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('NoActivo', BIT, server_default=text("((0))")),
    Column('MetaMon', MONEY, server_default=text("((0))")),
    Column('estadocivil', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Meta', MONEY, server_default=text("((0))")),
    Column('comision', Float(53), server_default=text("((0))")),
    Column('fechaing', DateTime, server_default=text("(space((0)))")),
    Column('fechanac', DateTime, server_default=text("(space((0)))")),
    Column('telefono', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ciudad', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('comuna', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('direccion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nombre', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_MSROTULO = Table(
    'MSROTULO', metadata,
    Column('MSNB', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ingtelas', BIT, server_default=text("((0))")),
    Column('MsNina', BIT, server_default=text("((1))")),
    Column('empresa', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('UsaParidad', BIT, server_default=text("((1))")),
    Column('Act_Economica', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Region', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MSJFP', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MsAgustin', BIT, server_default=text("((1))")),
    Column('MsSeguro', BIT, server_default=text("((1))")),
    Column('BaseDato', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Anselmo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cantidadlectorgv', BIT, server_default=text("((0))")),
    Column('TipoDE', BIT, server_default=text("((0))")),
    Column('Multiempresa', String(1, 'Modern_Spanish_CI_AS'), server_default=text("('N')")),
    Column('nombrerut', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('direccion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fonos', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nombreiva', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('sigla', String(25, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('giro', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('rutemp', String(14, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('comuna', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ciudad', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nombrecon', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Florencia', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TituloCon', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('rutrepleg', String(14, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('titulogg', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nombregg', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('nomrepleg', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Folio_Custodia', MONEY, server_default=text("((0))")),
    Column('Proveedorefact', String(20, 'Modern_Spanish_CI_AS')),
    Column('D_Elec', BIT, server_default=text("((1))"))
)


t_NUMERADOS = Table(
    'NUMERADOS', metadata,
    Column('articulo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("('')")),
    Column('correlativo', Integer, primary_key=True),
    Column('peso', MONEY, server_default=text("((0))")),
    Column('numero', Integer, server_default=text("((0))")),
    Column('narticulo', Integer)
)


t_PARAMETROS = Table(
    'PARAMETROS', metadata,
    Column('ImpresoraGuias', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cotizacion', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ruta', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ImpBoletera', BIT, server_default=text("((0))")),
    Column('Version', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CantidadCampos', Integer, server_default=text("((0))")),
    Column('CodTarjeta', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Lector', BIT, server_default=text("((0))")),
    Column('ImpresoraFactura', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Formato', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ImpresoraVale', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ImpresoraBoleta', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('UsuarioCaja', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ChequeMaximo', MONEY, server_default=text("((0))")),
    Column('ImpresoraNotasV', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ImpresoraNcredito', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('NDebito', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Balanza', BIT, server_default=text("((0))")),
    Column('LocalKit', BIT, server_default=text("((0))")),
    Column('Doblemoneda', BIT, server_default=text("((0))")),
    Column('ADICIONAL', BIT, server_default=text("((0))")),
    Column('CambiaPrevenPorc', SMALLMONEY, server_default=text("((0))")),
    Column('FactorFlete', SMALLMONEY, server_default=text("((0))")),
    Column('CambiaLocal', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('DescuentoMaximo', MONEY, server_default=text("((0))")),
    Column('LargoBarra', TINYINT, server_default=text("((0))")),
    Column('ParteConsumo', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CambiaCostoMaterial', BIT, server_default=text("((0))")),
    Column('CantidadLector', BIT, server_default=text("((0))")),
    Column('LargoMinutos', TINYINT, server_default=text("((0))")),
    Column('Puerto', SmallInteger, server_default=text("((1))")),
    Column('UsaCodigoFamilia', BIT, server_default=text("((0))")),
    Column('QCopiasV', Integer, server_default=text("((1))")),
    Column('ValFPago', BIT, server_default=text("((0))")),
    Column('IniVende', BIT, server_default=text("((0))")),
    Column('PuertoFiscal', SmallInteger, server_default=text("((1))")),
    Column('Fiscal', BIT, server_default=text("((0))")),
    Column('ArticulosActivos', TINYINT, server_default=text("((3))")),
    Column('NotaCredito', BIT, server_default=text("((0))")),
    Column('ProCodigoBarra', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('LargoCosto', TINYINT, server_default=text("((0))")),
    Column('ValorIva', SMALLMONEY, server_default=text("((0))")),
    Column('ImpuestoCarnes', BIT, server_default=text("((0))")),
    Column('CambiaPreVen', BIT, server_default=text("((0))")),
    Column('VenSinStock', BIT, server_default=text("((0))")),
    Column('EmpresaConstructora', BIT, server_default=text("((0))")),
    Column('Ila', BIT, server_default=text("((0))")),
    Column('NivelPreciosCostos', TINYINT, server_default=text("((0))")),
    Column('NivelPrecios', TINYINT, server_default=text("((0))")),
    Column('FolioDocumento', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('LargoVenta', TINYINT, server_default=text("((0))")),
    Column('PorcCarnes', Float(53), server_default=text("((0))")),
    Column('LargoCantidad', TINYINT, server_default=text("((0))")),
    Column('Decimal', BIT, server_default=text("((0))")),
    Column('CantidadxNivel', TINYINT, server_default=text("((0))")),
    Column('NombreMatriz', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CantidadNiveles', TINYINT, server_default=text("((0))")),
    Column('NombreAtributo', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ParteTraspaso', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('LocalCaja', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('LargoPU', TINYINT, server_default=text("((0))")),
    Column('GuiaDespacho', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ParteEgreso', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ParteIngreso', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('GuiaTransito', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('NVenta', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('NCredito', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Boleta', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('DesglosaPorKit', BIT, server_default=text("((0))")),
    Column('LargoArticulo', TINYINT, server_default=text("((0))")),
    Column('Imagen', BIT, server_default=text("((0))")),
    Column('LargoAtributo', TINYINT, server_default=text("((0))")),
    Column('MonedaDollar', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ComisionxArticulo', BIT, server_default=text("((0))")),
    Column('MonedaAlternativa', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MonedaLocal', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('GuiaTraspaso', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CodigoBarra', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('SinSaldoCredito', BIT, server_default=text("((0))")),
    Column('ValidaLineaCredito', BIT, server_default=text("((1))")),
    Column('MonedaTrabajo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Factura', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ImpuestoEspecifico', BIT, server_default=text("((0))"))
)


t_PASOARTXLOCAL = Table(
    'PASOARTXLOCAL', metadata,
    Column('Fecha', DateTime),
    Column('Kardex', MONEY, server_default=text("((0))")),
    Column('StockInicial', MONEY, server_default=text("((0))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Stock', MONEY, server_default=text("((0))")),
    Column('Precio', MONEY, server_default=text("((0))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Iden', DateTime),
    Index('ArtxLocalIndice', 'Iden', 'Articulo', 'Atributo', 'Especificacion')
)


t_PASOCPOABONOS = Table(
    'PASOCPOABONOS', metadata,
    Column('numero', String(9, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Valor_BrutoMOn', MONEY, server_default=text("((0))")),
    Column('Abonomon', MONEY, server_default=text("((0))")),
    Column('Hora', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Abono', MONEY, server_default=text("((0))")),
    Column('Valor_Bruto', MONEY, server_default=text("((0))")),
    Column('fechavence', DateTime),
    Column('correlativo', SmallInteger, server_default=text("((0))")),
    Column('tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fecha', DateTime)
)


t_PASOCTAABONOS = Table(
    'PASOCTAABONOS', metadata,
    Column('Hora', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Abonomon', MONEY, server_default=text("((0))")),
    Column('Valor_BrutoMOn', MONEY, server_default=text("((0))")),
    Column('Abono', MONEY, server_default=text("((0))")),
    Column('correlativo', SmallInteger, server_default=text("((0))")),
    Column('numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('fecha', DateTime, server_default=text("(space((0)))")),
    Column('fechavence', DateTime, server_default=text("(space((0)))")),
    Column('Valor_Bruto', MONEY, server_default=text("((0))"))
)


t_PASODATOSCLIENTE = Table(
    'PASODATOSCLIENTE', metadata,
    Column('Telefono', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Despacho', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Giro', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Transporte', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoVenta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ComisionVendedor', MONEY, server_default=text("((0))")),
    Column('Ciudad', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ruta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Direccion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Razon', String(60, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Lista', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Dias', SmallInteger, server_default=text("((0))")),
    Column('CondicionVenta', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cobrador', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Vendedor', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ComisionCobrador', MONEY, server_default=text("((0))")),
    Column('Comuna', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('TipoId', String(2, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))"))
)


t_PASODESCUENTORECARGO = Table(
    'PASODESCUENTORECARGO', metadata,
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Valor', MONEY, server_default=text("((0))")),
    Column('Monto', MONEY, server_default=text("((0))")),
    Column('ValorMOn', MONEY, server_default=text("((0))")),
    Column('MontoMOn', MONEY, server_default=text("((0))")),
    Column('tipoid', String(2, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Tipo', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_PASODETALLEDOCUMENTO = Table(
    'PASODETALLEDOCUMENTO', metadata,
    Column('Cantidad14', MONEY, server_default=text("((0))")),
    Column('Cantidad9', MONEY, server_default=text("((0))")),
    Column('Cantidad10', MONEY, server_default=text("((0))")),
    Column('DatosKit', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cantidad11', MONEY, server_default=text("((0))")),
    Column('Cantidad12', MONEY, server_default=text("((0))")),
    Column('Cantidad13', MONEY, server_default=text("((0))")),
    Column('Cantidad8', MONEY, server_default=text("((0))")),
    Column('Cantidad15', MONEY, server_default=text("((0))")),
    Column('PrecioVentaMOn', MONEY, server_default=text("((0))")),
    Column('PrecioCostoMon', MONEY, server_default=text("((0))")),
    Column('Indiceoc', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ParidadMon', MONEY, server_default=text("((0))")),
    Column('Alternativo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CompletoIncompleto', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cantidad7', MONEY, server_default=text("((0))")),
    Column('TotalLIneaMon', MONEY, server_default=text("((0))")),
    Column('Cantidad6', MONEY, server_default=text("((0))")),
    Column('Tipoid', String(2, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Descripcion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Pedido', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PrecioVenta', MONEY, server_default=text("((0))")),
    Column('Cantidad5', MONEY, server_default=text("((0))")),
    Column('Variacion', MONEY, server_default=text("((0))")),
    Column('Paridad', MONEY, server_default=text("((0))")),
    Column('TotalLinea', MONEY, server_default=text("((0))")),
    Column('Cantidad1', MONEY, server_default=text("((0))")),
    Column('Cantidad2', MONEY, server_default=text("((0))")),
    Column('Cantidad3', MONEY, server_default=text("((0))")),
    Column('Cantidad4', MONEY, server_default=text("((0))")),
    Column('PrecioCosto', MONEY, server_default=text("((0))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_PASODETALLEDOCUMENTOG = Table(
    'PASODETALLEDOCUMENTOG', metadata,
    Column('Cantidad13', MONEY, server_default=text("((0))")),
    Column('Cantidad12', MONEY, server_default=text("((0))")),
    Column('Cantidad11', MONEY, server_default=text("((0))")),
    Column('Cantidad10', MONEY, server_default=text("((0))")),
    Column('Cantidad14', MONEY, server_default=text("((0))")),
    Column('Cantidad8', MONEY, server_default=text("((0))")),
    Column('Cantidad9', MONEY, server_default=text("((0))")),
    Column('Cantidad15', MONEY, server_default=text("((0))")),
    Column('PrecioVentaMOn', MONEY, server_default=text("((0))")),
    Column('PrecioCostoMon', MONEY, server_default=text("((0))")),
    Column('TotalLIneaMon', MONEY, server_default=text("((0))")),
    Column('CompletoIncompleto', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Indiceoc', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cantidad7', MONEY, server_default=text("((0))")),
    Column('ParidadMon', MONEY, server_default=text("((0))")),
    Column('DatosKit', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Tipoid', String(2, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Alternativo', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cantidad6', MONEY, server_default=text("((0))")),
    Column('Descripcion', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Pedido', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('PrecioVenta', MONEY, server_default=text("((0))")),
    Column('Cantidad1', MONEY, server_default=text("((0))")),
    Column('PrecioCosto', MONEY, server_default=text("((0))")),
    Column('Cantidad4', MONEY, server_default=text("((0))")),
    Column('Cantidad2', MONEY, server_default=text("((0))")),
    Column('Cantidad3', MONEY, server_default=text("((0))")),
    Column('Cantidad5', MONEY, server_default=text("((0))")),
    Column('TotalLinea', MONEY, server_default=text("((0))")),
    Column('Paridad', MONEY, server_default=text("((0))")),
    Column('Variacion', MONEY, server_default=text("((0))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Linea', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_PASOENCABEZADOCUMENTO = Table(
    'PASOENCABEZADOCUMENTO', metadata,
    Column('TipoMoneda', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('FacturaAnticipo', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Facturado', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TipoId', String(2, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Vigente', BIT, server_default=text("((1))")),
    Column('Emitido', BIT, server_default=text("((0))")),
    Column('caja', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Hora', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CompletoIncompleto', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('DoctoMinera', BIT, server_default=text("((0))")),
    Column('VenceOC', DateTime, server_default=text("(space((0)))")),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('NumeroRelacionador', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('TIPO1', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Numero', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Fecha', DateTime, server_default=text("(space((0)))")),
    Column('TipoRelacionador', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('LocalDes', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Vence', DateTime, server_default=text("(space((0)))")),
    Column('Pedido', String(7, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Factura', String(8, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('AfectoExento', String(1, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Comentario', String(255, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Impreso', BIT, server_default=text("((0))")),
    Column('OrdenCompra', String(11, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('FueraPlazo', BIT, server_default=text("((0))")),
    Column('NetooBruto', BIT, server_default=text("((1))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Tipo', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_PASOENCABEZADOCUMENTOG = Table(
    'PASOENCABEZADOCUMENTOG', metadata,
    Column('VenceOC', DateTime, server_default=text("(space((0)))")),
    Column('DoctoMinera', BIT, server_default=text("((0))"))
)


t_PASOESTES = Table(
    'PASOESTES', metadata,
    Column('StockFisico', MONEY, server_default=text("((0))")),
    Column('StockValorizado', MONEY, server_default=text("((0))")),
    Column('Iden', DateTime, index=True),
    Column('PrecioCosto', MONEY, server_default=text("((0))")),
    Column('PrecioCostoIni', MONEY, server_default=text("((0))")),
    Column('PIA', MONEY, server_default=text("((0))")),
    Column('Salidas', MONEY, server_default=text("((0))")),
    Column('BO', MONEY, server_default=text("((0))")),
    Column('nusuario', Integer, server_default=text("((0))")),
    Column('TE', MONEY, server_default=text("((0))")),
    Column('Atributo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('StockInicial', MONEY, server_default=text("((0))")),
    Column('PI', MONEY, server_default=text("((0))")),
    Column('NV', MONEY, server_default=text("((0))")),
    Column('NC', MONEY, server_default=text("((0))")),
    Column('GD', MONEY, server_default=text("((0))")),
    Column('Entradas', MONEY, server_default=text("((0))")),
    Column('FA', MONEY, server_default=text("((0))")),
    Column('PE', MONEY, server_default=text("((0))")),
    Column('ND', MONEY, server_default=text("((0))")),
    Column('TS', MONEY, server_default=text("((0))")),
    Column('GT', MONEY, server_default=text("((0))")),
    Column('PC', MONEY, server_default=text("((0))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_PASOPRECIOSCOSTOS = Table(
    'PASOPRECIOSCOSTOS', metadata,
    Column('CostoCM', MONEY, server_default=text("((0))")),
    Column('CostoPesos', MONEY, server_default=text("((0))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Costo', MONEY, server_default=text("((0))")),
    Column('CoE', MONEY, server_default=text("((0))")),
    Column('StockCM', MONEY, server_default=text("((0))")),
    Column('CostoPesosMon', MONEY, server_default=text("((0))")),
    Column('Iden', DateTime, index=True),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'Iden', 'Articulo', 'Atributo', 'Especificacion', unique=True)
)


t_PASOTOTALDOCUMENTO = Table(
    'PASOTOTALDOCUMENTO', metadata,
    Column('TotalRecargosMon', MONEY, server_default=text("((0))")),
    Column('TotalDetalleMon', MONEY, server_default=text("((0))")),
    Column('TotalDescuentosMon', MONEY, server_default=text("((0))")),
    Column('TotalImpuestoEspecifico', MONEY, server_default=text("((0))")),
    Column('TotalIvaCarneMon', MONEY, server_default=text("((0))")),
    Column('PorcRecuperacionMOn', MONEY, server_default=text("((0))")),
    Column('TotalRecuperacionMOn', MONEY, server_default=text("((0))")),
    Column('TotalMOn', MONEY, server_default=text("((0))")),
    Column('TotalImpuestoEspecificoMOn', MONEY, server_default=text("((0))")),
    Column('TotalDetalle', MONEY, server_default=text("((0))")),
    Column('TotalIvaCarne', MONEY, server_default=text("((0))")),
    Column('TotalIla', MONEY, server_default=text("((0))")),
    Column('TotalIlaMOn', MONEY, server_default=text("((0))")),
    Column('TotalExento', MONEY, server_default=text("((0))")),
    Column('TotalIva', MONEY, server_default=text("((0))")),
    Column('TotalNetoMon', MONEY, server_default=text("((0))")),
    Column('TotalNeto', MONEY, server_default=text("((0))")),
    Column('TotalDescuentos', MONEY, server_default=text("((0))")),
    Column('TotalRecargos', MONEY, server_default=text("((0))")),
    Column('PorcRecuperacion', SmallInteger, server_default=text("((0))")),
    Column('TotalRecuperacion', MONEY, server_default=text("((0))")),
    Column('Total', MONEY, server_default=text("((0))")),
    Column('TotalIvaMon', MONEY, server_default=text("((0))")),
    Column('TotalExentoMon', MONEY, server_default=text("((0))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('TipoId', String(2, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))"))
)


t_PRECIOS = Table(
    'PRECIOS', metadata,
    Column('Nombre', String(30, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('VentaBruto', MONEY, server_default=text("((0))")),
    Column('VentaNeto', MONEY, server_default=text("((0))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CodigoLista', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'CodigoLista', 'Articulo', 'Atributo', 'Especificacion', 'Local', 'Rut', 'Codigo', unique=True),
    Index('PRECIOS01', 'Rut', 'Codigo', 'Articulo', 'Atributo', 'Especificacion'),
    Index('PRECIOS02', 'Local', 'Articulo', 'Atributo', 'Especificacion')
)


t_PRECIOSCOSTOS = Table(
    'PRECIOSCOSTOS', metadata,
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('CostoPesosMon', MONEY, server_default=text("((0))")),
    Column('CostoPesos', MONEY, server_default=text("((0))")),
    Column('StockCM', MONEY, server_default=text("((0))")),
    Column('CostoCM', MONEY, server_default=text("((0))")),
    Column('CoE', MONEY, server_default=text("((0))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Costo', MONEY, server_default=text("((0))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'Articulo', 'Atributo', 'Especificacion', unique=True)
)


t_ParEfact = Table(
    'ParEfact', metadata,
    Column('FoliosAutorizados', String(255, 'Modern_Spanish_CI_AS')),
    Column('DTEVentas', String(255, 'Modern_Spanish_CI_AS')),
    Column('E_LibroVentas', String(255, 'Modern_Spanish_CI_AS')),
    Column('E_LibroCmpra', String(255, 'Modern_Spanish_CI_AS')),
    Column('Acteco', String(50, 'Modern_Spanish_CI_AS')),
    Column('CodigoSii', String(9, 'Modern_Spanish_CI_AS')),
    Column('DescripcionSii', String(20, 'Modern_Spanish_CI_AS')),
    Column('CopiaFact', Integer),
    Column('CopiaNC', Integer),
    Column('CopiaND', Integer),
    Column('CopiaBol', Integer),
    Column('CopiaGDC', Integer),
    Column('CopiaGDR', Integer),
    Column('CopiaGDT', Integer),
    Column('RutaAdobe', String(200, 'Modern_Spanish_CI_AS')),
    Column('Usa33Pto_Pdf', BIT, server_default=text("((0))")),
    Column('Usa33Pto_Xml', BIT, server_default=text("((0))")),
    Column('Usa39Pto_Pdf', BIT),
    Column('Usa39Pto_Xml', BIT),
    Column('Usa52Pto_Pdf', BIT),
    Column('Usa52Pto_Xml', BIT),
    Column('Usa56Pto_Pdf', BIT),
    Column('Usa56Pto_Xml', BIT),
    Column('Usa61Pto_Pdf', BIT),
    Column('Usa61Pto_Xml', BIT),
    Column('Usa33Gev_Pdf', BIT),
    Column('Usa33Gev_Xml', BIT),
    Column('Usa39Gev_Pdf', BIT),
    Column('Usa39Gev_Xml', BIT),
    Column('Usa52Gev_Pdf', BIT),
    Column('Usa52Gev_Xml', BIT),
    Column('Usa56Gev_Pdf', BIT),
    Column('Usa56Gev_Xml', BIT),
    Column('Usa61Gev_Pdf', BIT),
    Column('Usa61Gev_Xml', BIT),
    Column('Resolucion', String(100, 'Modern_Spanish_CI_AS')),
    Column('Usa_SubTotal', BIT, server_default=text("((0))")),
    Column('Usa_FormaPago', BIT, server_default=text("((0))")),
    Column('TipoDePublicacion', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_PtoTermicas = Table(
    'PtoTermicas', metadata,
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Equipo', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('ruta', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Comentario', String(100, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))"))
)


t_RANKING = Table(
    'RANKING', metadata,
    Column('Fecha', DateTime, server_default=text("(space((0)))")),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Zona', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('DescPorc', MONEY, server_default=text("((0))")),
    Column('Descuento', MONEY, server_default=text("((0))")),
    Column('Razon', String(60, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Vence', DateTime, server_default=text("(space((0)))")),
    Column('Articulo', String(25, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('MargenPorc', MONEY, server_default=text("((0))")),
    Column('NomVended', String(40, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Vendedor', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Unidad', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Descripcion', String(50, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Cantidad', MONEY, server_default=text("((0))")),
    Column('Qporc', MONEY, server_default=text("((0))")),
    Column('Ventas', MONEY, server_default=text("((0))")),
    Column('VentasPorc', MONEY, server_default=text("((0))")),
    Column('Margen', MONEY, server_default=text("((0))")),
    Column('Identificador', String(12, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))"))
)


t_RespaldoMSOCLIENTES = Table(
    'RespaldoMSOCLIENTES', metadata,
    Column('Despacho', String(40, 'Modern_Spanish_CI_AS')),
    Column('Ingreso', DateTime),
    Column('Comentario', String(200, 'Modern_Spanish_CI_AS')),
    Column('Giro', String(40, 'Modern_Spanish_CI_AS')),
    Column('Credito', MONEY),
    Column('Categoria', String(3, 'Modern_Spanish_CI_AS')),
    Column('Frecuencia', String(3, 'Modern_Spanish_CI_AS')),
    Column('Zona', String(3, 'Modern_Spanish_CI_AS')),
    Column('Rubro', String(3, 'Modern_Spanish_CI_AS')),
    Column('Cobrador', String(3, 'Modern_Spanish_CI_AS')),
    Column('Vendedor', String(3, 'Modern_Spanish_CI_AS')),
    Column('Clasificacion', String(3, 'Modern_Spanish_CI_AS')),
    Column('Condicion', String(3, 'Modern_Spanish_CI_AS')),
    Column('Razon', String(60, 'Modern_Spanish_CI_AS')),
    Column('Contacto2', String(255, 'Modern_Spanish_CI_AS')),
    Column('PosArticuloCliente', String(30, 'Modern_Spanish_CI_AS')),
    Column('Contacto1', String(40, 'Modern_Spanish_CI_AS')),
    Column('Internet', String(40, 'Modern_Spanish_CI_AS')),
    Column('Telefono', String(40, 'Modern_Spanish_CI_AS')),
    Column('Ciudad', String(30, 'Modern_Spanish_CI_AS')),
    Column('Comuna', String(30, 'Modern_Spanish_CI_AS')),
    Column('Direccion', String(40, 'Modern_Spanish_CI_AS')),
    Column('Sigla', String(40, 'Modern_Spanish_CI_AS')),
    Column('CondicionCompra', String(3, 'Modern_Spanish_CI_AS')),
    Column('PosEspecificacionCliente', String(10, 'Modern_Spanish_CI_AS')),
    Column('SUCURSAL', String(3, 'Modern_Spanish_CI_AS')),
    Column('Negativo', BIT),
    Column('dias_actualiza', Integer),
    Column('LargoCodigo', TINYINT),
    Column('PosAtributoCliente', String(30, 'Modern_Spanish_CI_AS')),
    Column('Importado', BIT),
    Column('ITEM', String(5, 'Modern_Spanish_CI_AS')),
    Column('CUENTACORRIENTE', String(30, 'Modern_Spanish_CI_AS')),
    Column('CUENTAC', String(7, 'Modern_Spanish_CI_AS')),
    Column('BANCOC', String(3, 'Modern_Spanish_CI_AS')),
    Column('Descuento_final', DateTime),
    Column('fecha_actualiza', DateTime),
    Column('AUXILIAR', String(3, 'Modern_Spanish_CI_AS')),
    Column('Descuento', String(3, 'Modern_Spanish_CI_AS')),
    Column('Transporte', String(30, 'Modern_Spanish_CI_AS')),
    Column('TipoVenta', String(3, 'Modern_Spanish_CI_AS')),
    Column('Ruta', String(3, 'Modern_Spanish_CI_AS')),
    Column('CreditoMon', MONEY),
    Column('Centro', String(50, 'Modern_Spanish_CI_AS')),
    Column('MasDatos', TEXT(2147483647, 'Modern_Spanish_CI_AS')),
    Column('Descuento_inicial', DateTime),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS')),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'))
)


t_SPRING_SESSION = Table(
    'SPRING_SESSION', metadata,
    Column('PRIMARY_ID', CHAR(36, 'Modern_Spanish_CI_AS'), primary_key=True),
    Column('SESSION_ID', CHAR(36, 'Modern_Spanish_CI_AS'), nullable=False, unique=True),
    Column('CREATION_TIME', BigInteger, nullable=False),
    Column('LAST_ACCESS_TIME', BigInteger, nullable=False),
    Column('MAX_INACTIVE_INTERVAL', Integer, nullable=False),
    Column('EXPIRY_TIME', BigInteger, nullable=False, index=True),
    Column('PRINCIPAL_NAME', String(100, 'Modern_Spanish_CI_AS'), index=True)
)


t_STOCKMINIMO = Table(
    'STOCKMINIMO', metadata,
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('StockMinimo', MONEY, server_default=text("((0))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('PKPrimaryKey', 'Local', 'Articulo', 'Atributo', 'Especificacion', unique=True)
)


t_TABLAPASO = Table(
    'TABLAPASO', metadata,
    Column('Cobrador', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Facturas', MONEY, server_default=text("((0))")),
    Column('Razon', String(60, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Hora', String(10, 'Modern_Spanish_CI_AS'), index=True, server_default=text("(space((0)))")),
    Column('Rut', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Codigo', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('P_Venta', Float(53), server_default=text("((0))")),
    Column('TCliente', MONEY, server_default=text("((0))")),
    Column('B_Credito', MONEY, server_default=text("((0))")),
    Column('N_Venta', MONEY, server_default=text("((0))")),
    Column('Iva', Float(53), server_default=text("((0))")),
    Column('Vendedor', String(20, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Ventas', MONEY, server_default=text("((0))")),
    Column('Protestos', MONEY, server_default=text("((0))")),
    Column('Pagado', MONEY, server_default=text("((0))")),
    Column('Saldo', MONEY, server_default=text("((0))")),
    Column('N_Credito', Integer, server_default=text("((0))")),
    Column('N_Debito', MONEY, server_default=text("((0))")),
    Column('Boletas', MONEY, server_default=text("((0))"))
)


t_TOMAINVENTARIO = Table(
    'TOMAINVENTARIO', metadata,
    Column('Fecha', DateTime),
    Column('Partida', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Stock', MONEY, server_default=text("((0))")),
    Column('Especificacion', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Atributo', String(5, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Local', String(3, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Column('Digitado', BIT, server_default=text("((0))")),
    Column('Folio', String(10, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('Folio', 'Folio', 'Articulo', 'Atributo', 'Especificacion')
)


t_TOTALDOCUMENTO = Table(
    'TOTALDOCUMENTO', metadata,
    Column('TotalImpuestoEspecificoMOn', MONEY, server_default=text("((0))")),
    Column('TotalMOn', MONEY, server_default=text("((0))")),
    Column('TotalDetalle', MONEY, server_default=text("((0))")),
    Column('TotalIlaMOn', MONEY, server_default=text("((0))")),
    Column('PorcRecuperacionMOn', MONEY, server_default=text("((0))")),
    Column('TotalRecargosMon', MONEY, server_default=text("((0))")),
    Column('TotalDescuentosMon', MONEY, server_default=text("((0))")),
    Column('TotalDetalleMon', MONEY, server_default=text("((0))")),
    Column('TotalIvaCarneMon', MONEY, server_default=text("((0))")),
    Column('TotalRecuperacionMOn', MONEY, server_default=text("((0))")),
    Column('TotalDescuentos', MONEY, server_default=text("((0))")),
    Column('TotalNeto', MONEY, server_default=text("((0))")),
    Column('TotalIva', MONEY, server_default=text("((0))")),
    Column('TotalExento', MONEY, server_default=text("((0))")),
    Column('TotalRecargos', MONEY, server_default=text("((0))")),
    Column('TotalIvaCarne', MONEY, server_default=text("((0))")),
    Column('TotalExentoMon', MONEY, server_default=text("((0))")),
    Column('PorcRecuperacion', SmallInteger, server_default=text("((0))")),
    Column('TotalRecuperacion', MONEY, server_default=text("((0))")),
    Column('TotalImpuestoEspecifico', MONEY, server_default=text("((0))")),
    Column('Total', MONEY, server_default=text("((0))")),
    Column('TotalNetoMon', MONEY, server_default=text("((0))")),
    Column('TotalIvaMon', MONEY, server_default=text("((0))")),
    Column('TotalIla', MONEY, server_default=text("((0))")),
    Column('Id', String(10, 'Modern_Spanish_CI_AS'), unique=True, server_default=text("(space((0)))")),
    Column('TipoId', String(2, 'Modern_Spanish_CI_AS'), server_default=text("(space((0)))")),
    Index('TipoId', 'TipoId', 'Id')
)


t_VENTAS_METRICS = Table(
    'VENTAS_METRICS', metadata,
    Column('time', DateTime),
    Column('name', String(50, 'Modern_Spanish_CI_AS')),
    Column('ventaneta', Numeric(18, 0)),
    Column('ventabruta', Numeric(18, 0))
)


t_View_Stock = Table(
    'View_Stock', metadata,
    Column('Articulo', String(15, 'Modern_Spanish_CI_AS')),
    Column('Descripcion', String(40, 'Modern_Spanish_CI_AS')),
    Column('VentaNeto', MONEY),
    Column('PorcIla', Float(53)),
    Column('PorcCarne', Float(53)),
    Column('Unidad', String(3, 'Modern_Spanish_CI_AS')),
    Column('Stock', MONEY),
    Column('Pieces', Integer),
    Column('Numbered', Integer, nullable=False)
)


t_systranschemas = Table(
    'systranschemas', metadata,
    Column('tabid', Integer, nullable=False),
    Column('startlsn', BINARY(10), nullable=False, unique=True),
    Column('endlsn', BINARY(10), nullable=False),
    Column('typeid', Integer, nullable=False, server_default=text("((52))"))
)


t_SPRING_SESSION_ATTRIBUTES = Table(
    'SPRING_SESSION_ATTRIBUTES', metadata,
    Column('SESSION_PRIMARY_ID', ForeignKey('SPRING_SESSION.PRIMARY_ID'), primary_key=True, nullable=False),
    Column('ATTRIBUTE_NAME', String(200, 'Modern_Spanish_CI_AS'), primary_key=True, nullable=False),
    Column('ATTRIBUTE_BYTES', IMAGE, nullable=False)
)
