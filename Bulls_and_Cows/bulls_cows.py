"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Samuel Wlaschinsky

email: wlaschinsky.samuelr@gmail.com
email_2: samuel.wlaschinsky@daktela.com

discord: samuel_qa

"""

import random

def generate_secret_number():
    # Create an empty string to store the result
    random_number = ""
    
    # Create a set to keep track of used digits
    used_digits = set()
    
    # Generate a random digit for the first position (it cannot be 0)
    first_digit = random.randint(1, 9)  
    random_number += str(first_digit)
    used_digits.add(first_digit) 
    
    # Generate the remaining 3 digits (can include 0, but must be unique)
    while len(random_number) < 4:
        digit = random.randint(0, 9) 
        
        # Check if the digit has already been used
        if digit not in used_digits:
            random_number += str(digit) 
            used_digits.add(digit)  
    
    print("This print is for debugging:" + " " + random_number)
    return random_number

def welcome_message():
    
    print("""
Hi there!
----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
    """)

def validate_user_input(user_input):
    
     # Check if the input contains only digits
    if not user_input.isdigit():
        print("The input must contain only digits.")
        return False
    
    # Check if the input is exactly 4 digits
    if len(user_input) != 4:
        print("The number must be exactly 4 digits.")
        return False
    
    # Check if the number does not start with 0
    if user_input[0] == '0':
        print("The number cannot start with 0.")
        return False
    
    
    # Check if the digits are unique
    if len(set(user_input)) != 4:
        print("The digits must be unique.")
        return False
    
    return True

def check_bulls_and_cows(secret_number, user_guess):
    bulls = 0
    cows = 0
    
    # Validate each input
    for digit in range(4):
        if user_guess[digit] == secret_number[digit]:
            
            # Right number in the right place
            bulls += 1  
            
        # Right number in the wrong place    
        elif user_guess[digit] in secret_number:
            cows += 1   
    
    return bulls, cows

def play_bulls_and_cows():
    
    # Generate a secret number
    secret_number = generate_secret_number()
    
    # Display the welcome message
    welcome_message()
    
    # Inicialization of variables
    attempts = 0
    
    # At the start of the game, the player has not guessed the number yet
    guessed_correctly = False   
    
    # Loop for the game to continue until the player guesses the number
    while not guessed_correctly:
        
        # Ask the player for a guess
        user_guess = input("Enter your guess: ")
        
        # Increase the number of (valid and invalid) attempts
        attempts += 1
        
        # Validate the user input
        if not validate_user_input(user_guess):
            
            # If the input is not valid, ask the player for another guess
            continue    
        
        # Count the number of bulls and cows
        bulls, cows = check_bulls_and_cows(secret_number, user_guess)
        
        # Define the text for the number of bulls
        if bulls == 1:
            bull_text = "bull"  
        else:
            bull_text = "bulls"  
            
        # Define the text for the number of cows
        if cows == 1:
            cow_text = "cow"  
        else:
            cow_text = "cows" 
            
    
        # # Define the text for the number of bulls and cows
        # bull_text = "bull" if bulls == 1 else "bulls"
        # cow_text = "cow" if cows == 1 else "cows"

        # Print the result
        print(f"{bulls} {bull_text}, {cows} {cow_text}")
        
        # If the player has guessed the number correctly
        if bulls == 4:
            guessed_correctly = True
            print(f"Correct! You've guessed the right number in {attempts} guesses!")

# Run the game
play_bulls_and_cows()


