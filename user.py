class user_management:
    users = []   # Initialize an empty list called 'users' as a class attribute
    
 # Define a method named 'add_user' to add a new user to the 'users' list
    def add_user(self,name, user_id):
        return self.users.append({"name": name, "user_id": user_id})
