# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:16:03 2022

@author: Computer Science ~ B
"""

def repeated_values(my_tuple):
    for e in my_tuple:
        if my_tuple.count(e) > 1:
            return True
    return False

print(repeated_values((3, 4, 5, 'a', 7))) 
print(repeated_values((3, 'a', 5, 'a', 7))) 
print(repeated_values((7, 4, 5, 'a', 7))) 
print(repeated_values(('b', 'c', 'd', 'a', 'e'))) 
print(repeated_values(('a', 4, 5, 'a', 7)))

    