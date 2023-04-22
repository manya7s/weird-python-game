import random

# Generate a random number between 1 and 100
# The random.randint function generates a random integer between the given range (1 and 100 in this case)
number_to_guess = random.randint(1, 100)

# Get the player's name
# The input function allows the player to enter their name and assigns it to the variable "name"
name = input("What's your name? ")

# Start the game
# The .format method is used to insert the player's name into the welcome message
print("Welcome to the game, {}!".format(name))
print("I'm thinking of a number between 1 and 100. Can you guess it?")

# Ask the player to guess the number
# The input function is used to get the player's guess, and the int function is used to convert the guess to an integer
guess = int(input("Your guess: "))

# Keep track of the number of guesses
guesses = 1

# Keep looping until the player guesses the number
while guess != number_to_guess:
    if guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Your guess: "))
    guesses += 1

# Let the player know they won
# The .format method is used to insert the player's name and number of guesses into the winning message
print("Congratulations, {}! You guessed the number in {} tries!".format(name, guesses))