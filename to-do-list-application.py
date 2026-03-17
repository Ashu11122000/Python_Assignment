# Create an empty list to store all tasks entered by the user
todo_list = []  

# Start an infinite loop so the program keeps running until user chooses to exit
while True:  
    
    # Display menu options to the user
    print("\n1. Add Task")   # Option 1 to add a new task
    print("2. View Tasks")   # Option 2 to see all tasks
    print("3. Remove Task") # Option 3 to delete a task
    print("4. Exit")        # Option 4 to stop the program
    
    # Take input from user for menu choice
    # input() returns a string, so we compare it with string values ("1", "2", etc.)
    choice = input("Enter your choice: ")  

    # If user selects option 1 (Add Task)
    if choice == "1":  
        
        # Ask user to enter a task name
        task = input("Enter task: ")  
        
        # Add the entered task to the list using append()
        todo_list.append(task)  
        
        # Confirm that task was added successfully
        print("Task added successfully!")  

    # If user selects option 2 (View Tasks)
    elif choice == "2":  
        
        # Check if the list is empty using len()
        if len(todo_list) == 0:  
            # If no tasks exist, show message
            print("No tasks in the list.")  
        else:  
            # If tasks exist, display heading
            print("Your Tasks:")  
            
            # Loop through the list using range() and len()
            # range(len(todo_list)) gives index values (0, 1, 2, ...)
            for i in range(len(todo_list)):  
                
                # Print task number (i+1) and task name
                # i+1 is used because list index starts from 0 but users expect 1-based numbering
                print(i + 1, ".", todo_list[i])  

    # If user selects option 3 (Remove Task)
    elif choice == "3":  
        
        # Ask user to enter task number to remove
        # Convert input to integer using int()
        task_num = int(input("Enter task number to remove: "))  
        
        # Check if entered number is valid
        # It must be greater than 0 and less than or equal to list length
        if 0 < task_num <= len(todo_list):  
            
            # Remove task using pop()
            # task_num - 1 is used because list index starts from 0
            removed = todo_list.pop(task_num - 1)  
            
            # Display which task was removed
            print("Removed task:", removed)  
        else:  
            # If invalid number entered, show error message
            print("Invalid task number!")  

    # If user selects option 4 (Exit)
    elif choice == "4":  
        
        # Print exit message
        print("Exiting program...")  
        
        # break stops the loop and ends the program
        break  

    # If user enters anything other than 1, 2, 3, or 4
    else:  
        
        # Show error message for invalid input
        print("Invalid choice! Please try again.")  