#!usr/bin/env python3
# Made by Maximiliano Fairman
# Created on oct 16th 2025
# this program is a

import random  # used to generate a random number

# Ask the user to guess
guess = int(input("Guess a number between 0 and 9: "))
secret_number = random.randint(0, 9)  # generates a random number between 0 and 9
# If the guess is correct
if guess == secret_number:
    print("You guessed correctly!")

# If the guess is incorrect
else:
    print("You guessed wrong")
