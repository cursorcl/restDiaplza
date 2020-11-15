from restDiaplza.sqlserver.basedipalza import Base, engine,session
from  restDiaplza.sqlserver.db_name import t_MSOCLIENTES

def run():
    clientes = session.query(t_MSOCLIENTES).all()
    for client in clientes:
        print(client)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    run()