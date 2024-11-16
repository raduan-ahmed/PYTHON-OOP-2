class LibraryBook:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self.__isbn = isbn
        self.status = "available"

    def get_ISBN(self):
        return f"{self.__isbn[:3]}-****-****-{self.__isbn[-3:]}"

    def borrow_book(self, borrower_name):
        self.status = "borrowed"
        print(f"The book '{self._title}' has been borrowed by {borrower_name}.")

    def _display_basic_info(self):
        print(f"Title: {self._title}, Author: {self._author}")


class DigitalLibraryBook(LibraryBook):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def display_info(self):
        self._display_basic_info()
        print(f"File Format: {self.file_format}")


# Create an instance of LibraryBook
book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")

# Display the masked ISBN
print(book.get_ISBN())

# Borrow the book
book.borrow_book("John Doe")

# Create an instance of DigitalLibraryBook
digital_book = DigitalLibraryBook("Digital Fortress", "Dan Brown", "9780440240860", "PDF")

# Display the book's basic and digital information
digital_book.display_info()
