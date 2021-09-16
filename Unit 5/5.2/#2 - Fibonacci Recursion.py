# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:12:08 2021

@author: Computer Science ~ B
"""

def fibonacci(num):
    if num < 3:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

num = int(input('Which term? '))
print(fibonacci(num))