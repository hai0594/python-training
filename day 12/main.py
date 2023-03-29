import csv
import os
"""
It reads the file, skips the first line, then reads the rest of the lines, splits them on the comma,
and then creates a dictionary from the header and the line
"""
BOOK_FILE = "books.csv"

MENU = """Welcome to the program
1. Add new book
2. show list books
3. search books
4. update book
5. remove book
6. remove book file
7. create new book file
8. quit
Your choice: """

MENU2 = """
1. Update book
2. Remove book
3. exit
"""


try:
    with open(BOOK_FILE, mode='x') as f:
        f.write("Title,Author,Year\n")
except Exception:
    pass


def add_book():
    """
    It takes user input and writes it to a file.
    """
    Title = input("Title: ")
    Author = input("Author: ")
    Year = input("Year: ")
    book = f"{Title},{Author},{Year}\n"
    with open(BOOK_FILE, 'a') as file:
        file.write(book)


def show_book_details(id, line):
    title, author, year = line.strip().split(',')
    print(f"{id}. {title} ({author}) - {year}")


def return_all_book():
    """
    It reads the books.csv file and returns a json object of all the books in the file.
    :return: A list of dictionaries
    """

    with open(BOOK_FILE, 'r') as file:
        next(file)
        for id, line in enumerate(file, start=1):
            show_book_details(id, line)


def search_book():
    """
    It takes a book title as input, loads the JSON data from the return_all_book() function, and then
    loops through the data to find the book with the matching title.
    """
    """
    It takes a book title as input, loads the JSON data from the return_all_book() function, and then
    loops through the data to find the book with the matching title
    """
    search_title = input("Enter the book title: ")
    with open(BOOK_FILE) as book_file:
        next(book_file)
        for id, line in enumerate(book_file, start=1):
            title, author, year = line.strip().split(',')

            if title == search_title:
                lines = id,title,author,year
                print(f"{id}. {title} ({author}) - {year}")
                
                

def update_book():
    search_title = input("Enter the book title: ")
    found = False
    lines = []
    with open(BOOK_FILE) as book:
        next(book)
        for line in book:
            title, author, year = line.strip().split(',')
            if title == search_title:
                print(f'{title},{author}, {year}')
                new_title = input("New_Title: ")
                new_author = input("New_Author: ")
                new_year = input("New_Year: ")
                line1 = f"{new_title},{new_author},{new_year}\n"
                print(f'{new_title},{new_author}, {new_year}')
                found = True                
            else:
                line1 = line
            lines.append(line1)
        if not found:
            print('Not found')

    with open(BOOK_FILE, 'w') as book:
        book.writelines(lines)


def remove_book():
    pass

def remove_file():
    if os.path.exists(BOOK_FILE):
        os.remove(BOOK_FILE)                
    else:
        print(f'The book file {BOOK_FILE} does not exist')

def create_new_bookfile():
    try:
        with open(BOOK_FILE, mode='x') as f:
            f.write("Title,Author,Year\n")
    except Exception:
        pass



# The main function of the program. It is the first thing that runs when the program is executed.
choice = int(input(MENU))

operations = (add_book, return_all_book, search_book, update_book, remove_book, remove_file, create_new_bookfile)

while choice != 8:
    if choice in range(1, len(operations) + 1):
        operations[choice - 1]()
    else:
        print("Invalid choice. Please try again.")
    print()
    choice = int(input(MENU))