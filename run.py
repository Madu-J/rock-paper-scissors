import random

print("Welcome to Game box!")
# Let player choose if they want to play or quit
player = input("Do you want to play Rock, Paper, Scissors Game? ")
print()
# Check If user condition is true. If yes then play else quit
if player.lower() != "yes":
    quit()
else:
    print("Here is the rules for the game ")

choose = ("rock", "paper", "scissors")
player = None
computer = random.choice(choose)

while player not in choose:
    player = input("Make a choice (rock, paper, scissors): ")

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
else:
    print("You lose!")
