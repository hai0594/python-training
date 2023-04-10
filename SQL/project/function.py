from project.db_connect import dbconnect 
import pymssql

server = 'TK-HAIND\SQL2019'
user = 'sa'
password = '123123'
database = 'book_store'
table = 'book'

sql_create_table = f"""
create table if not exist {table}(
title TEXT NOT NULL,
author TEXT NOT NULL,
year INTEGER NOT NULL
);"""

def input_book():
    title = input("Enter the book title\t: ").title()
    author = input("Enter the book author\t: ").capitalize()
    year = int(input("Enter the release year\t: "))
    return (title, author, year)

def create_book_table():
    with dbconnect(server,user,password,database) as conn:
        cur = conn.consur()
        cur.execute(sql_create_table)