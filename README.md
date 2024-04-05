# Library_Management
The Library Management System is designed to automate and streamline the management of books and users in a library setting. The system is built using object-oriented programming principles and consists of multiple components/modules to handle various functionalities.

# Book.py File
# Class Define: ManageBooks
A class to manage the collection of books in a library.
# Attributes:
books: A list attribute initialized as an empty list to store dictionaries representing individual books. Each dictionary contains keys title, author, and isbn to store the respective details of a book.
# Methods:
add_book: A method to add a new book to the collection. It takes three parameters (title, author, isbn) representing the title, author(s), and ISBN of the book to be added. A dictionary with these details is appended to the books list.
list_books: A method to list all the books in the collection. It iterates over the books list and prints each book as a dictionary containing title, author, and isbn keys.

# Check.py File
# Class Define: CheckoutManagement
A class to manage the checkout process of books to users in a library.
# Attributes:
checkouts: A list attribute initialized as an empty list to store dictionaries representing individual checkouts. Each dictionary contains keys user_id and isbn to store the respective details of a checkout.
# Methods:
checkout_book: A method to checkout a book to a user. It takes two parameters (user_id, isbn) representing the ID of the user checking out the book and the ISBN of the book to be checked out. 
A dictionary with these details is appended to the checkouts list, representing the new checkout.

# Model.py File
The model.py file defines classes that represent the core data entities or objects within the application. These classes can include attributes and methods to manipulate and interact with the data.
By encapsulating the data structures and their behaviors within classes, the model.py file abstracts the underlying data complexities, making it easier to manage, maintain, and extend the data model as the application evolves.
Keeping the data modeling logic separate from the application's business logic and presentation layer promotes a clean separation of concerns, enhancing the code's readability, maintainability, and scalability.
The data model classes defined in the model.py file can be reused across different parts of the application or even in other projects, providing a consistent and unified representation of the data entities.

# Storage.py File
# Class Define: Storage
A class to manage the storage of book details in a CSV file.
# Methods:
store_books: A method defined in the Storage class to store book details in a CSV file. It takes three parameters (title, author, isbn) representing the title, author(s), and ISBN of the book to be stored. 
store_chekout: (user_id) The ID of the user performing the checkout.
isbn (str or int) The ISBN of the book being checked out.
Attempts to store the user ID and ISBN of a book checkout into a CSV file named 'Checkout.csv'.
# The method performs the following operations:
It uses the os.getcwd() function to get the current working directory (CWD) of the Python script.
The variable relative_path is assigned the current directory path where the Python script is running.
It will automatically return the current directory path.
It uses the os.path.join() function to construct an absolute file path by joining the relative_path (current directory path) with the filename 'Logging.csv'
Checks if the file already exists using os.path.isfile().
Opens the CSV file in append mode to add new records.
Creates a DictWriter object to write dictionaries into the CSV file with specified field names (Title, Author, ISBN).
If the file does not exist, writes the header with field names using thewriter.writeheader().
Create separate CSV file which contains the Checkout details of the Books.
It uses the os.path.join() function to construct an absolute file path by joining the relative_path (current directory path) with the filename 'checkout.csv'
Checks if the file already exists using os.path.isfile().
Opens the CSV file in append mode to add new records.
Creates a DictWriter object to write dictionaries into the CSV file with specified field names (user_id, ISBN).

# User.py File
# Class Define: UserManagement
A class to manage the collection of users in a library.
# Attributes:
users: A list attribute initialized as an empty list to store dictionaries representing individual users. Each dictionary contains keys name and user_id to store the respective details of a user.
# Methods:
add_user: A method defined in the UserManagement class to add a new user to the collection. It takes two parameters (name, user_id) representing the name and ID of the user to be added. 
The method appends a dictionary containing these details to the users list and returns the updated list of users.

# Main.py File
This project is a Python-based command-line application for managing a library system. It allows users to add books, list available books, manage users, and check out books.
# main_menu()
Displays the main menu options for the Library Management System.
Options:
Add Book
List Books
Add User
Checkout Book
Exit
# Input Validation
Author's Name: Only alphabetic characters and spaces are allowed.
User ID: Only integer values are accepted.
