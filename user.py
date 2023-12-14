class User:
    """A simple class describing a user"""
    def __init__(self, first_name, last_name):
        """Initialise first and last name attributes"""
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        """Describes the user"""
        print(f"The user is {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        """Greet the user"""
        print(f"Welcome back {self.first_name.title()} {self.last_name.title()}")