class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"'{self.title}' by {self.author}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            book.display_info()


# Usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library = Library("City Library")
library.add_book(book1)
library.add_book(book2)

library.display_books()

# Books can exist independently
book1.display_info()
