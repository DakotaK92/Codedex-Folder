import random

# Mapping numbers to symbols
choices = {
    1: "✊",  # Rock
    2: "✋",  # Paper
    3: "✌️"   # Scissors
}

# Welcome message
print("===================")
print("Rock Paper Scissors")
print("===================")

# Player input
player = int(input("Pick a number: "))

# Validate input
if player not in choices:
    print("Invalid choice! Please choose 1, 2, or 3.")
else:
    # Computer random choice
    computer = random.randint(1, 3)

    # Show choices
    print(f"You chose: {choices[player]}")
    print(f"CPU chose: {choices[computer]}")

    # Determine winner
    if player == computer:
        print("It's a tie!")
    elif (player == 1 and computer == 3) or \
        (player == 2 and computer == 1) or \
        (player == 3 and computer == 2):
        print("The player won!")
    else:
        print("The computer won!")
