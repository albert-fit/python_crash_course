from user import User

class Privileges:
    """A simple class to represent Admin privileges"""
    def __init__(self, privileges = ['can add post', 'can edit post', 'can delete post', 'can ban user']):
        self.privileges = privileges
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"-{privilege}") 



class Admin(User):
    """An admin class that inheirits from User"""
    def __init__(self, first_name, last_name ):
        """Initialize attributes"""
        super().__init__(first_name, last_name )
        self.privileges = Privileges()