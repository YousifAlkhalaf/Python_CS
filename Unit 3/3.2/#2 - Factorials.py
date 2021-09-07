# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:34:00 2021

@author: Computer Science ~ B
"""

num = int(input('Enter a positive integer: '))
total = 0
factorial = 0
if num == 0:
    print('0! is 1')
else:
    for i in range(num, 0, -1):
        factorial += i

print(f'{num}! is {factorial}')
        