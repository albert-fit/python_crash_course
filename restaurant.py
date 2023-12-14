class Restaurant:
    """A class that describes a restaurant"""
    def __init__(self,name, type, numbers_served = 0):
        """Initialize name and type attribute"""
        self.name = name
        self.type = type
        self.number_served = numbers_served

    def describe(self):
        """Describe the restaurant based on name and type as well as modify number_served to match the argument"""
        print(f"The restaurant is called {self.name} and it serves {self.type}")
        print(f"{self.name.title()} served {self.number_served} customers today!")
    
    def open(self):
        """Announce that the restaurant is open"""
        print(f"{self.name.title()} is open")