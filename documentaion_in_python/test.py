# math_operations.py
"""
This module provides basic mathematical operations: addition, subtraction, and multiplication.
Functions:
    add_numbers(a, b): Returns the sum of two numbers.
    subtract_numbers(a, b): Returns the difference between two numbers.
    multiply_numbers(a, b): Returns the product of two numbers.
"""
__author__ = 'pankaj'
__copyright__ = 'copy right 2024,Pankaj'

def add_numbers(a, b):
    """
    Add two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtract the second number from the first number.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference between the two numbers.
    """
    return a - b

def multiply_numbers(a, b):
    """
    Multiply two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b

x = 888 
y = 999

def main():
    num1 = 10
    num2 = 5

    print(f"The sum of {num1} and {num2} is: {add_numbers(num1, num2)}")
    print(f"The difference between {num1} and {num2} is: {subtract_numbers(num1, num2)}")
    print(f"The product of {num1} and {num2} is: {multiply_numbers(num1, num2)}")
    
if __name__ == "__main__":
    # Example usage of the functions
    main()
