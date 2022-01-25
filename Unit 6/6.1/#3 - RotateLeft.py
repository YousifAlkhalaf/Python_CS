# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:53:17 2022

@author: Computer Science ~ B
"""
def rotate_left2(num_list):
    '''Moves all list contents to the left 1, loops around to keep same length'''
    return num_list[1:] + num_list[0:1:]
def rotate_left(num_list):
    '''Moves all list contents to the left 1, loops around to keep same length'''
    num_list.insert(len(num_list), num_list[0])
    del num_list[0]
    return num_list

print(rotate_left([1, 2, 3]))
print(rotate_left([5, 11, 21, 9]))
print(rotate_left([7, 0, 0]))
print(rotate_left([1, 2, 2, 2, 1]))
print(rotate_left([0, 0, 1]))
print()
print(rotate_left2([1, 2, 3]))
print(rotate_left2([5, 11, 21, 9]))
print(rotate_left2([7, 0, 0]))
print(rotate_left2([1, 2, 2, 2, 1]))
print(rotate_left2([0, 0, 1]))