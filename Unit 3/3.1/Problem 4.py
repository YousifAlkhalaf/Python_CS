# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 13:51:53 2021

@author: Computer Science ~ B
"""
i = 1
max = 0
while i <= 5:
    num = int(input('Enter an integer: '))
    if num > max:
        max = num
    i += 1
print(f'Max value is {max}')