# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:25:58 2022

@author: Computer Science ~ B
"""

def common_factors(num1, num2):
    factor_set = set()
    for i in range (2, max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            factor_set.add(i)
    return factor_set

num1 = int(input('Input first number: '))
num2 = int(input('Input second number: '))

print(f'The common factors of {num1} and {num2} are {common_factors(num1, num2)}')