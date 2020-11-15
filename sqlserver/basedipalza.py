from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

from restDiaplza.utils.util import pwd_context, encrypt_password




engine = create_engine('mssql+pymssql://{}:{}@{}:{}/{}'.format('sa', '_l2j1rs2', '192.168.0.7', '1433', 'MASTERSOFT'))

# create a configured 'Session' class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

if not engine.has_table('EOS_USUARIOS'):
    metadata = MetaData(engine)

    users = Table('EOS_USUARIOS', metadata,
          Column('rut', String(10), primary_key=True, nullable=False),
          Column('password', String),
          Column('lastlogin', DateTime, onupdate=datetime.datetime.now))
    # Implement the creation
    metadata.create_all()
    with engine.begin() as conn:
        conn.execute(users.insert(), { 'rut': '1', 'password': 'Audi', 'lastlogin': datetime.datetime.now })

#data = {'rut' : '106137811', 'password' : encrypt_password('_l2j1rs2'), 'lastlogin': datetime.datetime.now}



Base = declarative_base()