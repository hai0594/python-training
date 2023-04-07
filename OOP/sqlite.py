import sqlite3

def connect_db():
    try:
        bookdb = "books.db"
        return sqlite3.connect(bookdb)
    except:
            print("Connection failed!")


# This is a Python class that creates a book database, allows users to add, show, update, and delete
# books from the database.
class book:        
    def __init__(self) -> None:
        sql_createtable = """CREATE TABLE IF NOT EXISTS book (
	title TEXT PRIMARY KEY,
   	author TEXT ,
	year INTEGER )"""
        connect = connect_db()
        cur = connect.cursor()
        cur.execute(sql_createtable)
        connect.commit()
        connect.close()
   
    def add_book(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        sql_insert = f"insert into book values('{self.title}','{self.author}',{self.year})"
        connect = connect_db()
        cur = connect.cursor()
        cur.execute(sql_insert)
        connect.commit()
        connect.close()

    def show_book(self):
        sql_show = f"select * from book"
        connect = connect_db()
        cur = connect.cursor()
        cur.execute(sql_show)
        rows = cur.fetchall()        
        for row in rows:
            title,author,year = row
            print(f"{title} -({author}) release year: {year}")
        connect.close()

    def update_book(self,search,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        sql_update = f"update book set title = '{self.title}',author = '{self.author}',year = {self.year} where title ='{search}'"
        connect = connect_db()
        cur = connect.cursor()
        cur.execute(sql_update)
        connect.commit()
        connect.close()

    def delete_book(self,search):
        sql_delte = f"delete from book where title ='{search}'"
        connect = connect_db()
        cur = connect.cursor()
        cur.execute(sql_delte)
        connect.commit()
        connect.close()        
        
