import random

print("[Rock - Paper - Scissor] Game : ")
print()

# Available options
options = ["rock", "paper", "scissor"]

# User input
user = input("Enter your choice (Rock / Paper / Scissor): ").lower()

# Validate user input
if user not in options:
    print("<-------------------------------------------------->")
    print("Invalid choice! Please enter Rock, Paper, or Scissor")
    print("<-------------------------------------------------->")
    exit()

# Computer random choice
computer = random.choice(options)

print("\n You choosed   : ", user.capitalize())
print("Computer choosed : ", computer.capitalize(), "\n")

# Game Logic
if user == computer:
    result = "Draw"

elif (user == "rock" and computer == "scissor"):
    result = "You Win!"

elif (user == "scissor" and computer == "paper"):
    result = "You Win!"

elif (user == "paper" and computer == "rock"):
    result = "You Win!"

else:
    result = "Computer Wins!"

# Final Result
print("Result:", result)
