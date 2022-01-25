# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:46:44 2022

@author: Computer Science ~ B
"""

def get_total(num_list):
    '''Returns sum of elements'''
    total = 0;
    for num in num_list:
        total += num
    return total

print(get_total([1, 2, 3]))
print(get_total([5, 11, 2, 2, 1]))
print(get_total([7, 0, 0]))
print(get_total([1, 2, 1, 100]))
print(get_total([1, 1, -1]))
print(get_total([2, 7, 2]))
print()
print(sum([1, 2, 3]))
print(sum([5, 11, 2, 2, 1]))
print(sum([7, 0, 0]))
print(sum([1, 2, 1, 100]))
print(sum([1, 1, -1]))
print(sum([2, 7, 2]))
