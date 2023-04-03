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
6. mark_book
7. quit
Your choice: """


try:
    with open(BOOK_FILE, mode='x') as f:
        f.write("Title,Author,Year\n")
except Exception:
    pass


def input_book():
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    return (title, author, year)


def add_book():
    """
    It takes user input and writes it to a file.
    """
    title, author, year = input_book()
    with open(BOOK_FILE, 'a') as file:
        file.write(f"{title},{author},{year}\n")


def show_book_details(id, line):
    title, author, year = line.split(',')
    print(f"{id}. {title} ({author}) - {year}")


def return_all_book():
    """
    It reads the books.csv file and returns a json object of all the books in the file.
    :return: A list of dictionaries
    """

    with open(BOOK_FILE, 'r') as file:
        next(file)
        books = [line.strip() for line in file.readlines()]

    if books:
        for id, book in enumerate(books, start=1):
            show_book_details(id, book)
    else:
        print("The books is empty!")


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
    found = False

    with open(BOOK_FILE) as book_file:
        next(book_file)
        for id, line in enumerate(book_file, start=1):
            title, author, year = line.strip().split(',')

            if title == search_title:
                print(f"{id}. {title} ({author}) - {year}")
                found = True

        if not found:
            print(f"`{search_title}` is not found!")


def update_book():
    search_title = input("Enter the book title: ")
    found = False
    books = []
    with open(BOOK_FILE) as book:
        next(book)
        for line in book:
            title, _, _ = line.strip().split(',')
            data = line

            if title == search_title:
                new_title, new_author, new_year = input_book()
                data = f"{new_title},{new_author},{new_year}\n"
                found = True
            books.append(data)
    if not found:
        print(f'`{search_title}` is not found!')
    else:
        with open(BOOK_FILE, 'w') as book_file:
            book_file.write("Title,Author,Year\n")
            book_file.writelines(books)


def remove_book():
    search_title = input("Enter the book title: ")
    books = []
    with open(BOOK_FILE) as book:
        next(book)
        for line in book:
            title, _, _ = line.strip().split(',')
            if title != search_title:
                books.append(line)
    
    with open(BOOK_FILE, 'w') as book_file:
        book_file.write("Title,Author,Year\n")
        book_file.writelines(books)

def mark_book():
    search_title = input("Enter the book title: ")
    found = False
    books = []
    with open(BOOK_FILE) as book:
        next(book)
        for line in book:
            title, author, year = line.strip().split(',')
            data = line

            if title == search_title:
                data = f"{title}(read), {author}, {year}\n"
                found = True
            books.append(data)
    if not found:
        print(f'`{search_title}` is not found!')
    else:
        with open(BOOK_FILE, 'w') as book_file:
            book_file.write("Title,Author,Year\n")
            book_file.writelines(books)
    


# The main function of the program. It is the first thing that runs when the program is executed.
choice = int(input(MENU))

operations = (add_book, return_all_book, search_book, update_book, remove_book, mark_book)

while choice != 7:
    if choice in range(1, len(operations) + 1):
        operations[choice - 1]()
    else:
        print("Invalid choice. Please try again.")
    print()
    choice = int(input(MENU))