# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:19:36 2021

@author: Computer Science ~ B
"""

def factorial(num):
    if num < 2:
        return 1
    else:
        return factorial(num - 1) * num

num = int(input('Enter a positive integer: '))
print(f'{num}! is {factorial(num)}')
    