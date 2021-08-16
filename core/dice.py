import random

def roll_1d4():
    return roll_dice(4)

def roll_1d6():
    return roll_dice(6)

def roll_1d8():
    return roll_dice(8)

def roll_1d10():
    return roll_dice(10)

def roll_1d12():
    return roll_dice(12)
    
def roll_1d20():
    return roll_dice(20)

def roll_1d100():
    return roll_dice(100)

def roll_dice(dice: int):
    return random.randint(1, dice)