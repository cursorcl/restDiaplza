from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime, base64
from utils import configuration

user = base64.b64decode(configuration.database_user).decode('utf-8')
password = base64.b64decode(configuration.database_password).decode('utf-8')
database_name = base64.b64decode(configuration.database_name).decode('utf-8')
db_ip = configuration.database_ip
db_port = configuration.database_port

engine = create_engine('mssql+pymssql://{}:{}@{}:{}/{}'.format(user, password, db_ip, db_port, database_name),
                       echo=False,
                       implicit_returning=False)

# create a configured 'Session' class
# Session = sessionmaker(autocommit=True, autoflush=True, bind=engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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
        conn.execute(users.insert(), {'rut': '1', 'password': 'Audi', 'lastlogin': datetime.datetime.now})

# data = {'rut' : '106137811', 'password' : encrypt_password('_l2j1rs2'), 'lastlogin': datetime.datetime.now}


Base = declarative_base()
