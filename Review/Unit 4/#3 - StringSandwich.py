# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:53:54 2022

@author: Computer Science ~ B
"""

a = input('Enter a string: ')
b = input('Enter a string: ')
if len(a) > len(b) :
    print(b + a + b)
else:
    print(a + b + a)