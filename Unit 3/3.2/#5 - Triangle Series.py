# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:30:36 2021

@author: Computer Science ~ B
"""
# Find triangle series up to n
n = int(input('Enter a positive integer: '))
tri = 0
for i in range (1, n+1, 1):
    tri += i
    print(tri)