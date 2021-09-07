# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:08:15 2021

@author: Computer Science ~ B
"""

num = int(input('Enter a positive integer: '))
i1 = 1
i2 = 1

while 5*i1 <= num or 12*i2 <= num:
    if 5*i1 < 12*i2:
        print(5*i1)
        i1 += 1
    if 5*i1 > 12*i2:
        print(12*i2)
        i2 += 1