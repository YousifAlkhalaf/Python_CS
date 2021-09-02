# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 13:26:20 2021

@author: Computer Science ~ B
"""

for column in range (1, 11, 1):
    for row in range (1, 11, 1):
        num = column * row
        print(f'{num:>3}', end = ' ')
    print('')