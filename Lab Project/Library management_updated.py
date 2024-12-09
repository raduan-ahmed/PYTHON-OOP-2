from abc import ABC, abstractmethod
import hashlib

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

# Authentication Class
class UserAuth:
    def __init__(self):
        self.users = {}  # Store usernames and hashed passwords

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def sign_up(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different username.")
        else:
            self.users[username] = self.hash_password(password)
            print("User signed up successfully!")

    def sign_in(self, username, password):
        if username in self.users and self.users[username] == self.hash_password(password):
            print("Sign-in successful. Welcome from (Raduan,Riddi,Somoy,Sajib) to you!")
            return True
        else:
            print("Invalid username or password.")
            return False

# Main Function
def main():
    auth = UserAuth()
    library = Library()
    
    logged_in = False

    while True:
        print("\n--- Library Management System ---")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Add a Book (requires sign-in)")
        print("4. Add a Member (requires sign-in)")
        print("5. Borrow a Book (requires sign-in)")
        print("6. Return a Book (requires sign-in)")
        print("7. Search for a Book")
        print("8. Sort Books by Title (requires sign-in)")
        print("9. Display All Books")
        print("10. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                # Sign Up
                username = input("Enter username: ")
                password = input("Enter password: ")
                auth.sign_up(username, password)

            elif choice == "2":
                # Sign In
                username = input("Enter username: ")
                password = input("Enter password: ")
                logged_in = auth.sign_in(username, password)

            elif choice == "3":
                # Add a Book
                if logged_in:
                    title = input("Enter book title: ")
                    author = input("Enter author name: ")
                    copies = int(input("Enter number of copies: "))
                    library.add_book(Book(title, author, copies))
                    print("Book added successfully!")
                else:
                    print("You must sign in to perform this action.")

            elif choice == "4":
                # Add a Member
                if logged_in:
                    name = input("Enter member name: ")
                    member_id = input("Enter member ID: ")
                    library.add_member(Member(name, member_id))
                    print("Member added successfully!")
                else:
                    print("You must sign in to perform this action.")

            elif choice == "5":
                # Borrow a Book
                if logged_in:
                    member_id = input("Enter member ID: ")
                    title = input("Enter book title: ")
                    member = next((m for m in library.members if m.member_id == member_id), None)
                    book = next((b for b in library.books if b.title.lower() == title.lower()), None)
                    if member and book:
                        member.borrow_book(book)
                    else:
                        print("Invalid member ID or book title.")
                else:
                    print("You must sign in to perform this action.")

            elif choice == "6":
                # Return a Book
                if logged_in:
                    member_id = input("Enter member ID: ")
                    title = input("Enter book title: ")
                    member = next((m for m in library.members if m.member_id == member_id), None)
                    book = next((b for b in library.books if b.title.lower() == title.lower()), None)
                    if member and book:
                        member.return_book(book)
                    else:
                        print("Invalid member ID or book title.")
                else:
                    print("You must sign in to perform this action.")

            elif choice == "7":
                # Search for a Book
                title = input("Enter book title to search: ")
                results = library.search_book(title)
                if results:
                    print("Search Results:")
                    for book in results:
                        book.display_info()
                else:
                    print("No books found with that title.")

            elif choice == "8":
                # Sort Books
                if logged_in:
                    library.sort_books()
                    print("Books sorted by title.")
                else:
                    print("You must sign in to perform this action.")

            elif choice == "9":
                # Display All Books
                if library.books:
                    library.display_all_books()
                else:
                    print("No books available in the library.")

            elif choice == "10":
                # Exit
                print("Exiting the Library Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
