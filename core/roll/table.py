from typing import List
from core import roll

def table(table: List[str]):
    dice_roll = roll.dice.custom(len(table)) - 1
    return table[dice_roll]