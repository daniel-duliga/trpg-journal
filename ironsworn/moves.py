from core import dice

def roll(modifier: int = 0):
    challenge1 = dice.roll_1d10()
    challenge2 = dice.roll_1d10()
    action = dice.roll_1d6() + modifier
    
    result = ""
    
    if (action > challenge1 and action > challenge2):
        result = "Strong hit"
        if (challenge1 == challenge2):
            result = f"{result} - Opportunity!"
    elif (action > challenge1 or action > challenge2):
        result = "Weak hit"
    else:
        result = "Miss"
        if (challenge1 == challenge2):
            result = f"{result} - Complication!"
    
    result = f"{result} ({action} vs. {challenge1}, {challenge2})"
    
    print(result);