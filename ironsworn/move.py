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

def face_danger():
    print("""
When you attempt something risky or react to an imminent threat, envision your action and roll. If you act...
- With speed, agility, or precision: Roll +edge.
- With charm, loyalty, or courage: Roll +heart.
- With aggressive action, forceful defense, strength, or endurance: Roll +iron.
- With deception, stealth, or trickery: Roll +shadow.
- With expertise, insight, or observation: Roll +wits.

On a strong hit, you are successful. Take +1 momentum.

On a weak hit, you succeed, but face a troublesome cost. Choose one.
- You are delayed, lose advantage, or face a new danger: Suffer -1 momentum.
- You are tired or hurt: Endure Harm (1 harm).
- You are dispirited or afraid: Endure Stress (1 stress).
- You sacrifice resources: Suffer -1 supply.

On a miss, you fail, or your progress is undermined by a dramatic and costly turn of events. Pay the Price.""")

def secure_an_advantage():
    print("""
When you assess a situation, make preparations, or attempt to gain leverage, envision your action and roll. If you act...
• With speed, agility, or precision: Roll +edge.
• With charm, loyalty, or courage: Roll +heart.
• With aggressive action, forceful defense, strength, or endurance: Roll +iron.
• With deception, stealth, or trickery: Roll +shadow.
• With expertise, insight, or observation: Roll +wits.

On a strong hit, you gain advantage. Choose one.
• Take control: Make another move now (not a progress move); when you do, add +1.
• Prepare to act: Take +2 momentum.

On a weak hit, your advantage is short-lived. Take +1 momentum.

On a miss, you fail or your assumptions betray you. Pay the Price.
""")