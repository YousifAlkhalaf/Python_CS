# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:20:07 2022

@author: Computer Science ~ B
"""
def first_last(num_list):
    '''Checks if first value is equal to last value'''
    if len(num_list) == 0:
        return False;
    if num_list[0] == num_list[len(num_list) - 1]:
        return True;
    return False;

print(first_last([1, 2, 3]))
print(first_last([1, 2, 3, 1]))
print(first_last([1, 2, 1]))
print(first_last([7]))
print(first_last([]))
print(first_last([1, 2, 3, 4, 5, 1]))
print(first_last([1, 2, 3, 4, 5, 13]))
print(first_last([13, 2, 3, 4, 5, 13]))
print(first_last([7, 7]))
    