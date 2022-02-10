# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:41:27 2022

@author: Computer Science ~ B
"""

def find_min_2nd(num_pairs):
    '''Returns tuple in num_pairs with smallest second value'''
    min_num = None
    min_index = -1
    for pair in range(len(num_pairs)):
        num = num_pairs[pair][1]
        if min_num == None or num < min_num:
            min_index = pair
            min_num = num
    return num_pairs[min_index]

print(find_min_2nd([(3, 4), (1, 2), (9, -10), (55, 0)]))