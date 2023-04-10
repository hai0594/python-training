import pymssql

class dbconnect:
    def __init__(self, server,user,password,database):
        self.connection = None
        self.server = server
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self) -> pymssql.connect :
        self.connection = pymssql.connect(self.server,self.user,self.password,self.database)
        return self.connection
    
    def __exit__(self, exec_type, exec_val, exec_tb):
        self.connection.commit()
        self.connection.close()

server = 'TK-HAIND\SQL2019'
user = 'sa'
password = '123123'
database = 'book_store'
table = 'book'

sql_create_table = f"""
CREATE TABLE IF NOT EXISTS {table} (
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
);"""


def create_book_table():
    with dbconnect(server,user,password,database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_create_table)

create_book_table()