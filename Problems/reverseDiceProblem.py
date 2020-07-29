## Given a 5 sided dice, you have to convert it into 7 sided dice
from random import randint


def dice5():
    return randint(1, 5)

def convert5to7():
    while True:
        dice1 = dice5()
        dice2 = dice5()

        num = ((dice1 - 1) * 4) + (dice2)

        if num > 21:
            continue
        else:
            return num % 7 + 1
