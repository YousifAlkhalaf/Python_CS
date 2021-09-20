# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:10:48 2021

@author: Computer Science ~ B
"""
import random

def get_roll(sides = 6, dice_num = 2):
    roll = 0
    for i in range (dice_num):
        n = random.randint(1, sides)
        roll += n
        print(f'Die {i + 1}: {n}')
    print(f'Roll total is {roll}\n')

print('Default values:\n')
for i in range(2):
    get_roll()
print('Two 10-sided dice:\n')
for i in range(2):
    get_roll(10)
print('5 standard dice:\n')
for i in range(2):
    get_roll(dice_num = 5)