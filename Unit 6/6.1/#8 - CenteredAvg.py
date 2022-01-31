# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 13:28:44 2022

@author: Computer Science ~ B
"""

def centered_average(num_list):
    '''Finds avg value of list, without max & min values'''
    total = 0
    for num in num_list:
        total += num
    total -= max(num_list) + min(num_list)
    total /= len(num_list) - 2
    return total

print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))