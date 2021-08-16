import core.dice
from typing import List

def roll_table(table: List[str]):
    dice_roll = core.dice.roll_dice(len(table) - 1)
    return table[dice_roll]
