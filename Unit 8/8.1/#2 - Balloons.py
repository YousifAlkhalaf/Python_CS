# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 13:33:06 2022

@author: Computer Science ~ B
"""
import math

class Balloon(object):
    def __init__(self):
        self.radius = 0
    
    def inflate(self, amount):
        self.radius += amount
        
    def get_radius(self):
        return self.radius
    
    def get_volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

b1 = Balloon()
print(f'At the start:  balloon has radius {b1.get_radius()} and volume {b1.get_volume()}')
b1.inflate(1)
b1.inflate(2)
print(f'At point 2:  balloon has radius {b1.get_radius()} and volume {round(b1.get_volume(), 2)}')
b1.inflate(1)
b1.inflate(0.5)
print(f'At point 3:   balloon has radius {b1.get_radius()} and volume {round(b1.get_volume(), 2)}')
