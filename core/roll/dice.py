import random

def custom(n: int):
    return random.randint(1, n)

def d4():
    return custom(4)

def d6():
    return custom(6)

def d8():
    return custom(8)

def d10():
    return custom(10)

def d12():
    return custom(12)
    
def d20():
    return custom(20)

def d100():
    return custom(100)