class Employee:
    """A class that stores employee details on name and salary"""

    def __init__(self, first_name, last_name, annual_salary):
        """Initiate the employee details"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, pay_increase=5000):
        self.annual_salary += pay_increase
    
