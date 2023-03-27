import json
"""
    It reads the file, skips the first line, then reads the rest of the lines, splits them on the comma,
    and then creates a dictionary from the header and the line
    """


def add_book():
    """
    It takes user input and writes it to a file.
    """
    Title = input("Title:")
    Author = input("Author:")
    Year = input("year:")
    book = f"{Title},{Author},{Year}\n"
    with open("books.csv", 'a') as file:
        file.write(book)


def return_all_book():
    """
    It reads the books.csv file and returns a json object of all the books in the file.
    :return: A list of dictionaries
    """
    book = []
    with open("books.csv", 'r') as file:
        header = next(file).strip().split(',')
        for line in file:
            line = line.strip().split(',')
            book.append(dict(zip(header, line)))
        books = json.dumps(book, indent=4)
        return books


def search_book():
    """
    It takes a book title as input, loads the JSON data from the return_all_book() function, and then
    loops through the data to find the book with the matching title
    """
    search_title = input("Enter the book tile:")
    all_book = json.loads(return_all_book())
    for books in all_book:
        if books['Title'] == search_title:
            print(books)


# The main function of the program. It is the first thing that runs when the program is executed.
print("welcome to the program")
print("Please choose an option:")
print("1. Add new books")
print("2. show list books")
print("3. search books")
print("4. quit")
choice = 0

while choice != 4:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_book()
    elif choice == 2:
        print(return_all_book())
    elif choice == 3:
        search_book()
    else:
        print("Invalid choice. Please try again.")
