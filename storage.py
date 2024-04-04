# Import the necessary modules
import csv
import os
# Define a class named 'storage'
class storage:

# Define a method named 'store_books' to store book details in a CSV file
    
    def store_books(self,title,author,isbn): 
       
       """
        Store book details in a CSV file.
        
        Args:
            title (str): The title of the book to be stored.
            author (str): The author(s) of the book to be stored.
            isbn : The International Standard Book Number of the book to be stored.
        """
       relative_path = os.getcwd()  # It will automatically return the current directory path
       file_name = os.path.join(relative_path, 'Logging.csv')  # It will join the relative_path with the logging.csv file.

# Check if the file already exists
       
       file_exists = os.path.isfile(file_name)

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
