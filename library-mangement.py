# Create a class called Book
class Book:
    # Define the attributes for Book
    def __init__(self, title, author, year, availability):
        self.title = title
        self.author = author
        self.year = year
        self.availability = availability

    # Create a method to display book details
    def bookDisplay(self):
        print("Book title is:", self.title)
        print("Book author is:", self.author)
        print("Book publication year is:", self.year)
        print("Book availability is:", self.availability)

# Create a class called Patron
class Patron:
    # Store patron attributes
    def __init__(self, name, id, books_borrowed):
        self.name = name
        self.ID = id
        books_borrowed = []
        self.books_borrowed = books_borrowed

    # Create a method to manage a list of borrowed books
    def bookManager(self):
        interaction = input("Enter 'check out book' to check a book out, or 'view books' to see books: ").lower()
        if interaction == "check out book":
            check_out = input("Enter book title to check out: ")
            self.books_borrowed.append(check_out)
        elif interaction == "view books":
            print()
        else:
            print("are available")
            # Handle invalid inputs
            print("Invalid request")

# Create a class called Library
class Library:
    # Create a way to view or add books to the library
    def bookList(self, book1, book2, book3):
        books = [book1, book2, book3]
        task = input("Enter 'view' to see books, or 'add' to add a book: ").lower()
        if task == "view":
            print(books)
        elif task == "add":
            new_book = input("Enter book name: ")
            books.append(new_book)
        else:
            # Handle invalid inputs
            print("Invalid request")

    # Create a way to add patrons and track books
    def patronList(self):
        patrons = []
        interaction = input("Enter 'register' to register a new patron or 'exit' to exit program: ").lower()
        if interaction == "register":
            patron_name = input("Enter patron name: ")
            patrons.append(patron_name)
        elif interaction == "exit":
            print("Thank you")
        else:
            # Handle invalid inputs
            print("Invalid request")

nonfiction = Book("Python Learning", "Meet Patel", "2004", "Not Available")
nonfiction.bookDisplay()

user = Patron("Ethan", "00", "Python Learning")
user.bookManager()

LukasLibrary = Library
LukasLibrary.bookList("Python Learning", "HTML Mastery", "CSS Basics", "Understanding VMs")
LukasLibrary.patronList("Ethan")