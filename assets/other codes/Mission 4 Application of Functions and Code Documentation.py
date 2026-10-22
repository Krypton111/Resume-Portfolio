# Function to do mathematical equations of 2 values

"""
The function written below accepts w numbers as arguments in which returns the value of the mathematical equations using the return function
"""
    
def math_thingz():
    num1 = float(input("Enter the first value: "))
    num2 = float(input("Enter the second value: "))
    addition = num1 + num2
    minus = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    return (addition, minus, multiplication, division)

# To greet user

"""
The function written below accepts the user's name as an argument and returns a greeting message
"""

def greet(name):
    return f"Hello, {name}."

# swap content of the 2 variables

"""
This function just simply swaps the content of the 2 variables
"""

def swap(a, b):
    a, b = b, a
    return (a, b)

# Test greet user
name = input("Enter your name: ")
print(greet(name))

# Test math_thingz
result = math_thingz()
print(f"addition: {result[0]}, minus: {result[1]}, multiplication: {result[2]}, division: {result[3]}")

# Test swap function
a = float(input("Enter the first variable value: "))
b = float(input("Enter the second variable value: "))
a, b = swap(a, b)
print(f"Swapped values: {a}, {b}")