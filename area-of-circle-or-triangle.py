# Import the math module so we can use mathematical constants and functions (like pi)
import math  

# Ask the user to enter the shape name (circle or triangle)
# input() always returns a string
shape = input("Enter shape (circle/triangle): ")  

# Convert user input to lowercase using .lower()
# This helps handle inputs like "Circle", "CIRCLE", etc.
# Then check if the shape is "circle"
if shape.lower() == "circle":  
    
    # Ask user to enter radius and convert it to float
    # float() is used because radius can be a decimal number
    radius = float(input("Enter radius of the circle: "))  
    
    # Calculate area of circle using formula: π × r²
    # math.pi gives value of π (3.14159...)
    # radius * radius is same as radius squared
    area = math.pi * radius * radius  
    
    # Print the result
    # Comma automatically adds space between text and value
    print("Area of the circle is:", area)  

# Check if the user selected "triangle"
elif shape.lower() == "triangle":  
    
    # Ask user to enter base and convert to float
    base = float(input("Enter base of the triangle: "))  
    
    # Ask user to enter height and convert to float
    height = float(input("Enter height of the triangle: "))  
    
    # Calculate area using formula: 1/2 × base × height
    # 0.5 is used instead of 1/2
    area = 0.5 * base * height  
    
    # Print the result
    print("Area of the triangle is:", area)  

# If user enters anything other than circle or triangle
else:  
    
    # Show error message to guide user
    print("Invalid shape selected!")  