#!/usr/bin/python

import math
from Weapon import Weapon

class Character:
    """ personagem porra """
    
    def __init__(self, name='undefined', power=0, weapon=None, hp=0, speed=1):
        self.name = name
        self.power = power
        self.weapon = weapon
        self.speed = speed
        self.hp = hp
        self.x = 0
        self.y = 0
        
    def damage(self):
        return (self.power + self.weapon.damage) if self.weapon != None else self.power
        
    def move_to(self, x, y):
        self.x = x
        self.y = y
        
    def alive(self):
        return (self.hp > 0)
        
    def attack(self, target):
        """ agride o alvo com uma arma """
        target.hp -= self.damage() if self.reachable(target) else 0
        
    def reachable(self, target):
        """ verifica se o alvo esta no alcance do personagem """
        return self.distance(target) <= (self.weapon.attack_range if self.weapon != None else 1)
        
    def distance(self, target):
        a = (self.x - target.x)**2
        b = (self.y - target.y)**2
        return math.sqrt(a + b)
        
