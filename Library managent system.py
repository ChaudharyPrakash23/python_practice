class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    # Add a book
    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1
        print(f'"{book}" added successfully.')

    # Print all books
    def show_books(self):
        if self.no_of_books == 0:
            print("Library is empty.")
        else:
            print("\nBooks in Library:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    # Get total number of books
    def get_no_of_books(self):
        print(f"\nTotal Books: {self.no_of_books}")


# Creating Library Object
library = Library()

# Adding Books
library.add_book("Python Programming")
library.add_book("Java Programming")
library.add_book("Data Structures")

# Display Books
library.show_books()

# Display Number of Books
library.get_no_of_books()