# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:29:50 2022

@author: Computer Science ~ B
"""

def max_end(num_list):
    '''Replaces all elements in a list with the largest element on either end of the lists'''
    largest = max(num_list[0], num_list[-1])
    for i in range(len(num_list)):
        num_list.insert(i, largest)
        del num_list[i+1]
    return num_list
print(max_end([1, 2, 3, -5, 1, 3]))
print(max_end([11, 5, 9, -3, 1]))
print(max_end([2, 11, 3]))