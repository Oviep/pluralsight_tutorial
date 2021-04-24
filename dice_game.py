import random


def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total


def main():
    player1 = input('Enter player one\'s name \n')
    player2 = input('Enter player two\'s name \n')

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if player1 > player2:
        print(player1, 'wins!')
    elif player2 > player1:
        print(player2, 'wins!')
    else:
        print('TIE!')


main()
