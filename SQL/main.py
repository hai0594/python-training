from project import function as func
import pymssql

MENU = """Enter
'a' - add a book
'l' - list books
'd' - delete book
'u' - update book
'q' - quit
your choice: """

operations = {
    'a': func.insert_book_table,
    'l': func.get_all_books,
    'd': func.delete_book,
    'u': func.update_book
}

func.create_book_table()
user_choice = input(MENU).lower()

while user_choice != 'q':

    if user_choice in operations:
        operations[user_choice]()
    else:
        print("Invalid command, please try again!")

    user_choice = input(MENU).lower()
