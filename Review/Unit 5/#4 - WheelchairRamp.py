# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:06:09 2022

@author: Computer Science ~ B
"""
import math

def findRampRun(height):
    return height
def findRampLength(height, length):
    length = height ** 2 + length ** 2
    length = math.sqrt(length)
    return length

height = float(input('Enter the height of the set of stairs, in inches: '))
length = findRampRun(height)
print('Minimum ramp run: {:.2f} ft'.format(length))
print('Minimum ramp length: {:.2f} ft'.format(findRampLength(height/12, length)))