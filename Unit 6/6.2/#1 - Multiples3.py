# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:33:49 2022

@author: Computer Science ~ B
"""

def multiples3():
    '''Multiples of 3 from 3 to 45'''
    my_list = list(range(1, 16))
    my_list = [i*3 for i in my_list]
    return my_list

print(multiples3())