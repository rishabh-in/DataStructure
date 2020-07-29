## Given a dice that rolls 1 to 7. Simulate a 5 sided dice
from random import randint

def dice7():
    return randint(1, 7)

def convert7to5():

    roll_value = 7
    while roll_value > 5:
        roll_value = dice7()

    return roll_value

print(convert7to5())
