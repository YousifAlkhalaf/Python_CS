# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:45:18 2022

@author: Computer Science ~ B
"""

def separateTypes(my_list):
    int_list = [i for i in my_list if type(i) == int]
    float_list = [i for i in my_list if type(i) == float]
    str_list = [i for i in my_list if type(i) == str]
    print('Original list:', my_list)
    print(int_list)
    print(str_list)
    print(float_list)

separateTypes([1, 'fish', 2, 'frogs', 3.2])