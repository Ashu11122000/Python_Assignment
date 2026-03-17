# Number Guessing Game

# Import random module to generate a random number
import random

# Generate a random number between 1 and 100
# randint(start, end) includes bot start and end values
number = random.randint(1, 100)

# Print welcome message for the user
print("Welcome to the Number Guessing Game!!")

# Tell user about the range of number
print("Select a number between 1 and 100")

# Initializes guess variable with 0 which is a starting value
guess = 0

# Initialize attempts counter to count number of tries
attempt = 0

# Start a loop that will continue until user guesses correct number
while guess != number:

    # Ask a user to enter a number
    #input() returns string, so we convert it into integer using int
    guess = int(input("Enter your guess:"))

    # Increase attempt count by 1 every time user guesses
    attempt = attempt + 1

    # Check if user's guess is smaller than the actual number
    if guess < number:
        # Inform user that guess is too small
        print("Too Low! Try again.")

    # Check if user's guess is greater than the actual number
    elif guess > number:
        # Inform user that guess is too high
        print("Too high! Try again.")
    
    # If user's guess is equal to the number
    else:
        # Congratulate the user
        print("Congratulations! You guessed the correct number.")

        # Show numbers of attempts taken
        print("You guessed it in", attempt, "attempt(s).")

# Ask user if they want to play again
play_again = input("Do you want to play again? (yes/no): ")

# Convert answer to lowercase for easy comparison
play_again = play_again.lower()

# Check user choice
if play_again == "yes":
    # Inform user to restart program manually
    print("Please run the program again to play.")
else:
    # Exit message
    print("Thank you for playing! Goodbye.")      