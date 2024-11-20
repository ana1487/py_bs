import math
import random


# This part uses basic label to make user keep giving valid input
label = True

while label:
    user_input = int(input("Enter a valid choice for the game \n 1 for Rock \n 2 For Paper \n 3 for Sissor \n"))
    if user_input >= 1 and user_input <= 3:
        label = False
    else:
        print("You entered an invalid number choice. Please try again \n")


#Once the user gives a valid input, we now randomize the computer choice
computer_input = int(random.choice("123"))

# print(computer_input)
#In this part, I wanna compare the values of user_input and computer_input. Check if they chose the same inputs or different. And I want to make the logic for the winner.



#Compare inputs and determine winner
if user_input == computer_input:
    print("It's a draw!")
elif (user_input == 1 and computer_input == 3) or \
     (user_input == 2 and computer_input == 1) or \
     (user_input == 3 and computer_input == 2):
    print("You win! 👌")
else:
    print("Computer wins! 🤖")

#Show what each player chose
choices = {1: "Rock 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}
print(f"\nYou chose: {choices[user_input]}")
print(f"Computer chose: {choices[computer_input]}")
    
