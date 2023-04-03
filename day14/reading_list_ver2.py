from pymongo import MongoClient

import csv
import json
import pandas as pd

BOOK_DB = "BookDB"
BOOK_COL = "book"
CONN_STRING = "mongodb+srv://hai:1234@cluster0.ydkjnff.mongodb.net/test"
BOOK_FILE = "books.csv"
def connect_db():
    client = MongoClient(CONN_STRING)
    book_db = client["BookDB"]
    return book_db["book"] # collection in MongoDB

    


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
    price = float(input("Price: "))
    rating = float(input("Rating: "))

    return {
        "title": title,
        "author": author,
        "year": year,
        "price": price,
        "rating": rating
    }


def add_book():
    """
    It takes user input and writes it to a file.
    """
    book_col = enter_book_col()
    db_col = connect_db()
    db_col.insert_one(book_col)
    
def show_book_details(id, book):
    print(f"{id}: {repr(book['title'])} - {repr(book['author'])} - {book['year']} - {book['price']} - {book['rating']}")


def get_all_book():
    """
    It reads the books.csv file and returns a json object of all the books in the file.
    :return: A list of dictionaries
    """
    books = []

    book_col = connect_db()

    for doc in book_col.find().sort([('rating',1),('price',1)]):
        book = {}

        for key, value in doc.items():
            if key != '_id':
                book[key] = value

        books.append(book)

    if books:
        for id, book in enumerate(books, start=1):
            show_book_details(id, book)
                        
            
    else:
        print("The books is empty!")


def search_book():
    search_title = input("Enter the book title: ")
    found = False

    book_col = connect_db()

    for id, doc in enumerate(book_col.find(), start=1):

        if doc['title'] == search_title:
            show_book_details(id, doc)
            found = True
                    
    if not found:
        print(f"`{search_title}` is not found!")


def update_book():
    search_title = input("Enter the book title: ")
    found = False
    book_col = connect_db()

    for doc in book_col.find():

        if doc['title'] == search_title:
            found = True

    if found:
        myquery = { "title": search_title }
        newvalues = { "$set": enter_book_col()}
        book_col.update_one(myquery, newvalues)
    else:
        print(f'`{search_title}` is not found!')


def remove_book():
    search_title = input("Enter the book title: ")
    found = False
    book_col = connect_db()

    for doc in book_col.find():

        if doc['title'] == search_title:
            found = True

    if found:
        my_query = {'title': search_title}
        book_col.delete_one(my_query)
    else:
        print(f'`{search_title}` is not found!')


def read_csv():
    with open(BOOK_FILE,'r') as file:
        data = csv.DictReader(file)
        db_col = connect_db()


        for row in data:
            db_col.insert_one(row)
def export():
    
    cursor = connect_db().find()
    df = pd.DataFrame(list(cursor))
    df.drop('_id', axis=1, inplace=True)
    df.to_csv('mongo.csv', index=False, mode='w')       

choice = int(input(MENU))

operations = (add_book, get_all_book, search_book, update_book, remove_book, read_csv, export)

while choice != 8:
    if choice in range(1, len(operations) + 1):
        operations[choice - 1]()
    else:
        print("Invalid choice. Please try again.")
    print()
    choice = int(input(MENU))
