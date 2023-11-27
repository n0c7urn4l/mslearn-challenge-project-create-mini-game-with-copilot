#write a rock paper scissors game to play with the computer
#the computer should choose randomly
#the user should choose rock, paper, or scissors
#the user should be able to quit with q
#if the user wins, print out "you win"
#if the computer wins, print out "you lose"
#if it's a tie, print out "tie"

import random
import sys
print("Welcome to Rock, Paper, Scissors!")
print("Please choose either rock, paper, scissors or quit with q.")
user = input("Please choose: ")
while True:
    if user == "q":
        print("You have chosen to quit.")
        sys.exit()
    elif user == "rock":
        print("You have chosen rock.")
        break
    elif user == "paper":
        print("You have chosen paper.")
        break
    elif user == "scissors":
        print("You have chosen scissors.")
        break
    else:
        print("Invalid choice.")
        user = input("Please choose again: ")
comp = random.randint(1,3)
if comp == 1:
    print("The computer has chosen rock.")
elif comp == 2:
    print("The computer has chosen paper.")
else:
    print("The computer has chosen scissors.")
if user == "rock" and comp == 1:
    print("It's a tie!")
elif user == "rock" and comp == 2:
    print("You lose!")
elif user == "rock" and comp == 3:
    print("You win!")
elif user == "paper" and comp == 1:
    print("You win!")
elif user == "paper" and comp == 2:
    print("It's a tie!")
elif user == "paper" and comp == 3:
    print("You lose!")
elif user == "scissors" and comp == 1:
    print("You lose!")
elif user == "scissors" and comp == 2:
    print("You win!")
elif user == "scissors" and comp == 3:
    print("It's a tie!")
