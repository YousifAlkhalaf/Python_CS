# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 13:37:55 2022

@author: Computer Science ~ B
"""

class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name}, age {self.age}'

print(Pet('Turtle', 5))
print(Pet('Hedwig', 3))
print(Pet('Wilbur', 2))
