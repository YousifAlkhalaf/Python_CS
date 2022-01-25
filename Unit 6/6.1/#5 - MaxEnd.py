# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:29:50 2022

@author: Computer Science ~ B
"""

def max_end(num_list):
    largest = max(num_list[0], num_list[-1])
    for i in range(len(num_list)):
        num_list.insert(i, largest)
        del num_list[i+1]
    return num_list
print(max_end([1, 2, 3, -5, 1, 3]))
            