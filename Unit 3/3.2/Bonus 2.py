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

ami_sum = 0
for i in range (1, 10000):
    for k in range (1, 10000):
        if  i != k and factor_sum(i) == factor_sum(k):
            ami_sum += k + i
            
print (ami_sum)