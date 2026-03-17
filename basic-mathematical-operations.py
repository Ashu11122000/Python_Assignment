import math 

# Define function named "add" that takes two parameters: a and b
def add(a, b):  
    # Returns the sum of two numbers a and b
    return a + b

# Define function named "subtract" for subtraction of two numbers: a and b
def subtract(a, b): 
    # Returns the subtracted value from a and b 
    return a - b    

# Define function named multiply for multiplication of two numbers: a and b
def multiply(a, b):  
    # Returns the product of two numbers a and b
    return a * b  

# Define function named divide for division of two numbers: a and b
def divide(a, b):  
    # Check division by zero
    if b != 0:   
        # If b is not equals to 0 condition true, it returns the value by a/b
        return a / b  
    else:  
        # If b is 0, returns a message of "Cannot divide by zero"
        return "Cannot divide by zero!"  
    
# Define function named power to calculate the power: a^b
def power(a, b):
    # a raised to power b
    return a ** b

# Define a function named modulus to calculate remainder of two numbers: a and b
def modulus(a, b):
    # Returns remainder after division
    return a % b

# Define a function named floor_divison
def floor_division(a, b):
    if b!= 0:
        # Returns integer quotient
        return a // b
    else:
        return "Cannot divide by zero"
    
# Function named square_root to calculate the square root of a number
def square_root(a):
    if a>= 0:
        # Calculate the square root using math module
        return math.sqrt(a)
    else:
        return "Cannot find the square root of negative number"
    
# Function named absolute to calculate the absolute value of a number
def absolute(a):
    # Returns positive value
    return abs(a)

# Function named maximum to find the maximum of two numbers: a and b
def maximum(a, b):
    return max(a, b)

# Function named minimum to find the minimum of two numbers
def minimum(a, b):
    return min(a, b)

# Take two numbers as input from user
# Convert input into float data type for numeric operations
num1 = float(input("Enter first number: "))  
num2 = float(input("Enter second number: "))  

# Call functions and display results
print("Addition:", add(num1, num2))  
print("Subtraction:", subtract(num1, num2))  
print("Multiplication:", multiply(num1, num2))  
print("Division:", divide(num1, num2))  
print("Power:", power(num1, num2))  
print("Modulus:", modulus(num1, num2))  
print("Floor Division:", floor_division(num1, num2))  
print("Square Root:", square_root(num1))  
print("Absolute Value:", absolute(num2))  
print("Maximum:", maximum(num1, num2))  
print("Minimum:", minimum(num1, num2)) 
