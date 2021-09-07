# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:31:47 2021

@author: Computer Science ~ B
"""

import math

weight = float(input('Enter weight (in pounds): '))
distance = float(input('Enter the distance (in miles): '))
rate =  float

if weight <= 2:
    rate = 1.10
elif weight <= 6:
    rate = 2.20
elif weight <= 10:
    rate = 3.70
else:
    rate = 3.80
    
charge_count = float(math.ceil(distance/500))
cost = float(charge_count * rate)
cost = format(cost, '.2f')

print('Shipping cost = ${}'.format(cost))