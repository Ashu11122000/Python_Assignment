# Open a file named "sample.txt" in write mode ("w")
# If the file does not exist, it will be created
# If it already exists, its old content will be overwritten
file = open("sample.txt", "w")  

# Ask the user to enter some text
# input() takes user input as a string
text = input("Enter some text to write into file: ")  

# Write the user-entered text into the file
# write() stores the text inside the file
file.write(text)  

# Close the file after writing
# Closing is important to save changes and free system resources
file.close()  

# Open the same file again, but now in read mode ("r")
# This allows us to read the content stored in the file
file = open("sample.txt", "r")  

# Read the entire content of the file
# read() returns all text from the file as a string
content = file.read()  

# Print a message before showing file content
print("File content is:")  

# Display the content read from the file
print(content)  

# Close the file after reading
# Always close file after operations to avoid memory/resource issues
file.close()  