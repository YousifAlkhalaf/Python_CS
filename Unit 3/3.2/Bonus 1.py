# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:34:13 2021

@author: Computer Science ~ B
"""
import random
import math
loop = 1000000
counter = 0
for i in range(0, loop, 1):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    hyp = math.pow(x, 2) + math.pow(y, 2)
    hyp = math.sqrt(hyp)
    if hyp <= 1:
        counter += 1
     
print(f'Total points inside circle: {counter}')
print(f'Estimate for pi is {(counter/loop) * 4}')