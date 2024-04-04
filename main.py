# Import necessary modules and classes

from models import manage_books, storage, checkout_management, user_management

# Define a function named 'main_menu' to display the main menu options

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Exit")
    choice = input("Enter choice: ")
    return choice

# Define the main function to run the library management system

def main():
    while True:
        choice = main_menu()
        # Check the user's choice and perform the corresponding actions
        if choice == '1':
            title = input("Enter title: ")

# For the Author's name we put one condition that the name of author should be only Alphabets other than that it will not work.
            
            while True:
                author = input("Enter author: ")
                if all(char.isalpha() or char.isspace() for char in author):
                    break
                else:
                    print("Please enter a valid author name containing only alphabetic characters and spaces.")

            #author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            manage_books().add_book(title, author, isbn)
            storage().store_books(title,author,isbn)


        elif choice == '2':
            manage_books().list_books()

# For the user_id it will only accept the integers values 
            
        elif choice == '3':
            name = input("Enter user name: ")
            while True:
                user_id = input("Enter user ID: ")
                if user_id.isdigit():
                    break
                else:
                    print("Please enter a valid integer user ID.")
            user_management().add_user(name, user_id)
            print("User added.")

        elif choice == '4':
            while True:
                user_id = input("Enter user ID: ")
                if user_id.isdigit():
                    break
                else:
                    print("Please enter a valid integer user ID.")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_management().checkout_book(user_id, isbn)
            print("Book checked out.")
    
# Check if the script is being run as the main program
            
if __name__ == "__main__":
    main()    # Call the 'main' function to start the library management system
