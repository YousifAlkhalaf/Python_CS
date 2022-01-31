# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 13:32:35 2022

@author: Computer Science ~ B
"""

def sum13(num_list):
    total = 0
    i = 0
    '''Returns sum of list excluding values immediately after 13 or equal to 13'''
    while i < len(num_list):
        if num_list[i] == 13:
            i += 2
        else:
            total += num_list[i]
            i += 1
    return total

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))
print(sum13([1, 2, 13, 2, 1, 13]))
print(sum13([13, 1, 2, 13, 2, 1, 13]))
print(sum13([13]))
print(sum13([13, 13]))
print(sum13([13, 0, 13]))
print(sum13([13, 1, 13]))
print(sum13([5, 7, 2]))
print(sum13([5, 13, 2]))
print(sum13([0]))
print(sum13([13, 0]))