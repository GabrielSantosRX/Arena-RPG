#!/usr/bin/python

from Battleground import Battleground
from Character import Character
from Weapon import Weapon

import unittest

class TestCharacter(unittest.TestCase):

    def setUp(self):
        sword = Weapon('Spartan Sword', 1, 20)
        bow = Weapon('Long Bow', 5, 60)
        
        self.leonidas = Character('King Leonidas', 10, sword, 200)
        self.legolas = Character('Elf Legolas', 5, bow, 100, 4)
        self.hulk = Character('Incredible Hulk', 100, None, 800, 2)
        
    def test_leonidas_alive(self):
        self.assertTrue(self.leonidas.alive())
        
    def test_leonidas_attack_hulk(self):
        self.leonidas.attack(self.hulk)
        self.assertEquals(self.hulk.hp, 770)
        
    def test_leonidas_has_weapon(self):
        assert self.leonidas.weapon != None
        
    def test_hulk_has_no_weapon(self):
        assert self.hulk.weapon == None
        
    def test_leonidas_cant_attack_legolas(self):
        self.legolas.move_to(0,5)
        self.assertFalse(self.leonidas.reachable(self.legolas))
        
    def test_legolas_can_attack_leonidas(self):
        self.legolas.move_to(0,5)
        assert (self.legolas.reachable(self.leonidas))
        
    def test_legolas_move(self):
        self.legolas.move_to(1,1)
        self.legolas.move_to(4,5)
        
        assert self.legolas.x == 4
        assert self.legolas.y == 5
        
if __name__ == '__main__':
    unittest.main()
