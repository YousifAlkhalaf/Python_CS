# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:29:04 2022

@author: Computer Science ~ B
"""

def findCalories(num):
    return 300 * (num/4)

num = int(input('How many cookies did you eat? '))
print(f'You ate {findCalories(num)} calories2')