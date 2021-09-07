# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:08:58 2021

@author: Computer Science ~ B
"""
import math
import random

num = 3.5
num3 = math.pow(num, 3)

print('The number', num, 'raised to the 3rd power is', num3)
num += 2
num3 = math.pow(num, 3)
print('The number ' + str(num) + ' raised to the 3rd power is ' + str(num3))
num += 2
num3 = math.pow(num, 3)
print('The number {} raised to the 3rd power is {}'.format(num, num3))