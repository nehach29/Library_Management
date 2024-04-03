# Library_Management
The Library Management System is designed to automate and streamline the management of books and users in a library setting. The system is built using object-oriented programming principles and consists of multiple components/modules to handle various functionalities.
Components/Modules:
# model:

Purpose: Defines the foundational data models for books and users.
Entities Defined:
Book Class: Represents a book with attributes like title, author, and isbn.
User Class: Represents a user with attributes like name and user_id.
Key Features: Encapsulation of data and behavior, string representation for debugging and logging.

# manage_books:

Purpose: Manages the collection of books in the library.
Functionalities:
add_book(title, author, isbn): Adds a new book to the collection.
list_books(): Lists all the books in the collection.
Data Structure: Uses a list (books) to store dictionaries representing individual books.

# storage:

Purpose: Handles the storage and retrieval of book details using a CSV file.
Functionalities:
store_books(title, author, isbn): Stores the book details in a CSV file.
Data Storage: Stores book details in a CSV file named Logging.csv.

# checkout_management:

Purpose: Manages the checkout process of books to users.
Functionalities:
checkout_book(user_id, isbn): Checks out a book to a user.
Data Structure: Uses a list (checkouts) to store dictionaries representing individual checkouts.

# user_management:

Purpose: Manages the collection of users in the library.
Functionalities:
add_user(name, user_id): Adds a new user to the collection.
Data Structure: Uses a list (users) to store dictionaries representing individual users.

# main_menu & main:

Purpose: Provides the user interface to interact with the Library Management System.
Functionalities:
Displaying main menu options.
Handling user choices to perform corresponding actions like adding books, listing books, adding users, and checking out books.
