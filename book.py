# Global list to store books
# Define a class named 'manage_books'
class manage_books:
    
    books = []     # Initialize an empty list called 'books' as a class attribute

# Define a method named 'add_book' that takes three parameters: 'self', 'title', 'author', and 'isbn'
    
    def add_book(self,title, author, isbn):
        self.books.append({"title": title, "author": author, "isbn": isbn})
        
# Define a method named 'list_books' that takes only 'self' as a parameter
    def list_books(self):
        for book in self.books:
            print(book)     

