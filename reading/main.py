import msvcrt
import csv
import sqlite3
import os

BOOK_COL = "book"
BOOK_FILE = "books.csv"
BOOK_EXPORT = "sqlite.csv"
BOOK_SQLDB = "books.db"


def connect_sqlite_db():
    try:
        return sqlite3.connect(BOOK_SQLDB)
    except:
        print("Connection failed!")


def enter_book_col():
    """
    This Python function prompts the user to enter information about a book (title, author, and year)
    and returns a dictionary containing that information.
    :return: A dictionary containing the title, author, and year of a book.
    """
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))

    return {"title": title, "author": author, "year": year}


def add_book():
    """
    This function adds a book to a SQLite database.
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
    """
    The function `show_book_details` takes in an `id` and a `book` dictionary and prints out the details
    of the book.

    :param id: The unique identifier for the book
    :param book: The book parameter is a dictionary that contains information about a book, including
    its title, author, year of publication, price, and rating
    """
    print(
        f"{id}: {repr(book['title'])} - {repr(book['author'])} - {book['year']} - {book['price']} - {book['rating']}"
    )


def get_all_book():
    """
    This function retrieves all the data from the "book" table in a SQLite database and prints it.
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
    """
    This function searches for a book in a SQLite database based on the user inputted title.
    """
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
    """
    This function updates a book's information in a SQLite database based on the user's input of the
    book title.
    """

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
    """
    This function removes a book from a SQLite database based on the user inputted book title.
    """

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

    """
    This function reads data from a CSV file and inserts it into a SQLite database.
    """


def read_csv():

    try:
        db_col = connect_sqlite_db()
        cur = db_col.cursor()
        with open(BOOK_FILE, 'r') as file:
            data = csv.reader(file)
            next(data)

            for row in data:
                cur.execute(
                    'INSERT INTO book (title, author, year) VALUES (?, ?, ?)', row)
        db_col.commit()
        db_col.close()

    except Exception as e:
        print(e)


def export():
    """
    This function exports data from a SQLite database table to a CSV file.
    """
    try:
        db_col = connect_sqlite_db()
        cur = db_col.cursor()
        cur.execute('select * from book')
        new_name = input('Enter file name: ')
        os.rename(BOOK_EXPORT,new_name)
        with open(BOOK_EXPORT, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([i[0] for i in cur.description])
            writer.writerows(cur)
        db_col.close()
    except Exception as e:
        print(e)


options = ['Add new book', 'show list books', 'find books',
           'update book', 'remove book', 'read csv', 'export to csv', 'Exit']
functions = (add_book, get_all_book, search_book, update_book, remove_book,
             read_csv, export)


while True:
    selected_option_index = 0

    while True:
        # Print menu options
        for i, option in enumerate(options):
            if i == selected_option_index:
                print(f"> {option}")
            else:
                print(f"  {option}")

        # Wait for key press
        key = msvcrt.getch()

        # Move selection up
        if key == b'w' or key == b'W' or key == b'\xe0H':
            selected_option_index = (selected_option_index - 1) % len(options)

        # Move selection down
        elif key == b's' or key == b'S' or key == b'\xe0P':
            selected_option_index = (selected_option_index + 1) % len(options)

        # Select option
        elif key == b'\r':
            if selected_option_index == len(options) - 1:
                print("Exiting...\n")
                break
            else:
                print("\n")
                functions[selected_option_index]()
                print("\n")
                break
    if selected_option_index == len(options) - 1:
        break
