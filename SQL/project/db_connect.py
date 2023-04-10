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


