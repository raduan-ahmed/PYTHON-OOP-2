from abc import ABC, abstractmethod
import copy

# Abstract Class - Library Item
class LibraryItem(ABC):
    @abstractmethod
    def display_info(self):
        pass

# Encapsulation - Book class
class Book(LibraryItem):
    def __init__(self, title, author, copies):
        self.__title = title
        self.__author = author
        self.__copies = copies

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def copies(self):
        return self.__copies

    @copies.setter
    def copies(self, value):
        if value < 0:
            raise ValueError("Copies cannot be negative.")
        self.__copies = value

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}")

# Member Class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append(book.title)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book: Book):
        if book.title in self.borrowed_books:
            book.copies += 1
            self.borrowed_books.remove(book.title)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def display_borrowed_books(self):
        print(f"{self.name} has borrowed: {', '.join(self.borrowed_books)}" if self.borrowed_books else "No books borrowed.")

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_member(self, member: Member):
        self.members.append(member)

    def search_book(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results

    def sort_books(self):
        self.books.sort(key=lambda book: book.title)

    def display_all_books(self):
        for book in self.books:
            book.display_info()

# Main Function
def main():
    library = Library()
    while True:
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
        print("1. Add a Book")
        print("2. Add a Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Search for a Book")
        print("6. Sort Books by Title")
        print("7. Display All Books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                # Add a Book
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                copies = int(input("Enter number of copies: "))
                library.add_book(Book(title, author, copies))
                print("Book added successfully!")

            elif choice == "2":
                # Add a Member
                name = input("Enter member name: ")
                member_id = input("Enter member ID: ")
                library.add_member(Member(name, member_id))
                print("Member added successfully!")

            elif choice == "3":
                # Borrow a Book
                member_id = input("Enter member ID: ")
                title = input("Enter book title: ")
                member = next((m for m in library.members if m.member_id == member_id), None)
                book = next((b for b in library.books if b.title.lower() == title.lower()), None)
                if member and book:
                    member.borrow_book(book)
                else:
                    print("Invalid member ID or book title.")

            elif choice == "4":
                # Return a Book
                member_id = input("Enter member ID: ")
                title = input("Enter book title: ")
                member = next((m for m in library.members if m.member_id == member_id), None)
                book = next((b for b in library.books if b.title.lower() == title.lower()), None)
                if member and book:
                    member.return_book(book)
                else:
                    print("Invalid member ID or book title.")

            elif choice == "5":
                # Search for a Book
                title = input("Enter book title to search: ")
                results = library.search_book(title)
                if results:
                    print("Search Results:")
                    for book in results:
                        book.display_info()
                else:
                    print("No books found with that title.")

            elif choice == "6":
                # Sort Books
                library.sort_books()
                print("Books sorted by title.")

            elif choice == "7":
                # Display All Books
                if library.books:
                    library.display_all_books()
                else:
                    print("No books available in the library.")

            elif choice == "8":
                # Exit
                print("Exiting the Library Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


