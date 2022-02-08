# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:10:19 2022

@author: Computer Science ~ B
"""

def flatten_list(list_2d):
    new_list = []
    for var in list_2d:
        for e in var:
            new_list.append(e)
    return new_list

print(flatten_list([[1, 2, 4], [5, 3], [8, 1]]))