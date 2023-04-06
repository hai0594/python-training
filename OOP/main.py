import csv
import os


class book_store:
    def __init__(self):
        self.books = []
        self.filename = 'books.csv'

        if not os.path.isfile(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['title', 'author', 'year'])
                writer.writeheader()

    def add_book(self, title, author, year):
        try:
            with open(self.filename, mode='a', newline='') as file:
                write = csv.writer(file)
                write.writerow([title, author, year])
        except Exception as e:
            print(e)

    def show_book(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                next(file)
                for row in reader:
                    title, author, year = row
                    print(f"{title} - ({author}) {year}")
        except Exception as e:
            print(e)

    def update_book(self, search, title_n, author_n, year_n):
        try:
            data = [title_n, author_n, year_n]
            found = False
            books = []
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for title, author, year in reader:
                    if title == search:
                        found = True
                books.append(data)
            if not found:
                print(f'`{search}` is not found!')
            else:
                with open(self.filename, mode='w', newline='') as bookfile:
                    write = csv.writer(bookfile)
                    write.writerow(['title', 'author', 'year'])
                    write.writerows(books)

        except Exception as e:
            print(e)

    def delete_book(self, search):
        try:
            found = False
            books = []
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for lines in reader:
                    title, author, year = lines
                    if title != search:
                        found = True
                        books.append(lines)
                    if search not in reader:
                        print(f'`{search}` is not found!')

            with open(self.filename, mode='w', newline='') as bookfile:
                write = csv.writer(bookfile)
                write.writerow(['title', 'author', 'year'])
                write.writerows(books)

        except Exception as e:
            print(e)


book_store = book_store()
book_store.add_book('The Odyssey', 'Homer', 800)
# book_store.add_book('The Great Gatsby', 'F. Scott Fitzgerald', 1925)
book_store.update_book('The Great Gatsby', 'a', 'b', 'c')
