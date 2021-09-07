# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:22:20 2021

@author: Computer Science ~ B
"""

num = int(input('Enter a positive integer: '))
i = 1
while i <= num:
    if num % i == 0:
        print(i, end = '')
        if i < num:
            print (',', end  = ' ')
    i += 1