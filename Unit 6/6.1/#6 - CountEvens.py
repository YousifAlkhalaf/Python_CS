# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:37:43 2022

@author: yousi
"""

def count_evens(num_list):
    evens = 0
    for num in num_list:
        if num % 2 == 0:
            evens += 1
    return evens

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))