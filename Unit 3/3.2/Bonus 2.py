# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:06:53 2021

@author: Computer Science ~ B
"""

def findAmicable(insert):
    sum = 0
    for i in range (1, insert, 1):
        if insert % i == 0:
            if insert/i != i:
                sum += i
    return sum



num1 = findAmicable(10000)
num2 = findAmicable(findAmicable(10000))
print(num1)
print(num2)
if findAmicable(num1) == num2 and num1 == findAmicable(num2):
    print('CLEAR!')