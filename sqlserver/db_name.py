# coding: utf-8
from sqlalchemy import BigInteger, CHAR, Column, DateTime, Float, Integer, LargeBinary, MetaData, Numeric, SmallInteger, String, TEXT, Table, text
from sqlalchemy.dialects.mssql import BIT, IMAGE, MONEY, SMALLMONEY, TIMESTAMP, TINYINT

metadata = MetaData()


t_ALTERNATIVO = Table(
    'ALTERNATIVO', metadata,
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Alternativo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', Integer),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_ARTICULO = Table(
    'ARTICULO', metadata,
    Column('MonedaImportado', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ConversionVolumen', Float(53)),
    Column('Moneda', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CtaResultado', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Kit', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CostoCentro', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CostoCuenta', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Importado', BIT),
    Column('Auxiliar', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CentroCosto', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PorcCarne', Float(53)),
    Column('ImpuestoEspecifico', SMALLMONEY),
    Column('CostoItem', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Activo', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ar_NoFacturable', BIT),
    Column('ItemGasto', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Familia', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('StockReal', MONEY),
    Column('PorcIla', Float(53)),
    Column('Costo', MONEY),
    Column('CostoEconomico', MONEY),
    Column('VentaNeto', MONEY),
    Column('VentaBruto', MONEY),
    Column('Inicio', DateTime),
    Column('CostoAuxiliar', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Imagen', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DescuentoPromocional', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ganado', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DescuentoInicio', DateTime),
    Column('Comision', SMALLMONEY),
    Column('Rut_Proveedor', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DescuentoFinal', DateTime),
    Column('Ubicacion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CodigoIla', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('StockMinimo', Float(53)),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descripcion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Nivel', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Unidad', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_ARTICULOSNUMERADOS = Table(
    'ARTICULOSNUMERADOS', metadata,
    Column('articulo', String(50, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_ARTXLOCAL = Table(
    'ARTXLOCAL', metadata,
    Column('Fecha', DateTime),
    Column('Kardex', Integer),
    Column('StockInicial', MONEY),
    Column('Stock', MONEY),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('StockCalculo', MONEY),
    Column('Salida', DateTime),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_ARTXLOCALLINEA = Table(
    'ARTXLOCALLINEA', metadata,
    Column('Stockinicial', Integer),
    Column('Stock', Integer),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Iden', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_ATRIBUTO = Table(
    'ATRIBUTO', metadata,
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_BITACORA = Table(
    'BITACORA', metadata,
    Column('Numero', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fecha', DateTime),
    Column('Hora', DateTime),
    Column('Sistema', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descripcion', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Formulario', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Clave', String(70, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tabla', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Criterio', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Computador', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FechaMOv', DateTime)
)


t_CARTOLA = Table(
    'CARTOLA', metadata,
    Column('Tipo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Origen', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Destino', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Entrada', MONEY),
    Column('Referencia', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('StockInicial', MONEY),
    Column('Fecha', DateTime),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Salida', MONEY),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Iden', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CARTOLAVALORIZADA = Table(
    'CARTOLAVALORIZADA', metadata,
    Column('SaldoDH', MONEY),
    Column('Haber', MONEY),
    Column('Debe', MONEY),
    Column('StockInicial', MONEY),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PrecioUnCompra', MONEY),
    Column('Iden', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Costo', MONEY),
    Column('Origen', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Destino', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Entrada', MONEY),
    Column('Salida', MONEY),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fecha', DateTime),
    Column('Referencia', String(7, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CODIGOBARRAART = Table(
    'CODIGOBARRAART', metadata,
    Column('Velocidad', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Secuencia', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Impresora', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Puerto', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Temperatura', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Retardo', MONEY),
    Column('Linea', String(60, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descripcion', String(100, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CONDUCCION = Table(
    'CONDUCCION', metadata,
    Column('codigo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ruta', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('precio', Integer),
    Column('articulo', String(50, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CORRELATIVONUMERADOS = Table(
    'CORRELATIVONUMERADOS', metadata,
    Column('Id', Integer),
    Column('correlativo', Integer)
)


t_CPOABONOS = Table(
    'CPOABONOS', metadata,
    Column('cargomon', MONEY),
    Column('codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('numero', String(9, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('correlativo', SmallInteger),
    Column('cargo', MONEY),
    Column('abono', MONEY),
    Column('cancela', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('AbonoTotal', BIT),
    Column('abonomon', MONEY),
    Column('rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cargo1', MONEY)
)


t_CPOARCHIVOPLANO = Table(
    'CPOARCHIVOPLANO', metadata,
    Column('BANCO', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LINEA', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TABLA', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CAMPO', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TIPO', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LARGO', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('INICIO', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CABECERA', String(1, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CPOCLA = Table(
    'CPOCLA', metadata,
    Column('clave2', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cantidadfilas', Integer),
    Column('atributo4', BIT),
    Column('atributo3', BIT),
    Column('atributo2', BIT),
    Column('atributo1', BIT),
    Column('password', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave3', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave1', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('atributo5', BIT),
    Column('clave5', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave4', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MargenIzquierdo', TINYINT),
    Column('usuario', String(40, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CPODOCTO = Table(
    'CPODOCTO', metadata,
    Column('Valor_Ilamon', MONEY),
    Column('Retencion', Float(53)),
    Column('cancela', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('emitido', BIT),
    Column('fueraPlazo', BIT),
    Column('FechaC', DateTime),
    Column('FechaR', DateTime),
    Column('FechaD', DateTime),
    Column('Valor_brutomon', MONEY),
    Column('Valor_Importacion', MONEY),
    Column('Valor_NetoMon', MONEY),
    Column('valor_abono', MONEY),
    Column('Valor_ivamon', MONEY),
    Column('Valor_abonoMon', MONEY),
    Column('ImpuestoespMon', MONEY),
    Column('Moneda', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Paridad', MONEY),
    Column('Retencionmon', MONEY),
    Column('Rut_Provee', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Valor_ExentoMon', MONEY),
    Column('estado', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Correlativo', SmallInteger),
    Column('codigo_Provee', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Glosa', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fecha_ingreso', DateTime),
    Column('fecha_vencimiento', DateTime),
    Column('fecha_inicial', DateTime),
    Column('Mesdeclaracion', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Valor_ImportacionMon', MONEY),
    Column('banco', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LitrosComb', Float(53)),
    Column('vigencia', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cambio', DateTime),
    Column('valor_bruto', MONEY),
    Column('valor_exento', MONEY),
    Column('valor_neto', MONEY),
    Column('valor_ila', MONEY),
    Column('valor_iva', MONEY),
    Column('ImpuestoEsp', MONEY),
    Column('CentroCosto', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Valor_IvaImportacion', MONEY),
    Column('TipoFactura', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Porc_Rete', TINYINT),
    Column('Valor_IvaImportacionMon', MONEY),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(9, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Folio', String(7, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CPONOMINAPAGO = Table(
    'CPONOMINAPAGO', metadata,
    Column('ValorPago', MONEY),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ValorAbono', MONEY),
    Column('Pago', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Razon', String(60, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vence', DateTime),
    Column('Emision', DateTime),
    Column('Glosa', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Sucursal', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ValorBruto', MONEY),
    Column('ValorIva', MONEY),
    Column('ValorNeto', MONEY),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FechaPago', DateTime),
    Column('Comentario', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Banco', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Egreso', String(6, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CPOROTULO = Table(
    'CPOROTULO', metadata,
    Column('Cancelacion', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('yearSgte', SmallInteger),
    Column('MSArturo', String(18, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FacturaImportacion', BIT),
    Column('MonedaTrabajo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MonedaAlternativa', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MonedaLocal', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DobleMoneda', BIT),
    Column('Retencion', TINYINT),
    Column('nombre1', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ConeccionContabilidad', BIT),
    Column('nombre2', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PathDos', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ConectaCompVtas', BIT),
    Column('ILA', BIT),
    Column('FoliosInternos', BIT),
    Column('ImpuestoEspecifico', MONEY),
    Column('ImpEspecifico', BIT),
    Column('EmpresaConstructora', BIT),
    Column('tipoCuenta', BIT),
    Column('valorIVA', SMALLMONEY),
    Column('folioUnico', BIT),
    Column('comuna', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('titulo1', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fechadeldia', DateTime),
    Column('titulocon', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombrecon', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('titulogg', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombregg', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fechaver', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('version', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nomrepleg', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('titulo2', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ciudad', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PorcCarnes', SMALLMONEY),
    Column('direccion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('rutemp', String(14, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('giro', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('sigla', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('empresa', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('serie', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CvtCtaCarnes', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('yearProceso', SmallInteger),
    Column('yearActual', SmallInteger),
    Column('ImpuestoCarnes', BIT),
    Column('rutrepleg', String(14, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TempField0', BIT)
)


t_CTAABONOS = Table(
    'CTAABONOS', metadata,
    Column('Tipo1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cancela', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('saldo', MONEY),
    Column('saldomon', MONEY),
    Column('abono', MONEY),
    Column('abonomon', MONEY),
    Column('cargo', MONEY),
    Column('cargomon', MONEY),
    Column('correlativo', SmallInteger),
    Column('numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigo', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('AbonoTotal', BIT),
    Column('rut', String(10, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CTABOLETIN = Table(
    'CTABOLETIN', metadata,
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Monto', MONEY),
    Column('Fecha', DateTime),
    Column('Boletin', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Situacion', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Carpeta', String(8, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CTACLA = Table(
    'CTACLA', metadata,
    Column('usuario', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('password', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave1', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave2', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave3', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave4', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('atributo1', BIT),
    Column('atributo2', BIT),
    Column('atributo3', BIT),
    Column('atributo4', BIT),
    Column('cantidadfilas', Integer),
    Column('MargenIzquierdo', TINYINT)
)


t_CTACREDITO = Table(
    'CTACREDITO', metadata,
    Column('MasDatos', TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fecha', DateTime),
    Column('NotasPedido', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Observacion3', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Observacion2', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Compra', MONEY),
    Column('Vendedor', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Observacion1', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Razon', String(60, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Condicion', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fax', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('RepLegal', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fonos', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Comite', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Carpeta', String(8, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_CTADOCTO = Table(
    'CTADOCTO', metadata,
    Column('FechaR', DateTime),
    Column('FechaP', DateTime),
    Column('FechaC', DateTime),
    Column('fueraPlazo', BIT),
    Column('valor_abono', MONEY),
    Column('vigente', BIT),
    Column('Recuperacion', MONEY),
    Column('deuda_directa', BIT),
    Column('glosa_directa', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cancela', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FechaE', DateTime),
    Column('Valor_NetoMOn', MONEY),
    Column('PorcRecuperacion', SMALLMONEY),
    Column('comision', SMALLMONEY),
    Column('emitido', BIT),
    Column('Valor_IvaMon', MONEY),
    Column('TIPO1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('valor_iva', MONEY),
    Column('ImpuestoEspecificoMon', MONEY),
    Column('Caja', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Paridad', MONEY),
    Column('Valor_BrutoMon', MONEY),
    Column('Valor_AbonoMon', MONEY),
    Column('FechaD', DateTime),
    Column('Valor_IlaMon', MONEY),
    Column('Valor_ExentoMOn', MONEY),
    Column('RecuperacionMon', MONEY),
    Column('ImpuestoEspecifico', MONEY),
    Column('LitrosCombustible', Float(53)),
    Column('cambio', DateTime),
    Column('Moneda', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ciudad', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('valor_ila', MONEY),
    Column('boleta_hasta', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Rut_cliente', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigo_cliente', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fecha_ingreso', DateTime),
    Column('fecha_vencimiento', DateTime),
    Column('fecha_inicial', DateTime),
    Column('vendedor', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cobrador', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('local_venta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NroCtaCte', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('banco', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('glosa', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('estado', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('vigencia', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cartola', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('rut_endoso', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigo_endoso', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombre_endoso', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('valor_bruto', MONEY),
    Column('valor_exento', MONEY),
    Column('valor_neto', MONEY),
    Column('plaza', BIT),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Correlativo', SmallInteger),
    Column('TipoSII', Integer)
)


t_CTAROTULO = Table(
    'CTAROTULO', metadata,
    Column('ImpEspecifico', BIT),
    Column('valorIVA', SMALLMONEY),
    Column('EmpresaConstructora', BIT),
    Column('ILA', BIT),
    Column('ConectaCompVtas', BIT),
    Column('Cancelacion', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ConeccionContabilidad', BIT),
    Column('yearActual', SmallInteger),
    Column('ImpuestoEspecifico', MONEY),
    Column('yearProceso', SmallInteger),
    Column('yearSgte', SmallInteger),
    Column('nombre1', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FoliosInternos', BIT),
    Column('folioUnico', BIT),
    Column('PathDos', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Doblemoneda', BIT),
    Column('MonedaLocal', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MonedaTrabajo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MonedaAlternativa', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('titulo2', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('serie', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('tipoCuenta', BIT),
    Column('sigla', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CvtCtaCarnes', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ImpuestoCarnes', BIT),
    Column('nombre2', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MSArturo', String(18, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PorcCarnes', SMALLMONEY),
    Column('empresa', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('giro', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('rutemp', String(14, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('direccion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('comuna', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ciudad', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombrecon', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fechadeldia', DateTime),
    Column('titulo1', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('rutrepleg', String(14, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('titulocon', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('titulogg', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombregg', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fechaver', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('version', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nomrepleg', String(40, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_DATOSCLIENTE = Table(
    'DATOSCLIENTE', metadata,
    Column('Despacho', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CondicionVenta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Dias', SmallInteger),
    Column('Ruta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Lista', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoVenta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ciudad', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Giro', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Razon', String(60, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Direccion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Comuna', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Telefono', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ComisionCobrador', MONEY),
    Column('Transporte', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ComisionVendedor', MONEY),
    Column('Vendedor', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cobrador', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_DESCUENTORECARGO = Table(
    'DESCUENTORECARGO', metadata,
    Column('MontoMon', MONEY),
    Column('Tipo', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Valor', MONEY),
    Column('tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ValorMOn', MONEY),
    Column('Monto', MONEY),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_DETALLEDOCUMENTO = Table(
    'DETALLEDOCUMENTO', metadata,
    Column('Pedido', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cantidad', MONEY),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TotalLinea', MONEY),
    Column('PrecioVentaMon', MONEY),
    Column('PrecioCostoMOn', MONEY),
    Column('Variacion', MONEY),
    Column('TotalLineaMOn', MONEY),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PrecioCosto', MONEY),
    Column('ParidadMOn', MONEY),
    Column('PrecioVenta', MONEY),
    Column('Paridad', MONEY),
    Column('Subpedido', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Indiceoc', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DatosKit', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Alternativo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Caja', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CompletoIncompleto', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descripcion', String(40, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_ENCABEZADOCUMENTO = Table(
    'ENCABEZADOCUMENTO', metadata,
    Column('FueraPlazo', BIT),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LocalDes', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fecha', DateTime),
    Column('Vence', DateTime),
    Column('Pedido', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('OrdenCompra', String(11, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Factura', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('AfectoExento', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Comentario', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TIPO1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NetooBruto', BIT),
    Column('FacFlete', Integer),
    Column('Caja', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Transporte', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('VenceOC', DateTime),
    Column('DoctoMinera', BIT),
    Column('traspasado', BIT),
    Column('Impreso', BIT),
    Column('Subpedido', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoRelacionador', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CompletoIncompleto', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoMoneda', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FacturaAnticipo', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Facturado', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Emitido', BIT),
    Column('Vigente', BIT),
    Column('NumeroRelacionador', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Mov', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fec_Carga', DateTime),
    Column('Foliocarga', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fec_Anula', DateTime),
    Column('Publicado', BIT, nullable=False),
    Column('PublicadoNro', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoSII', Integer)
)


t_EOS_CONFIGURACION = Table(
    'EOS_CONFIGURACION', metadata,
    Column('clave', String(255, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True),
    Column('valor', TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_EOS_LOGVENTAS = Table(
    'EOS_LOGVENTAS', metadata,
    Column('id', Integer, primary_key=True),
    Column('fecha', DateTime),
    Column('vendedor', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('tipo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('titulo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('mensaje', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('json_parameters', TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_EOS_POSITIONS = Table(
    'EOS_POSITIONS', metadata,
    Column('indice', Integer, primary_key=True),
    Column('vendedor', String(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('fecha', DateTime, nullable=False),
    Column('latitude', Float(53), nullable=False),
    Column('longitude', Float(53), nullable=False),
    Column('velocidad', Float(53), nullable=False, server_default=text("((-1))"))
)


t_EOS_REGISTROS = Table(
    'EOS_REGISTROS', metadata,
    Column('indice', BigInteger, nullable=False),
    Column('rut', String(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('codigo', String(19, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('vendedor', String(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('fila', Integer, nullable=False),
    Column('fecha', DateTime, nullable=False),
    Column('articulo', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cantidad', SMALLMONEY),
    Column('neto', SMALLMONEY),
    Column('descuento', SMALLMONEY),
    Column('codigoila', String(3, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('ila', SMALLMONEY),
    Column('carne', SMALLMONEY),
    Column('iva', SMALLMONEY),
    Column('precio', SMALLMONEY),
    Column('numeros', String(512, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('correlativos', String(512, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('pesos', String(1024, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('esnumerado', BIT),
    Column('totalila', SMALLMONEY),
    Column('sobrestock', BIT)
)


t_EOS_USUARIOS = Table(
    'EOS_USUARIOS', metadata,
    Column('rut', String(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('password', LargeBinary),
    Column('lastlogin', DateTime)
)


t_ESPECIALES = Table(
    'ESPECIALES', metadata,
    Column('id', Numeric(18, 0), nullable=False),
    Column('productoinicio', String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('productofinal', String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
)


t_FACELECTERR = Table(
    'FACELECTERR', metadata,
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fecha', DateTime),
    Column('Comentario', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Error', String(255, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_FACTURACION = Table(
    'FACTURACION', metadata,
    Column('Iden', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NetooBruto', BIT),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TIPO1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Pedido', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_FACTURACIONDES = Table(
    'FACTURACIONDES', metadata,
    Column('Iden', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Monto', MONEY),
    Column('Valor', MONEY)
)


t_FOLIOS = Table(
    'FOLIOS', metadata,
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TIPO1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_FORMATO = Table(
    'FORMATO', metadata,
    Column('Sensor', BIT),
    Column('Lineas', SmallInteger),
    Column('SeparacionLineas', SMALLMONEY),
    Column('FormularioContinuo', BIT),
    Column('Cantidad', Integer),
    Column('Impresora', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoFecha', TINYINT),
    Column('AnchoDoc', SMALLMONEY),
    Column('MM2año', SMALLMONEY),
    Column('Largo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MM2dia', SMALLMONEY),
    Column('LargoDoc', SMALLMONEY),
    Column('Separacion', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Decimal', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Matriz', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Letra', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('SeparacionTallas', SMALLMONEY),
    Column('Imprimir', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Mm2', SMALLMONEY),
    Column('Mm1', SMALLMONEY),
    Column('Texto', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Nombre', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fecha', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MM2mes', SMALLMONEY),
    Column('Ancho', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ila1', SMALLMONEY),
    Column('Ila15', SMALLMONEY),
    Column('Ila14', SMALLMONEY),
    Column('Ila13', SMALLMONEY),
    Column('Ila12', SMALLMONEY),
    Column('Ila11', SMALLMONEY),
    Column('Ila10', SMALLMONEY),
    Column('ImprimeDescripcion', BIT),
    Column('Ila2', SMALLMONEY),
    Column('Ila8', SMALLMONEY),
    Column('Ila7', SMALLMONEY),
    Column('Ila6', SMALLMONEY),
    Column('Ila5', SMALLMONEY),
    Column('Ila4', SMALLMONEY),
    Column('Ila3', SMALLMONEY),
    Column('Ila9', SMALLMONEY)
)


t_GEVCLA = Table(
    'GEVCLA', metadata,
    Column('usuario', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('password', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave1', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave2', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave3', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave4', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave5', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cantidadfilas', Integer),
    Column('MargenIzquierdo', TINYINT),
    Column('Atributo1', BIT)
)


t_GEVROTULO = Table(
    'GEVROTULO', metadata,
    Column('ConeccionContabilidad', BIT),
    Column('fechadeldia', DateTime),
    Column('serie', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ConeccionCambiaCuentas', BIT),
    Column('CvtCtaCarnes', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MSArturo', String(18, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('RefundeGuias', String(1, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_HCTADOCTO = Table(
    'HCTADOCTO', metadata,
    Column('FechaD', DateTime),
    Column('Recuperacion', MONEY),
    Column('FechaC', DateTime),
    Column('FechaR', DateTime),
    Column('FechaP', DateTime),
    Column('FechaE', DateTime),
    Column('glosa_directa', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fueraPlazo', BIT),
    Column('comision', SMALLMONEY),
    Column('emitido', BIT),
    Column('PorcRecuperacion', SMALLMONEY),
    Column('cambio', DateTime),
    Column('Caja', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('vigente', BIT),
    Column('LitrosCombustible', Float(53)),
    Column('ImpuestoEspecifico', MONEY),
    Column('Valor_BrutoMon', MONEY),
    Column('Valor_ExentoMOn', MONEY),
    Column('Valor_NetoMOn', MONEY),
    Column('Valor_IlaMon', MONEY),
    Column('Valor_IvaMon', MONEY),
    Column('Valor_AbonoMon', MONEY),
    Column('ImpuestoEspecificoMon', MONEY),
    Column('fecha_ingreso', DateTime),
    Column('Paridad', MONEY),
    Column('Moneda', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TIPO1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('deuda_directa', BIT),
    Column('RecuperacionMon', MONEY),
    Column('banco', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fecha_inicial', DateTime),
    Column('NroCtaCte', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cancela', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('boleta_hasta', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Rut_cliente', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigo_cliente', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fecha_vencimiento', DateTime),
    Column('vendedor', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cobrador', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('plaza', BIT),
    Column('ciudad', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('glosa', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('valor_bruto', MONEY),
    Column('valor_abono', MONEY),
    Column('valor_iva', MONEY),
    Column('valor_ila', MONEY),
    Column('local_venta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('valor_exento', MONEY),
    Column('estado', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombre_endoso', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigo_endoso', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('rut_endoso', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cartola', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('vigencia', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('valor_neto', MONEY),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Correlativo', SmallInteger)
)


t_HDATOSCLIENTE = Table(
    'HDATOSCLIENTE', metadata,
    Column('Direccion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoVenta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Giro', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Despacho', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Telefono', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Comuna', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ruta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Razon', String(60, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vendedor', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ciudad', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Lista', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ComisionVendedor', MONEY),
    Column('Cobrador', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ComisionCobrador', MONEY),
    Column('CondicionVenta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Dias', SmallInteger),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Transporte', String(30, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_HDESCUENTORECARGO = Table(
    'HDESCUENTORECARGO', metadata,
    Column('ValorMOn', MONEY),
    Column('MontoMon', MONEY),
    Column('tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Valor', MONEY),
    Column('Monto', MONEY),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_HDETALLEDOCUMENTO = Table(
    'HDETALLEDOCUMENTO', metadata,
    Column('DatosKit', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cantidad', MONEY),
    Column('Pedido', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PrecioVenta', MONEY),
    Column('PrecioCosto', MONEY),
    Column('Variacion', MONEY),
    Column('Paridad', MONEY),
    Column('PrecioCostoMOn', MONEY),
    Column('PrecioVentaMon', MONEY),
    Column('TotalLineaMOn', MONEY),
    Column('ParidadMOn', MONEY),
    Column('Caja', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CompletoIncompleto', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Alternativo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Subpedido', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TotalLinea', MONEY),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descripcion', String(40, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_HENCABEZADOCUMENTO = Table(
    'HENCABEZADOCUMENTO', metadata,
    Column('LocalDes', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NetooBruto', BIT),
    Column('Subpedido', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Caja', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CompletoIncompleto', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoMoneda', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FacturaAnticipo', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Facturado', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Emitido', BIT),
    Column('Vigente', BIT),
    Column('NumeroRelacionador', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TIPO1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FueraPlazo', BIT),
    Column('traspasado', BIT),
    Column('Impreso', BIT),
    Column('Comentario', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('AfectoExento', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Factura', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('OrdenCompra', String(11, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Pedido', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vence', DateTime),
    Column('Fecha', DateTime),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoRelacionador', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_HTOTALDOCUMENTO = Table(
    'HTOTALDOCUMENTO', metadata,
    Column('TotalExentoMon', MONEY),
    Column('TotalImpuestoEspecificoMOn', MONEY),
    Column('TotalDetalleMon', MONEY),
    Column('TotalIvaMon', MONEY),
    Column('TotalIlaMOn', MONEY),
    Column('TotalDescuentosMon', MONEY),
    Column('TotalRecargosMon', MONEY),
    Column('TotalRecuperacionMOn', MONEY),
    Column('TotalMOn', MONEY),
    Column('Total', MONEY),
    Column('TotalImpuestoEspecifico', MONEY),
    Column('TotalNetoMon', MONEY),
    Column('PorcRecuperacionMOn', MONEY),
    Column('TotalNeto', MONEY),
    Column('TotalIla', MONEY),
    Column('TotalIvaCarne', MONEY),
    Column('TotalDetalle', MONEY),
    Column('TotalDescuentos', MONEY),
    Column('TotalRecargos', MONEY),
    Column('PorcRecuperacion', SmallInteger),
    Column('TotalRecuperacion', MONEY),
    Column('TotalExento', MONEY),
    Column('TotalIva', MONEY),
    Column('TotalIvaCarneMon', MONEY),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoId', String(2, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_INVCLA = Table(
    'INVCLA', metadata,
    Column('usuario', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('password', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave1', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave2', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave3', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave4', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('clave5', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cantidadfilas', Integer),
    Column('MargenIzquierdo', TINYINT),
    Column('Atributo1', BIT)
)


t_INVDETALLEPARTES = Table(
    'INVDETALLEPARTES', metadata,
    Column('Variacion', MONEY),
    Column('Paridad', MONEY),
    Column('TotalLineaMOn', MONEY),
    Column('PrecioVenta', MONEY),
    Column('ParidadMOn', MONEY),
    Column('Referencia', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PrecioCostoMon', MONEY),
    Column('PrecioVentaMOn', MONEY),
    Column('IdOriginal', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TotalLinea', MONEY),
    Column('PrecioCosto', MONEY),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descripcion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cantidad', MONEY),
    Column('OrdenC', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_INVENCABEZAPARTES = Table(
    'INVENCABEZAPARTES', metadata,
    Column('RutProvee', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Impreso', BIT),
    Column('Fecha', DateTime),
    Column('FacturaCompra', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Comentario', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ajuste', BIT),
    Column('Total', MONEY),
    Column('Referencia', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('OrdenC', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoMoneda', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CodProvee', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('IdOriginal', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MOv', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LocalDes', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TotalMOn', MONEY),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_INVHDETALLEPARTES = Table(
    'INVHDETALLEPARTES', metadata,
    Column('Referencia', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PrecioVenta', MONEY),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descripcion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PrecioVentaMOn', MONEY),
    Column('Cantidad', MONEY),
    Column('ParidadMon', MONEY),
    Column('PrecioCosto', MONEY),
    Column('Variacion', MONEY),
    Column('TotalLinea', MONEY),
    Column('Paridad', MONEY),
    Column('OrdenC', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PrecioCostoMOn', MONEY),
    Column('TotalLIneaMOn', MONEY),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_INVHENCABEZAPARTES = Table(
    'INVHENCABEZAPARTES', metadata,
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoMoneda', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TotalMon', MONEY),
    Column('OrdenC', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Referencia', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Total', MONEY),
    Column('Ajuste', BIT),
    Column('Comentario', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FacturaCompra', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fecha', DateTime),
    Column('Localdes', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_INVROTULO = Table(
    'INVROTULO', metadata,
    Column('MSArturo', String(18, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fechadeldia', DateTime),
    Column('serie', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('UsaEmisionPartes', BIT),
    Column('Informado', BIT),
    Column('FechaCalculo', DateTime),
    Column('CvtCtaCarnes', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PPP', BIT),
    Column('ConeccionContabilidad', BIT),
    Column('FechaCM', DateTime),
    Column('CantidadLector', BIT)
)


t_KIT = Table(
    'KIT', metadata,
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CodigoKit', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('cantidad', MONEY),
    Column('VentaNeto', MONEY),
    Column('VentaBruto', MONEY),
    Column('CodigoLIsta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('unidad', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_MATRIZ = Table(
    'MATRIZ', metadata,
    Column('Especificacion', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descripcion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Nivel', String(2, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_MONEDA = Table(
    'MONEDA', metadata,
    Column('DESCRIPCION', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('VALOR', MONEY),
    Column('FECHA', DateTime),
    Column('CODIGO', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_MSOCLIENTES = Table(
    'MSOCLIENTES', metadata,
    Column('Despacho', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ingreso', DateTime),
    Column('Comentario', String(200, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Giro', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Credito', MONEY),
    Column('Categoria', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Frecuencia', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Zona', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Rubro', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cobrador', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vendedor', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Clasificacion', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Condicion', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Razon', String(60, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Contacto2', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PosArticuloCliente', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Contacto1', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Internet', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Telefono', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ciudad', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Comuna', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Direccion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Sigla', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CondicionCompra', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PosEspecificacionCliente', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('SUCURSAL', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Negativo', BIT),
    Column('dias_actualiza', Integer),
    Column('LargoCodigo', TINYINT),
    Column('PosAtributoCliente', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Importado', BIT),
    Column('ITEM', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CUENTACORRIENTE', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CUENTAC', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('BANCOC', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descuento_final', DateTime),
    Column('fecha_actualiza', DateTime),
    Column('AUXILIAR', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descuento', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Transporte', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoVenta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ruta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CreditoMon', MONEY),
    Column('Centro', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MasDatos', TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descuento_inicial', DateTime),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_MSOGENERAL = Table(
    'MSOGENERAL', metadata,
    Column('path', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('iva', SMALLMONEY)
)


t_MSOSTCOMPRAS = Table(
    'MSOSTCOMPRAS', metadata,
    Column('ValorExento', MONEY),
    Column('RetencionIVA', MONEY),
    Column('Vigente', BIT),
    Column('MesDeclaracion', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ValorTotal', MONEY),
    Column('ValorILA', MONEY),
    Column('ValorIVA', MONEY),
    Column('Emitido', BIT),
    Column('LitrosCombustible', Float(53)),
    Column('ValorNeto', MONEY),
    Column('FechaEmision', DateTime),
    Column('Centro', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NumeroInterno', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ImpuestoEspecifico', MONEY),
    Column('TipoDocumento', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('RutProveedor', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_MSOSTCOMPRASILA = Table(
    'MSOSTCOMPRASILA', metadata,
    Column('CodigoIla', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoDocumento', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('valor', MONEY),
    Column('ila', SmallInteger),
    Column('Numero', String(9, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Correlativo', SmallInteger),
    Column('RutProveedor', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigo', String(10, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_MSOSTLOCAL = Table(
    'MSOSTLOCAL', metadata,
    Column('ciudad', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('BonoMeta', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Facturable', BIT),
    Column('Com_SubJefe', MONEY),
    Column('jefe', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Com_Jefe', MONEY),
    Column('Com_Local', MONEY),
    Column('TipoBono', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Com_Gral', MONEY),
    Column('N_Vende', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MetaMon', MONEY),
    Column('Meta', MONEY),
    Column('SubJefe', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fono', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('comuna', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('direccion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('descripcion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_MSOSTTABLAS = Table(
    'MSOSTTABLAS', metadata,
    Column('ValorMon', MONEY),
    Column('VariacionSemestral', MONEY),
    Column('tratamiento', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('valor', MONEY),
    Column('descripcion', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('VariacionAnual', MONEY),
    Column('tabla', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigo', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Email3', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Email2', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Email1', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Departamento', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Email5', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Email4', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Email6', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('sbif', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigosii', String(4, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_MSOSTVENTASILA = Table(
    'MSOSTVENTASILA', metadata,
    Column('tipo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TIPO1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigo', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('valor', MONEY),
    Column('numero', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ila', SmallInteger)
)


t_MSOVENDEDOR = Table(
    'MSOVENDEDOR', metadata,
    Column('comentario', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('tipo', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NoActivo', BIT),
    Column('MetaMon', MONEY),
    Column('estadocivil', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Meta', MONEY),
    Column('comision', Float(53)),
    Column('fechaing', DateTime),
    Column('fechanac', DateTime),
    Column('telefono', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ciudad', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('comuna', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('direccion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombre', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('rut', String(10, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_MSROTULO = Table(
    'MSROTULO', metadata,
    Column('MSNB', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ingtelas', BIT),
    Column('MsNina', BIT),
    Column('empresa', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('UsaParidad', BIT),
    Column('Act_Economica', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Region', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MSJFP', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MsAgustin', BIT),
    Column('MsSeguro', BIT),
    Column('BaseDato', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Anselmo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cantidadlectorgv', BIT),
    Column('TipoDE', BIT),
    Column('Multiempresa', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombrerut', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('direccion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fonos', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombreiva', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('sigla', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('giro', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('rutemp', String(14, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('comuna', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ciudad', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombrecon', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Florencia', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TituloCon', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('rutrepleg', String(14, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('titulogg', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nombregg', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('nomrepleg', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Folio_Custodia', MONEY),
    Column('Proveedorefact', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('D_Elec', BIT)
)


t_NUMERADOS = Table(
    'NUMERADOS', metadata,
    Column('articulo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('correlativo', Integer, nullable=False),
    Column('peso', MONEY),
    Column('numero', Integer),
    Column('narticulo', Integer)
)


t_PARAMETROS = Table(
    'PARAMETROS', metadata,
    Column('ImpresoraGuias', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cotizacion', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ruta', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ImpBoletera', BIT),
    Column('Version', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CantidadCampos', Integer),
    Column('CodTarjeta', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Lector', BIT),
    Column('ImpresoraFactura', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Formato', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ImpresoraVale', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ImpresoraBoleta', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('UsuarioCaja', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ChequeMaximo', MONEY),
    Column('ImpresoraNotasV', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ImpresoraNcredito', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NDebito', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Balanza', BIT),
    Column('LocalKit', BIT),
    Column('Doblemoneda', BIT),
    Column('ADICIONAL', BIT),
    Column('CambiaPrevenPorc', SMALLMONEY),
    Column('FactorFlete', SMALLMONEY),
    Column('CambiaLocal', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DescuentoMaximo', MONEY),
    Column('LargoBarra', TINYINT),
    Column('ParteConsumo', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CambiaCostoMaterial', BIT),
    Column('CantidadLector', BIT),
    Column('LargoMinutos', TINYINT),
    Column('Puerto', SmallInteger),
    Column('UsaCodigoFamilia', BIT),
    Column('QCopiasV', Integer),
    Column('ValFPago', BIT),
    Column('IniVende', BIT),
    Column('PuertoFiscal', SmallInteger),
    Column('Fiscal', BIT),
    Column('ArticulosActivos', TINYINT),
    Column('NotaCredito', BIT),
    Column('ProCodigoBarra', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LargoCosto', TINYINT),
    Column('ValorIva', SMALLMONEY),
    Column('ImpuestoCarnes', BIT),
    Column('CambiaPreVen', BIT),
    Column('VenSinStock', BIT),
    Column('EmpresaConstructora', BIT),
    Column('Ila', BIT),
    Column('NivelPreciosCostos', TINYINT),
    Column('NivelPrecios', TINYINT),
    Column('FolioDocumento', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LargoVenta', TINYINT),
    Column('PorcCarnes', Float(53)),
    Column('LargoCantidad', TINYINT),
    Column('Decimal', BIT),
    Column('CantidadxNivel', TINYINT),
    Column('NombreMatriz', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CantidadNiveles', TINYINT),
    Column('NombreAtributo', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ParteTraspaso', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LocalCaja', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LargoPU', TINYINT),
    Column('GuiaDespacho', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ParteEgreso', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ParteIngreso', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('GuiaTransito', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NVenta', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NCredito', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Boleta', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DesglosaPorKit', BIT),
    Column('LargoArticulo', TINYINT),
    Column('Imagen', BIT),
    Column('LargoAtributo', TINYINT),
    Column('MonedaDollar', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ComisionxArticulo', BIT),
    Column('MonedaAlternativa', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MonedaLocal', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('GuiaTraspaso', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CodigoBarra', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('SinSaldoCredito', BIT),
    Column('ValidaLineaCredito', BIT),
    Column('MonedaTrabajo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Factura', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ImpuestoEspecifico', BIT)
)


t_PASOARTXLOCAL = Table(
    'PASOARTXLOCAL', metadata,
    Column('Fecha', DateTime),
    Column('Kardex', MONEY),
    Column('StockInicial', MONEY),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Stock', MONEY),
    Column('Precio', MONEY),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Iden', DateTime)
)


t_PASOCPOABONOS = Table(
    'PASOCPOABONOS', metadata,
    Column('numero', String(9, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Valor_BrutoMOn', MONEY),
    Column('Abonomon', MONEY),
    Column('Hora', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Abono', MONEY),
    Column('Valor_Bruto', MONEY),
    Column('fechavence', DateTime),
    Column('correlativo', SmallInteger),
    Column('tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fecha', DateTime)
)


t_PASOCTAABONOS = Table(
    'PASOCTAABONOS', metadata,
    Column('Hora', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Abonomon', MONEY),
    Column('Valor_BrutoMOn', MONEY),
    Column('Abono', MONEY),
    Column('correlativo', SmallInteger),
    Column('numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('fecha', DateTime),
    Column('fechavence', DateTime),
    Column('Valor_Bruto', MONEY)
)


t_PASODATOSCLIENTE = Table(
    'PASODATOSCLIENTE', metadata,
    Column('Telefono', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Despacho', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Giro', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Transporte', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoVenta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ComisionVendedor', MONEY),
    Column('Ciudad', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ruta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Direccion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Razon', String(60, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Lista', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Dias', SmallInteger),
    Column('CondicionVenta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cobrador', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vendedor', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ComisionCobrador', MONEY),
    Column('Comuna', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoId', String(2, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_PASODESCUENTORECARGO = Table(
    'PASODESCUENTORECARGO', metadata,
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Valor', MONEY),
    Column('Monto', MONEY),
    Column('ValorMOn', MONEY),
    Column('MontoMOn', MONEY),
    Column('tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_PASODETALLEDOCUMENTO = Table(
    'PASODETALLEDOCUMENTO', metadata,
    Column('Cantidad14', MONEY),
    Column('Cantidad9', MONEY),
    Column('Cantidad10', MONEY),
    Column('DatosKit', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cantidad11', MONEY),
    Column('Cantidad12', MONEY),
    Column('Cantidad13', MONEY),
    Column('Cantidad8', MONEY),
    Column('Cantidad15', MONEY),
    Column('PrecioVentaMOn', MONEY),
    Column('PrecioCostoMon', MONEY),
    Column('Indiceoc', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ParidadMon', MONEY),
    Column('Alternativo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CompletoIncompleto', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cantidad7', MONEY),
    Column('TotalLIneaMon', MONEY),
    Column('Cantidad6', MONEY),
    Column('Tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descripcion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Pedido', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PrecioVenta', MONEY),
    Column('Cantidad5', MONEY),
    Column('Variacion', MONEY),
    Column('Paridad', MONEY),
    Column('TotalLinea', MONEY),
    Column('Cantidad1', MONEY),
    Column('Cantidad2', MONEY),
    Column('Cantidad3', MONEY),
    Column('Cantidad4', MONEY),
    Column('PrecioCosto', MONEY),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_PASODETALLEDOCUMENTOG = Table(
    'PASODETALLEDOCUMENTOG', metadata,
    Column('Cantidad13', MONEY),
    Column('Cantidad12', MONEY),
    Column('Cantidad11', MONEY),
    Column('Cantidad10', MONEY),
    Column('Cantidad14', MONEY),
    Column('Cantidad8', MONEY),
    Column('Cantidad9', MONEY),
    Column('Cantidad15', MONEY),
    Column('PrecioVentaMOn', MONEY),
    Column('PrecioCostoMon', MONEY),
    Column('TotalLIneaMon', MONEY),
    Column('CompletoIncompleto', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Indiceoc', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cantidad7', MONEY),
    Column('ParidadMon', MONEY),
    Column('DatosKit', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipoid', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Alternativo', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cantidad6', MONEY),
    Column('Descripcion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Pedido', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PrecioVenta', MONEY),
    Column('Cantidad1', MONEY),
    Column('PrecioCosto', MONEY),
    Column('Cantidad4', MONEY),
    Column('Cantidad2', MONEY),
    Column('Cantidad3', MONEY),
    Column('Cantidad5', MONEY),
    Column('TotalLinea', MONEY),
    Column('Paridad', MONEY),
    Column('Variacion', MONEY),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Linea', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_PASOENCABEZADOCUMENTO = Table(
    'PASOENCABEZADOCUMENTO', metadata,
    Column('TipoMoneda', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FacturaAnticipo', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Facturado', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoId', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vigente', BIT),
    Column('Emitido', BIT),
    Column('caja', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Hora', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CompletoIncompleto', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DoctoMinera', BIT),
    Column('VenceOC', DateTime),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('NumeroRelacionador', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TIPO1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Numero', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Fecha', DateTime),
    Column('TipoRelacionador', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LocalDes', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vence', DateTime),
    Column('Pedido', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Factura', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('AfectoExento', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Comentario', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Impreso', BIT),
    Column('OrdenCompra', String(11, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FueraPlazo', BIT),
    Column('NetooBruto', BIT),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Tipo', String(2, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_PASOENCABEZADOCUMENTOG = Table(
    'PASOENCABEZADOCUMENTOG', metadata,
    Column('VenceOC', DateTime),
    Column('DoctoMinera', BIT)
)


t_PASOESTES = Table(
    'PASOESTES', metadata,
    Column('StockFisico', MONEY),
    Column('StockValorizado', MONEY),
    Column('Iden', DateTime),
    Column('PrecioCosto', MONEY),
    Column('PrecioCostoIni', MONEY),
    Column('PIA', MONEY),
    Column('Salidas', MONEY),
    Column('BO', MONEY),
    Column('nusuario', Integer),
    Column('TE', MONEY),
    Column('Atributo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('StockInicial', MONEY),
    Column('PI', MONEY),
    Column('NV', MONEY),
    Column('NC', MONEY),
    Column('GD', MONEY),
    Column('Entradas', MONEY),
    Column('FA', MONEY),
    Column('PE', MONEY),
    Column('ND', MONEY),
    Column('TS', MONEY),
    Column('GT', MONEY),
    Column('PC', MONEY),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_PASOPRECIOSCOSTOS = Table(
    'PASOPRECIOSCOSTOS', metadata,
    Column('CostoCM', MONEY),
    Column('CostoPesos', MONEY),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Costo', MONEY),
    Column('CoE', MONEY),
    Column('StockCM', MONEY),
    Column('CostoPesosMon', MONEY),
    Column('Iden', DateTime),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_PASOTOTALDOCUMENTO = Table(
    'PASOTOTALDOCUMENTO', metadata,
    Column('TotalRecargosMon', MONEY),
    Column('TotalDetalleMon', MONEY),
    Column('TotalDescuentosMon', MONEY),
    Column('TotalImpuestoEspecifico', MONEY),
    Column('TotalIvaCarneMon', MONEY),
    Column('PorcRecuperacionMOn', MONEY),
    Column('TotalRecuperacionMOn', MONEY),
    Column('TotalMOn', MONEY),
    Column('TotalImpuestoEspecificoMOn', MONEY),
    Column('TotalDetalle', MONEY),
    Column('TotalIvaCarne', MONEY),
    Column('TotalIla', MONEY),
    Column('TotalIlaMOn', MONEY),
    Column('TotalExento', MONEY),
    Column('TotalIva', MONEY),
    Column('TotalNetoMon', MONEY),
    Column('TotalNeto', MONEY),
    Column('TotalDescuentos', MONEY),
    Column('TotalRecargos', MONEY),
    Column('PorcRecuperacion', SmallInteger),
    Column('TotalRecuperacion', MONEY),
    Column('Total', MONEY),
    Column('TotalIvaMon', MONEY),
    Column('TotalExentoMon', MONEY),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoId', String(2, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_PRECIOS = Table(
    'PRECIOS', metadata,
    Column('Nombre', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('VentaBruto', MONEY),
    Column('VentaNeto', MONEY),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CodigoLista', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_PRECIOSCOSTOS = Table(
    'PRECIOSCOSTOS', metadata,
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CostoPesosMon', MONEY),
    Column('CostoPesos', MONEY),
    Column('StockCM', MONEY),
    Column('CostoCM', MONEY),
    Column('CoE', MONEY),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Costo', MONEY),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_ParEfact = Table(
    'ParEfact', metadata,
    Column('FoliosAutorizados', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DTEVentas', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('E_LibroVentas', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('E_LibroCmpra', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Acteco', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CodigoSii', String(9, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DescripcionSii', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CopiaFact', Integer),
    Column('CopiaNC', Integer),
    Column('CopiaND', Integer),
    Column('CopiaBol', Integer),
    Column('CopiaGDC', Integer),
    Column('CopiaGDR', Integer),
    Column('CopiaGDT', Integer),
    Column('RutaAdobe', String(200, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Usa33Pto_Pdf', BIT),
    Column('Usa33Pto_Xml', BIT),
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
    Column('Resolucion', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Usa_SubTotal', BIT),
    Column('Usa_FormaPago', BIT),
    Column('TipoDePublicacion', String(50, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_PtoTermicas = Table(
    'PtoTermicas', metadata,
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Equipo', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ruta', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Comentario', String(100, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_RANKING = Table(
    'RANKING', metadata,
    Column('Fecha', DateTime),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Zona', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DescPorc', MONEY),
    Column('Descuento', MONEY),
    Column('Razon', String(60, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vence', DateTime),
    Column('Articulo', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MargenPorc', MONEY),
    Column('NomVended', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vendedor', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Unidad', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descripcion', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cantidad', MONEY),
    Column('Qporc', MONEY),
    Column('Ventas', MONEY),
    Column('VentasPorc', MONEY),
    Column('Margen', MONEY),
    Column('Identificador', String(12, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_RespaldoMSOCLIENTES = Table(
    'RespaldoMSOCLIENTES', metadata,
    Column('Despacho', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ingreso', DateTime),
    Column('Comentario', String(200, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Giro', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Credito', MONEY),
    Column('Categoria', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Frecuencia', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Zona', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Rubro', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Cobrador', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Vendedor', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Clasificacion', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Condicion', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Razon', String(60, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Contacto2', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PosArticuloCliente', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Contacto1', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Internet', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Telefono', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ciudad', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Comuna', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Direccion', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Sigla', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CondicionCompra', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PosEspecificacionCliente', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('SUCURSAL', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Negativo', BIT),
    Column('dias_actualiza', Integer),
    Column('LargoCodigo', TINYINT),
    Column('PosAtributoCliente', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Importado', BIT),
    Column('ITEM', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CUENTACORRIENTE', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CUENTAC', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('BANCOC', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descuento_final', DateTime),
    Column('fecha_actualiza', DateTime),
    Column('AUXILIAR', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descuento', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Transporte', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoVenta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ruta', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CreditoMon', MONEY),
    Column('Centro', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MasDatos', TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Descuento_inicial', DateTime),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_SPRING_SESSION = Table(
    'SPRING_SESSION', metadata,
    Column('PRIMARY_ID', CHAR(36, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('SESSION_ID', CHAR(36, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('CREATION_TIME', BigInteger, nullable=False),
    Column('LAST_ACCESS_TIME', BigInteger, nullable=False),
    Column('MAX_INACTIVE_INTERVAL', Integer, nullable=False),
    Column('EXPIRY_TIME', BigInteger, nullable=False),
    Column('PRINCIPAL_NAME', String(100, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_SPRING_SESSION_ATTRIBUTES = Table(
    'SPRING_SESSION_ATTRIBUTES', metadata,
    Column('SESSION_PRIMARY_ID', CHAR(36, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('ATTRIBUTE_NAME', String(200, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('ATTRIBUTE_BYTES', IMAGE, nullable=False)
)


t_STOCKMINIMO = Table(
    'STOCKMINIMO', metadata,
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('StockMinimo', MONEY),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_TABLAPASO = Table(
    'TABLAPASO', metadata,
    Column('Cobrador', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Facturas', MONEY),
    Column('Razon', String(60, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Hora', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Rut', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Codigo', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('P_Venta', Float(53)),
    Column('TCliente', MONEY),
    Column('B_Credito', MONEY),
    Column('N_Venta', MONEY),
    Column('Iva', Float(53)),
    Column('Vendedor', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Ventas', MONEY),
    Column('Protestos', MONEY),
    Column('Pagado', MONEY),
    Column('Saldo', MONEY),
    Column('N_Credito', Integer),
    Column('N_Debito', MONEY),
    Column('Boletas', MONEY)
)


t_TOMAINVENTARIO = Table(
    'TOMAINVENTARIO', metadata,
    Column('Fecha', DateTime),
    Column('Partida', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Stock', MONEY),
    Column('Especificacion', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Atributo', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Articulo', String(15, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Local', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Digitado', BIT),
    Column('Folio', String(10, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_TOTALDOCUMENTO = Table(
    'TOTALDOCUMENTO', metadata,
    Column('TotalImpuestoEspecificoMOn', MONEY),
    Column('TotalMOn', MONEY),
    Column('TotalDetalle', MONEY),
    Column('TotalIlaMOn', MONEY),
    Column('PorcRecuperacionMOn', MONEY),
    Column('TotalRecargosMon', MONEY),
    Column('TotalDescuentosMon', MONEY),
    Column('TotalDetalleMon', MONEY),
    Column('TotalIvaCarneMon', MONEY),
    Column('TotalRecuperacionMOn', MONEY),
    Column('TotalDescuentos', MONEY),
    Column('TotalNeto', MONEY),
    Column('TotalIva', MONEY),
    Column('TotalExento', MONEY),
    Column('TotalRecargos', MONEY),
    Column('TotalIvaCarne', MONEY),
    Column('TotalExentoMon', MONEY),
    Column('PorcRecuperacion', SmallInteger),
    Column('TotalRecuperacion', MONEY),
    Column('TotalImpuestoEspecifico', MONEY),
    Column('Total', MONEY),
    Column('TotalNetoMon', MONEY),
    Column('TotalIvaMon', MONEY),
    Column('TotalIla', MONEY),
    Column('Id', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TipoId', String(2, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_VENTAS_METRICS = Table(
    'VENTAS_METRICS', metadata,
    Column('time', DateTime),
    Column('name', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ventaneta', Numeric(18, 0)),
    Column('ventabruta', Numeric(18, 0))
)
