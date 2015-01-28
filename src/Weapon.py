#!/usr/bin/python

class Weapon:
    """ Arma, objeto manual com o proposito de infligir dano """
    
    def __init__(self, name, attack_range, damage):
        self.name = name
        self.attack_range = attack_range
        self.damage = damage
