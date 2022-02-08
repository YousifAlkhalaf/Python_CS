# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:15:22 2022

@author: Computer Science ~ B
"""

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [1, 2, 3, 4, 5]
my_dict = {}

for i in range (5):
    my_dict.update({list1[i]: list2[i]})
print(my_dict)