import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Choose between rock, paper and scissors\n")
if computer_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You Win")
elif user_choice == "paper" and computer_choice == "rock":
    print("You Win")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win")
else:
    print("You lose")
