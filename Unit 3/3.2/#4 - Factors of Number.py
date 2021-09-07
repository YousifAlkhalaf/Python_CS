# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:25:41 2021

@author: Computer Science ~ B
"""

integer = int(input('Enter a positive integer: '))
print(f'The factors of {integer} are: ')
for i in range (1, integer+1, 1):
    if (integer%i == 0):
        print(i)