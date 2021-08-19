# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:59:38 2021

@author: Computer Science ~ B
"""

import math

x1 = float(input('Enter the x-value of the first point: '))
y1 = float(input('Enter the y-value of the first point: '))
x2 = float(input('Enter the x-value of the second point: '))
y2 = float(input('Enter the y-value of the second point: '))

height = math.fabs(y2-y1)
width = math.fabs(x2-x1)

if height > width:
    print('Your rectangle is in portrait orientation!')
elif height < width:
    print('Your rectangle is in landscape orientation!')
else:
    print('Your rectangle is a square!')
