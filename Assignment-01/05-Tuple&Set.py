books = (
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)
tags = {"classic", "dystopian", "novel", "literature"}

# a_ Access the second book's author
second_book_author = books[1][1]
print(f"Author of the second book: {second_book_author}")

# b_Add a new record for "Brave New World" by Aldous Huxley, published in 1932
new_book = ("Brave New World", "Aldous Huxley", 1932)
books = books + (new_book,)
print("\nUpdated books tuple:")
print(books)

# c_Unpack the details of the third book
title, author, year = books[2]
print(f"\nDetails of the third book:\nTitle: {title}\nAuthor: {author}\nYear: {year}")

# d_ Loop through the books tuple and print each book's title
print("\nBook Titles:")
for book in books:
    print(book[0])

# e_Add a new tag "sci-fi" to the tags set
tags.add("sci-fi")
print("\nUpdated tags set:")
print(tags)

# f_ Remove the tag "novel" from the tags set
tags.discard("novel")
print("\nTags set after removing 'novel':")
print(tags)
