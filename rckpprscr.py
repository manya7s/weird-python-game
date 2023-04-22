import random

# Define the options for the game and their winning conditions
options = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# Ask for the player's name
player_name = input("What is your name? ")

# Initialize the player's score
score = {
    "wins": 0,
    "losses": 0,
    "ties": 0
}

while True:
    # Get the player's choice
    player_choice = input("{}, Choose rock, paper, or scissors: ".format(player_name)).lower()

    # Check that the player's choice is valid
    while player_choice not in options:
        print("Invalid choice, please choose rock, paper, or scissors.")
        player_choice = input("{}, Choose rock, paper, or scissors: ".format(player_name)).lower()

    # Generate a random choice for the computer
    computer_choice = random.choice(list(options.keys()))

    # Compare the player's choice to the computer's choice
    if options[player_choice] == computer_choice:
        result = "win"
        score["wins"] += 1
    elif options[computer_choice] == player_choice:
        result = "loss"
        score["losses"] += 1
    else:
        result = "tie"
        score["ties"] += 1
    # Print the results
    print("You chose {} and the computer chose {}. You {}!".format(player_choice, computer_choice, result))
    print("Your current score is {} wins, {} losses, {} ties".format(score["wins"], score["losses"], score["ties"]))
    choice = input("Do you want to continue? (yes/no) ")
    if choice.lower() == "no":
        break
print("Thanks for playing {}! Your final score was {} wins, {} losses, {} ties".format(player_name, score["wins"], score["losses"], score["ties"]))