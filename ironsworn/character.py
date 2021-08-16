from ironsworn.bond import Bond
from ironsworn.vow import Vow
from ironsworn.debility import Debility

from typing import List

class Character:
    name: str
    edge: int
    heart: int
    iron: int
    shadow: int
    wits: int
    experience: int = 0
    health: int = 5
    spirit: int = 5
    supply: int = 5
    momentum: int = 2
    momentum_max: int = 10
    momentum_reset: int = 2
    bonds: List[Bond] = []
    vows: List[Vow] = []
    debilities: set[Debility] = []

    def __init__(self) -> None:
        self.name = input("Name")
        self.edge = input("Edge")
        self.heart = input("Heart")
        self.iron = input("Iron")
        self.shadow = input("Shadow")
        self.wits = input("Wits")
        print(self.__dict__)