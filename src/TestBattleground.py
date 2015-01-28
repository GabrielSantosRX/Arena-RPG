#!/usr/bin/python

from Battleground import Battleground
import unittest

class TestBattleground(unittest.TestCase):

    def setUp(self):
        self.arena = Battleground('Thunderdome', 20, 20)
        
    def test_arena(self):
        self.assertEqual(self.arena.name, 'Thunderdome')
        self.assertEqual(self.arena.width, 20)
        self.assertEqual(self.arena.height, 20)
        
if __name__ == '__main__':
    unittest.main()
