# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:48:07 2022

@author: Computer Science ~ B
"""

def factorial(num):
    '''Returns factorial of num'''
    if num < 2:
        return 1
    else:
        return factorial(num-1) * num
    
def sumDigits(num):
    '''Returns the sum of all digits in num'''
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
fact_100 = factorial(100)
print(f'100! = {fact_100}')
print('The sum of the digits in 100! is {}'.format(sumDigits(fact_100)))