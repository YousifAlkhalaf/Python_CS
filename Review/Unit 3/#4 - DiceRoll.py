# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:13:40 2022

@author: Computer Science ~ B
"""
import random

def dieRoll() :
    return random.randint(1, 6)

roll = 0
number = 0
counter = 0

while number < 1 or number > 6:
    number = int(input('Enter a number from 1 to 6: '))

while number != roll:
    roll = dieRoll()
    print(f'I rolled a {roll}')
    counter += 1
print(f'It took {counter} roll(s) to get to your number!')
