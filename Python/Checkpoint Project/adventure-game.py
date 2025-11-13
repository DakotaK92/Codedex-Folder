# Terminal Adventure Game

import time

def print_pause(message, delay=1.5):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You find yourself in a dark forest.")
    print_pause("Rumors say that a treasure is hidden somewhere nearby.")
    print_pause("You see a path to the left and a cave to the right.")

def choose_path():
    print_pause("Where do you want to go?")
    choice = ""
    while choice not in ["1", "2"]:
        print("Enter 1 to go down the forest path.")
        print("Enter 2 to enter the dark cave.")
        choice = input("What do you choose? (1 or 2): ")
    return choice

def forest():
    print_pause("You walk down the forest path.")
    print_pause("Suddenly, a wild wolf appears!")
    action = ""
    while action not in ["1", "2"]:
        print("Enter 1 to fight the wolf.")
        print("Enter 2 to run back.")
        action = input("What do you do? (1 or 2): ")
    if action == "1":
        print_pause("You try to fight the wolf...")
        print_pause("The wolf overpowers you! You run back to safety.")
        forest()  # go back to forest choice
    else:
        print_pause("You safely run back to the starting point.")
        start_game()

def cave():
    print_pause("You enter the dark cave cautiously...")
    print_pause("You find a treasure chest filled with gold!")
    print_pause("Congratulations, you win!")

def start_game():
    intro()
    choice = choose_path()
    if choice == "1":
        forest()
    elif choice == "2":
        cave()

# Start the game
start_game()
