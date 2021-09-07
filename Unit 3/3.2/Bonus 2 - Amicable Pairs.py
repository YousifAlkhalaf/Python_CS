# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:06:53 2021

@author: Computer Science ~ B
"""

def factor_sum(insert):
    sum = 0
    for i in range (1, insert, 1):
        if insert % i == 0:
            sum += i
    return sum

print (factor_sum(10000))