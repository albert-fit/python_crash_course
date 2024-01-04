import pytest
from employee import Employee

@pytest.fixture
def employee():
    """An employee that will be available for all test functions."""
    employee = Employee(first_name = 'Joe', last_name = 'Doe', annual_salary=10000)
    return employee

def test_give_default_raise(employee):
    """A function that tests the default raise for an employee."""
    employee.give_raise()
    assert employee.annual_salary == 15000

def test_give_custom_raise(employee):
    """A function that tests the custom raise."""
    employee.give_raise(1000)
    assert employee.annual_salary == 11000