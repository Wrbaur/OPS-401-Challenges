#!/usr/bin/env python3
# Script: Ops 401 
# Class 16 challenge
# Authur: Will B. with the help of ChatGPT
# Date: 1/29/2024
# Resources Google, Bard, ChatGPT

# Automated Brute Force Wordlist Attack Tool Part 1 of 3
    # Create 2 Modes Offensive and defensive

# Import necessary libraries
import time  # For adding delay

# Function for Offensive mode: Dictionary Iterator
def offensive_mode():
    # Open the specified word list file (rockyou.txt)
    with open('rockyou.txt', 'r', errors='ignore') as file:
        # Iterate through each line in the file
        for line in file:
            # Remove leading/trailing whitespaces and assign the word to a variable
            word = line.strip()
            # Add a delay between words to mimic an iterator
            time.sleep(1)
            # Print the current word to the screen
            print(word)

# Function for Defensive mode: Password Recognized
def defensive_mode(user_input):
    # Open the specified word list file (rockyou.txt)
    with open('rockyou.txt', 'r', errors='ignore') as file:
        # Create a list of words from the file, removing leading/trailing whitespaces
        word_list = [line.strip() for line in file]

    # Check if the user input string is in the word list
    if user_input in word_list:
        # Print a message indicating the string is in the word list
        print(f"{user_input} is in the word list.")
    else:
        # Print a message indicating the string is not in the word list
        print(f"{user_input} is not in the word list.")

# Main function
def main():
    # Prompt the user to select a mode
    mode = int(input("Select mode:\n1. Offensive; Dictionary Iterator\n2. Defensive; Password Recognized\nEnter mode (1 or 2): "))

    if mode == 1:
        # Offensive mode: Dictionary Iterator
        # Call the offensive mode function
        offensive_mode()
    elif mode == 2:
        # Defensive mode: Password Recognized
        # Prompt the user for a string to check
        user_input = input("Enter a string to check: ")
        # Call the defensive mode function with the user input
        defensive_mode(user_input)
    else:
        # Print a message for an invalid mode
        print("Invalid mode. Exiting.")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()