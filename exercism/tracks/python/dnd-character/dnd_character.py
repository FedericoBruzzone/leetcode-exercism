import random
import math

def generator_random():
    while True:
        yield random.randrange(1, 7)

def modifier(score):
    if type(score) == int:
        return (score - 10) // 2
    return 0

class Character:
    strength: int = 0
    dexterity: int = 0
    constitution: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0
    hitpoints: int = 0

    def __init__(self): 
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        G = generator_random()
        return sum(sorted([next(G) for i in range(4)])[1:])