# Define a class named 'manage_books'
class manage_books:
    
    books = []     # Initialize an empty list called 'books' as a class attribute

# Define a method named 'add_book' that takes  parameters: 'self', 'title', 'author', and 'isbn'
    
    def add_book(self,title, author, isbn):

        """
        Add a new book to the collection.
        
        Args:
            title (str): The title of the book to be added.
            author (str): The author(s) of the book to be added.
            isbn : The International Standard Book Number of the book to be added.
        """
        self.books.append({"title": title, "author": author, "isbn": isbn})
        
# Define a method named 'list_books' that takes only 'self' as a parameter
        
    def list_books(self):
        for book in self.books:
            print(book)      # Prints each book as a dictionary containing 'title', 'author', and 'isbn' keys.

# Define a class named 'checkout_management'
            
class checkout_management:
    checkouts = []    # Initialize an empty list called 'checkouts' as a class attribute

 # Define a method named 'checkout_book' that takes three parameters
    
    def checkout_book(self,user_id, isbn):
        return self.checkouts.append({"user_id": user_id, "isbn": isbn})   #  Updated list of checkouts including the newly checked-out book.

# Import the necessary modules
import csv
import os

# Define a class named 'storage'
class storage:

# Define a method named 'store_books' to store book details in a CSV file
    def store_books(self,title,author,isbn):
       
       file_name = r'C:\Users\nehaa\OneDrive\Desktop\codes\Logging.csv'     # Define the file path where the CSV file will be stored
       
       file_exists = os.path.isfile(file_name)   # # Check if the file already exists

 # Open the CSV file in append mode to add new records
       with open('Logging.csv','a',newline='') as f:
          fieldNames = ['Title','Author','ISBN']
          thewriter = csv.DictWriter(f=f,fieldnames=fieldNames)     # Create a DictWriter object to write dictionaries into the CSV file
         
# If the file does not exist, write the header with field names
          if not file_exists:
             thewriter.writeheader()

# Write a new row with the provided book details
          thewriter.writerow({
                'Title' : title,
                'Author' : author,
                'ISBN': isbn})
class user_management:
    users = []   # Initialize an empty list called 'users' as a class attribute
    
 # Define a method named 'add_user' to add a new user to the collection
    def add_user(self,name, user_id):
        return self.users.append({"name": name, "user_id": user_id})
