# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:28:48 2021

@author: Computer Science ~ B
"""

num = int(input('Enter an integer: '))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10

print(f'Sum is {sum}')