# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:44:41 2021

@author: Computer Science ~ B
"""

num_a = int(input('Enter value of a: '))
num_b = int(input('Enter value of b: '))
num_c = int(input('Enter value of c: '))

sum = int(0)

if num_a != 13:
    sum += num_a
    if num_b != 13:
        sum += num_b
        if num_c != 13:
            sum += num_c

print('Sum is', sum)