# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:07:16 2022

@author: Computer Science ~ B
"""
import math

def distance(x1, y1, x2 = 0, y2 = 0):
    '''Calculates distance from x1, y1, x2, and y2. y2 and x2 are = 0 by default'''
    height = abs(y2 - y1)
    length = abs(x2 - x1)
    distance = height ** 2 + length ** 2
    distance = math.sqrt(distance)
    return distance

print(distance(3, 2))
print(distance(1, 2, 3, 4))
print(distance(5, 6, 1))