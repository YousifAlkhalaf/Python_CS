# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:33:28 2022

@author: Computer Science ~ B
"""

def remove_empty(list_2d):
    i = 0
    while i < len(list_2d):
        if len(list_2d[i]) < 1:
            del list_2d[i]
        else:
            i += 1
    return list_2d

print(remove_empty([[1, 2, 3], [21, 34], [], [5, 4, 3], []]))