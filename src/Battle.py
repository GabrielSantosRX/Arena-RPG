#!/usr/bin/python

from Character import Character
from Battleground import Battleground

class Battle:
    """ Evento em um campo de batalha """
    
    def __init__(self, battleground):
        self.battleground = battleground
        self.fighters = []
        
    def add_fighter(self, character, x, y):
        self.fighters.append(character)
        self.move_fighter_to(character, x, y)
        
    def move_fighter_to(self, character, x, y):
        if x > self.battleground.width: x = self.battleground.width
        if y > self.battleground.height: y = self.battleground.height
        if x < 0: x = 1
        if y < 0: y = 1
        
        character.move_to(x, y)
