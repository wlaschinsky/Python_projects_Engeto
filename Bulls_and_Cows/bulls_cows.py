"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Samuel Wlaschinsky

email: wlaschinsky.samuelr@gmail.com
email_2: samuel.wlaschinsky@daktela.com

discord: samuel_qa

"""

import random

def generate_secret_number():
    """
    Generates a random 4-digit number where:
    - The first digit is a number between 1 and 9 (to avoid starting with 0).
    - The remaining three digits are unique numbers between 0 and 9, but not equal to the first digit.

    Returns:
        Rrandomly generated 4-digit number.
    """
    first_digit = random.choice(range(1, 10))
    remaining_digits = random.sample([digit for digit in range(10) if digit != first_digit], 3)
    random_number = str(first_digit) + "".join(map(str, remaining_digits))
    
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
    """
    Validates the user's input to ensure it follows these rules:
    - The input contains only digits
    - The input is exactly 4 digits long
    - The input does not start with 0
    - All digits in the input are unique
    
    Returns:
        True if the input is valid, False otherwise.
    """
    
    if not user_input.isdigit():
        print("The input must contain only digits.")
        return False
    
    if len(user_input) != 4:
        print("The number must be exactly 4 digits.")
        return False

    if user_input[0] == '0':
        print("The number cannot start with 0.")
        return False
    
    if len(set(user_input)) != 4:
        print("The digits must be unique.")
        return False
    
    return True

def check_bulls_and_cows(secret_number, user_guess):
    """
    Compares the secret number with the user's guess and calculates:
    - Bulls: Number of digits that are correct and in the correct position
    - Cows: Number of digits that are correct but in the wrong position
    
    Args:
        secret_number (str): The secret number to be guessed.
        user_guess (str): The user's guess.
        
    Returns:
        The number of bulls and cows (bulls, cows).
    """
    
    bulls = 0
    cows = 0
    
    for digit in range(4):
        if user_guess[digit] == secret_number[digit]:
            bulls += 1  
        elif user_guess[digit] in secret_number:
            cows += 1   
    
    return bulls, cows

def play_bulls_and_cows():
    
    """
    Main function that runs the Bulls and Cows game:
    - Generates a secret number
    - Prompts the user for guesses
    - Validates each guess
    - Provides feedback with the number of bulls and cows
    - Ends when the user guesses the correct number
    """
    
    secret_number = generate_secret_number()
    welcome_message()
    
    attempts = 0
    guessed_correctly = False   
    
    while not guessed_correctly:
        user_guess = input("Enter your guess: ")
        attempts += 1
        
        if not validate_user_input(user_guess):
            continue    
        
        bulls, cows = check_bulls_and_cows(secret_number, user_guess)
        
        if bulls == 1:
            bull_text = "bull"  
        else:
            bull_text = "bulls"  
            
        if cows == 1:
            cow_text = "cow"  
        else:
            cow_text = "cows" 

        print(f"{bulls} {bull_text}, {cows} {cow_text}")
        
        if bulls == 4:
            guessed_correctly = True
            if attempts == 1:
             print(f"Correct! You've guessed the right number in {attempts} guess!")
            else:
                print(f"Correct! You've guessed the right number in {attempts} guesses!")

# Run the game
play_bulls_and_cows()


