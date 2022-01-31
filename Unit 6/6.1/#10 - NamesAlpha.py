# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 13:45:09 2022

@author: Computer Science ~ B
"""

def alpha(names):
    '''Returns names in alphabetical order'''
    names.sort()
    return names

print(alpha(['Bob', 'Alice', 'Katniss']))
print(alpha(['Bob']))
print(alpha(['Trevor', 'Tyler', 'Tom', 'Tim']))
