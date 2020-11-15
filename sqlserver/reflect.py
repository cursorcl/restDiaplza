from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
engine = create_engine('mssql+pyodbc://sa:_l2j1rs2@dipalza32', legacy_schema_aliasing=True)

# reflect the tables
Base.prepare(engine, reflect=True)


ArtXLocal = Base.classes.ARTXLOCAL


session = Session(engine)
articulos = session.query(ArtXLocal).all()
for articulo in articulos:
    print(articulo)
