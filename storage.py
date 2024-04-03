# Import the necessary modules
import csv
import os
# Define a class named 'storage'
class storage:

# Define a method named 'store_books' to store book details in a CSV file
    def store_books(self,title,author,isbn):
       
       file_name = r'C:\Users\nehaa\OneDrive\Desktop\codes\Logging.csv'     # Define the file path where the CSV file will be stored

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