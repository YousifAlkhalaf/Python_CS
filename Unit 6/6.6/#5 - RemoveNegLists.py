# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:31:23 2022

@author: Computer Science ~ B
"""

def remove_neg_lists(list_2d):
    '''Lists with values < 0 are removed'''
    l = 0
    while l < len(list_2d):
        for e in list_2d[l]:
            if e < 0:
                del list_2d[l]
                l -= 1
                break
        l += 1
    return list_2d

print(remove_neg_lists([[11, 2, 3], [21, 34], [2, -3, 5], [5, -4, 3], [-2]]))