import random

playerCounterPoints = 0
computerCounterPoints = 0
hands = ["ROCK", "PAPER", "SCISSOR"]

print("Welcome to my rock-paper-scissor game!")

wannaPlay = print(input("Do you wanna play? (YES or NO): "))
playerHand = (input("Please choose ROCK or PAPER or SCISSOR: "))

if wannaPlay == "NO":
   print("OK, magby next time!")
   quit()
else:
    print("Allright, let's play!")

random_number = random.randint(0, 2)
computerHand = hands[random_number]
print("")

if playerHand == "ROCK" and computerHand == "PAPER":
    computerCounterPoints += 1
    print(f"You have chosen {playerHand} and the computer has chosen {computerHand}. You lose!")
elif playerHand == "ROCK" and computerHand == "ROCK":
    print(f"You have chosen {playerHand} and the computer has chosen {computerHand}. It's a tie!")
elif playerHand == "ROCK" and computerHand == "SCISSOR":
    playerCounterPoints += 1
    print(f"You have chosen {playerHand} and the computer has chosen {computerHand}. You win!")
elif playerHand == "PAPER" and computerHand == "ROCK":
    playerCounterPoints += 1
    print(f"You have chosen {playerHand} and the computer has chosen {computerHand}. You win!")
elif playerHand == "PAPER" and computerHand == "PAPER":
    print(f"You have chosen {playerHand} and the computer has chosen {computerHand}. It's a tie!")
elif playerHand == "PAPER" and computerHand == "SCISSOR":
    computerCounterPoints += 1
    print(f"You have chosen {playerHand} and the computer has chosen {computerHand}. You lose!")
elif playerHand == "SCISSOR" and computerHand == "ROCK":
    computerCounterPoints += 1
    print(f"You have chosen {playerHand} and the computer has chosen {computerHand}. You lose!")
elif playerHand == "SCISSOR" and computerHand == "SCISSOR":
    print(f"You have chosen {playerHand} and the computer has chosen {computerHand}. It's a tie!")
elif playerHand == "SCISSOR" and computerHand == "PAPER":
    playerCounterPoints += 1
    print(f"You have chosen {playerHand} and the computer has chosen {computerHand}. You win!")
else:
    print("Please enter you hand position in capital letters ans make sure it is spelled correctly. Thank you!")

