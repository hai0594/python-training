import csv
import json
import pandas as pd
import sqlite3

BOOK_COL = "book"
BOOK_FILE = "books.csv"
BOOK_SQLDB = "books.db"



def connect_sqlite_db():
    try:
        return sqlite3.connect(BOOK_SQLDB)
    except:
        print("Connection failed!")

try:   
    sql_create = """
    CREATE TABLE IF NOT EXISTS book (
	title TEXT PRIMARY KEY,
   	author TEXT ,
	year INTEGER )"""

    db_conn = connect_sqlite_db()
    cur = db_conn.cursor()
    cur.execute(sql_create)
    db_conn.commit()
    db_conn.close()

except Exception:
    pass

MENU = """Welcome to the program
1. Add new book
2. show list books
3. search books
4. update book
5. remove book
6. import csv
7. export
8. quit
Your choice: """


def enter_book_col():
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))

    return {"title": title, "author": author, "year": year}


def add_book():
    """
    It takes user input and writes it to a file.
    """
    try:
        title, author, year = enter_book_col().values()
        db_conn = connect_sqlite_db()
        sql_insert = f"insert into book values ('{title}', '{author}', {year})"

        cur = db_conn.cursor()
        cur.execute(sql_insert)
        db_conn.commit()
        db_conn.close()
    except Exception as e:
        print(e)


def show_book_details(id, book):
    print(
        f"{id}: {repr(book['title'])} - {repr(book['author'])} - {book['year']} - {book['price']} - {book['rating']}"
    )


def get_all_book():
    """
    It reads the books.csv file and returns a json object of all the books in the file.
    :return: A list of dictionaries
    """
    try:
        book_col = connect_sqlite_db()
        sql_select = f"select * from book"
        cur = book_col.cursor()
        cur.execute(sql_select)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        book_col.close()
    except Exception as e:
        print(e)    


def search_book():
    try:
        search_title = input("Enter the book title: ")
        book_col = connect_sqlite_db()
        sql_select = f"select * from book where title = '{search_title}'"
        cur = book_col.cursor()
        cur.execute(sql_select)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        book_col.close()
    except Exception as e:
        print(e)   


def update_book():
    try:
        search_title = input("Enter the book title: ")
        book_col = connect_sqlite_db()    
        title, author, year = enter_book_col().values()
        sql_update = f"update book set title = '{title}', author = '{author}', year = {year} where title = '{search_title}'"
        cur = book_col.cursor()
        cur.execute(sql_update)
        book_col.commit()
        book_col.close()
    except Exception as e:
        print(e)    

def remove_book():
    try: 
        search_title = input("Enter the book title: ")
        book_col = connect_sqlite_db()  
        sql_delete = f" delete from book where title = '{search_title}'"
        cur = book_col.cursor()
        cur.execute(sql_delete)
        book_col.commit()
        book_col.close()
    except Exception as e:
        print(e)


def read_csv():
    try: 
        with open(BOOK_FILE, 'r') as file:
            data = csv.DictReader(file)
            db_col = connect_sqlite_db()
            next(data)
            cur = db_col.cursor()
            sql_insert = f"INSERT INTO book (title, author, year) VALUES (?, ?, ?)"
            for row in data:
                cur.executemany(sql_insert,row)
            db_col.commit()
            db_col.close()

    except Exception as e:
        print(e)

def export():

    cursor = connect_sqlite_db().find()
    df = pd.DataFrame(list(cursor))
    df.drop('_id', axis=1, inplace=True)
    df.to_csv('mongo.csv', index=False, mode='w')


choice = int(input(MENU))

operations = (add_book, get_all_book, search_book, update_book, remove_book,
              read_csv, export)

while choice != 8:
    if choice in range(1, len(operations) + 1):
        operations[choice - 1]()
    else:
        print("Invalid choice. Please try again.")
    print()
    choice = int(input(MENU))
