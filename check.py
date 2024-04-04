# Define a class named 'checkout_management'
class checkout_management:
    checkouts = []    # Initialize an empty list called 'checkouts' as a class attribute

 # Define a method named 'checkout_book' that takes three parameters
    
    def checkout_book(self,user_id, isbn):
        return self.checkouts.append({"user_id": user_id, "isbn": isbn})  # Updated list of checkouts including the newly checked-out book.
