import random
import string

# Function to generate a password based on user preferences
def passGenerator(length, num, sym):
    # Initialize character pool with uppercase and lowercase letters
    character = string.ascii_uppercase + string.ascii_lowercase
    
    # Add digits if the user wants numbers in the password
    if num == "yes":
        character += string.digits
    
    # Add symbols if the user wants symbols in the password
    if sym == "yes":
        character += string.punctuation
    
    # Generate password by randomly choosing characters from the pool
    password = "".join(random.choice(character) for _ in range(length))
    print("Generated Password:", password)

# Loop to keep generating passwords until user decides to exit
while True:
    try:
        # Get password length from user, ensuring it's a valid integer
        length = int(input("Enter password length: "))
        
        # Check if the password length is at least 8 characters
        if length < 8:
            print("Password should be at least 8 characters long")
            continue  # Ask again if length is too short
        
        # Get user preferences for including numbers and symbols
        num = input("Should the password have numbers (yes/no)? ").strip().lower()
        sym = input("Should the password have symbols (yes/no)? ").strip().lower()

        # Generate and print the password
        passGenerator(length, num, sym)

        # Ask if the user wants to generate another password
        con = input("\nDo you want to generate another password (yes/no)? ").strip().lower()
        if con != 'yes':
            print("Exiting... Goodbye! 👋")
            break  # Exit the loop if the user doesn't want another password
        
        print("\n") 

    except ValueError:
        # Handle non-numeric input for password length
        print("Invalid input! Please enter a number for password length.")
