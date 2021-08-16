from typing import List
from enum import Enum

from core import roll
from ironsworn import move, oracle

class Bond:
    name: str

class Debility(Enum):
    Wounded = 1
    Shaken = 2
    Unprepared = 3
    Encumbered = 4
    Maimed = 5
    Corrupted = 6
    Cursed = 7
    Tormented = 8

class Rank(Enum):
    Troublesome = 1,
    Dangerous = 2,
    Formidable = 3,
    Extreme = 4,
    Epic = 5

class Vow:
    name: str
    rank: Rank
    progress: int # max 40

class Character:
    # name
    name: str
    
    # stats    
    edge: int
    heart: int
    iron: int
    shadow: int
    wits: int
    
    # tracks
    health: int = 5
    spirit: int = 5
    supply: int = 5
    
    # momentum
    momentum: int = 2
    momentum_max: int = 10
    momentum_reset: int = 2
    
    # lists
    vows: List[Vow] = []
    bonds: List[Bond] = []
    debilities: set[Debility] = []
    
    # exp
    experience: int = 0

    def __init__(self) -> None:
        self.name = oracle.ironlander_names()
        self._roll_stats()
        print(self.__dict__)

    def _roll_stats(self):
        stats = ['edge', 'heart', 'iron', 'shadow', 'wits']
        self._roll_stat(stats, 3) # main
        self._roll_stat(stats, 2) # mid
        self._roll_stat(stats, 2) # mid
        self._roll_stat(stats, 1) # low
        self._roll_stat(stats, 1) # low
        
    def _roll_stat(self, stats: List[str], value: int):
        stat_index = roll.dice.custom(len(stats)) - 1
        self.__dict__[stats[stat_index]] = value
        stats.pop(stat_index)

    def roll_edge(self, bonus = 0):
        move.action(self.edge + bonus)

    def roll_heart(self, bonus = 0):
        move.action(self.heart + bonus)

    def roll_iron(self, bonus = 0):
        move.action(self.iron + bonus)

    def roll_shadow(self, bonus = 0):
        move.action(self.shadow + bonus)

    def roll_wits(self, bonus = 0):
        move.action(self.wits + bonus)