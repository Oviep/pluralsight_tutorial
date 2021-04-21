import random

roll_dice = random.randrange(1, 6)
guess = int(input("Guess the dice roll: \n"))

if guess == roll_dice:
    print("Congratulations you rolled a " + str(roll_dice))
else:
    print("Wrong. They rolled a " + str(roll_dice))



