# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:58:21 2021

@author: Computer Science ~ B
"""

def increment_x(x):
    x += 1
    return x

x = 5
for i in range(5):
    x = increment_x(x)
    print(f'Round {i+1}: x is {x}')
