# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:23:36 2021

@author: Computer Science ~ B
"""
import math

hypotenuse = float(input('Enter diagonal measurement, in inches: '))
height = hypotenuse / (math.sqrt(337) / 16)
width = hypotenuse / (math.sqrt(337) / 9)
height = round(height, 2)
width = round(width, 2)
print(f'The height is {height} inches')
print(f'The width is {width} inches')