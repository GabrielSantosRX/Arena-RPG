#!/usr/bin/python

from Battleground import Battleground
from Character import Character
from Weapon import Weapon
from Battle import Battle

import unittest

class TestBattle(unittest.TestCase):

    def setUp(self):
        sword = Weapon('Spartan Sword', 1, 20)
        bow = Weapon('Long Bow', 5, 60)
        
        self.leonidas = Character('King Leonidas', 10, sword, 200)
        self.legolas = Character('Elf Legolas', 5, bow, 100, 4)
        self.hulk = Character('Incredible Hulk', 100, None, 800, 2)
        
        self.arena = Battleground('Thunderdome', 20, 20)
        self.battle = Battle(self.arena)
        
    def test_add_fighters_in_arena(self):
        self.battle.add_fighter(self.legolas, -5, -5)
        self.battle.add_fighter(self.leonidas, 10, 10)
        self.battle.add_fighter(self.hulk, 50, 50)
        
        assert self.legolas.x == 1
        assert self.legolas.y == 1
        
        assert self.leonidas.x == 10
        assert self.leonidas.y == 10
        
        assert self.hulk.x == 20
        assert self.hulk.x == 20
        
if __name__ == '__main__':
    unittest.main()
