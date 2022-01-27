# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:34:40 2022

@author: yousi
"""

def big_diff(num_list):
    return max(num_list) - min(num_list)

print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))