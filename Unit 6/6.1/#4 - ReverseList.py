# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:18:05 2022

@author: Computer Science ~ B
"""
def reverse_list(num_list):
    '''Reverses the order of elements'''
    flipped = []
    for i in range (len(num_list) - 1, -1, -1):
        flipped.append(num_list[i])
    return flipped

print(reverse_list([1, 2, 3]))
print(reverse_list([5, 11, 9, 15]))
print(reverse_list([7, 0, 0, 0, 0, 0]))
print(reverse_list(['I', 'am', 3]))
