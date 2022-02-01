# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:41:34 2022

@author: Computer Science ~ B
"""

def doublePositives(num_list):
    new_list = [i * 2 if i > 0 else i for i in num_list]
    return new_list

num_list = [3, 2, 1, -0.5, -1, -1.5]
print(num_list)
print(doublePositives(num_list))