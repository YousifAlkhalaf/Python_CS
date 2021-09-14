# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:14:22 2021

@author: Computer Science ~ B
"""
import math

def find_circle_area(radius):
    return math.pi * math.pow(radius, 2)

area = round(find_circle_area(10), 2)
print(f'Area with radius 10 is {area}')
area = round(find_circle_area(5), 2)
print(f'Area with radius 5 is {area}')
area = round(find_circle_area(1), 2)
print(f'Area with radius 1 is {area}')