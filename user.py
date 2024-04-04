class user_Management:
    users = []  # Initialize an empty list called 'users' as a class attribute
    
    def add_user(self, name, user_id):
        """
        Add a new user to the collection.
        
        Args:
            name (str): The name of the user to be added.
            user_id (str): The ID of the user to be added.
            
        Returns:
            list: Updated list of users including the newly added user.
        """
        self.users.append({"name": name, "user_id": user_id})
        return self.users  # Return updated list of users including the newly added user.
