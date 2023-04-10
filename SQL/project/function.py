from project.db_connect import dbconnect
import pymssql

server = 'DESKTOP-TKDEATD'
user = 'sa'
password = '123123'
database = 'book_store'
table = 'book'

sql_create_table = f"""
IF OBJECT_ID('book', 'U') IS NOT NULL
    DROP TABLE book
CREATE TABLE book (
    title VARCHAR(100),
    name VARCHAR(100),
    year INT NOT NULL,
    PRIMARY KEY(title)
)
"""
SQL_INSERT_COMMAND = f"INSERT INTO {table} VALUES (%s, %s, %d);"

SQL_SELECT_COMMAND = f"SELECT * FROM {table};"

SQL_DELETE_COMMAND = f"DELETE FROM {table} WHERE title=%s;"

SQL_UPDATE_COMMAND = f"""
UPDATE {table}
SET author=?, year=?
WHERE title=?;
"""


def create_book_table():
    with dbconnect(server,user,password,database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_create_table)

def input_book():
    title = input("Enter the book title\t: ").title()
    author = input("Enter the book author\t: ").capitalize()
    year = int(input("Enter the release year\t: "))
    return (title, author, year)



def insert_book_table():
    with dbconnect(server,user,password,database) as conn:
        cur = conn.cursor()
        cur.execute(SQL_INSERT_COMMAND, input_book())


def get_all_books():
    with dbconnect(server,user,password,database) as conn:
        cur = conn.cursor()
        cur.execute(SQL_SELECT_COMMAND)

        for title, author, year in cur.fetchall():
            print(f"{title} ({year}) - {author}")


def delete_book():
    title = input("Enter the book title\t: ").title()

    with dbconnect(server,user,password,database) as conn:
        cur = conn.cursor()
        cur.execute(SQL_DELETE_COMMAND, (title,))


def update_book():
    title, author, year = input_book()
    with dbconnect(server,user,password,database) as conn:
        cur = conn.cursor()
        cur.execute(SQL_UPDATE_COMMAND, (author, year, title))

