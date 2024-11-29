import sys
import random
from enum import Enum

def playing_rps():

    class RPG(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3 

    player_choice = input("\nEnter \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    if player_choice not in ["1", "2", "3"]:
        print('You must enter 1, 2 or 3')
        return playing_rps()
    
    player_chose = int(player_choice)

    computer_choice = random.choice("123")

    computer_chose = int(computer_choice)

    print("\nYou chose"+ str(RPG(player_chose)).replace('RPG.','').title()+'.')
    print("Python chose " + str(RPG(computer_chose)
                                ).replace('RPG.', '').title() + ".\n")

    #Compare inputs and determine winner
    if player_chose == computer_chose:
        print("It's a draw!")
    elif (player_chose == 1 and computer_chose == 3) or \
        (player_chose== 2 and computer_chose == 1) or \
        (player_chose== 3 and computer_chose == 2):
        print("You win! 👌")
    else:
        print("Computer wins! 🤖")

    print("\nPlay again?")

    while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

    if playagain.lower() == "y":
        return playing_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


playing_rps()
