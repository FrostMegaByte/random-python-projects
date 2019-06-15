from random import randint

# Generate computer guess
options = ["rock", "paper", "scissors"]
computerGuess = options[randint(0, 2)]

# Handle user input
while (True):
  userInput = input("Rock, paper or scissors (r, p, s)?\n")

  if (userInput.lower() in options + ["r", "p", "s"]):
    if (userInput == "r"):
      userInput = "rock"
    elif (userInput == "p"):
      userInput = "paper"
    else:
      userInput = "scissors"
    break
  else:
    print("Incorrect input. Please try again.\n")

print("Computer guessed:", computerGuess)

# Main logic
if (userInput == computerGuess):
  print("That's a tie")

elif (userInput == "rock"):
  if (computerGuess == "paper"):
    print("You lose...")
  else:
    print("You win!")

elif (userInput == "paper"):
  if (computerGuess == "scissors"):
    print("You lose...")
  else:
    print("You win!")

elif (userInput == "scissors"):
  if (computerGuess == "rock"):
    print("You lose...")
  else:
    print("You win!")