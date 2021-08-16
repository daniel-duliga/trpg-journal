from core import roll

def action(modifier: int = 0):
    challenge1 = roll.d10()
    challenge2 = roll.d10()
    action = roll.d6() + modifier
    
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