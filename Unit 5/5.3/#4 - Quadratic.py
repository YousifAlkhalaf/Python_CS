# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:19:50 2021

@author: Computer Science ~ B
"""
import math

def quadratic(b, c, a = 1):
    x1 = 0.0
    x2 = 0.0
    if math.pow(b, 2) - (4 * a * c) < 0:
        print('No real solutions')
    else:
        x1 = (-b + math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
        if math.pow(b, 2) - (4 * a * c) == 0:
            print(f'One solution: {x1}')
        else:
            x2 = (-b - math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
            print(f'Two solutions: {x1} and {x2}')
    print()

quadratic(b=2, c=3)
quadratic(b = 2, c = -3)
quadratic(a = 2, b = 2, c = 0.5)