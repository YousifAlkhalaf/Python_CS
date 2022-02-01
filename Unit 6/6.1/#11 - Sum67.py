# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:05:39 2022

@author: Computer Science ~ B
"""

def sum67(num_list):
    i = 0
    total = 0
    while i < len(num_list):
        if num_list[i] == 6:
            while num_list[i] != 7:
                i += 1
            i += 1
        else:
            total += num_list[i]
            i += 1
    return total

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))
print(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]))
print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))
print(sum67([2, 7, 6, 2, 6, 2, 7]))
print(sum67([1, 6, 7, 7]))
print(sum67([6, 7, 1, 6, 7, 7]))
print(sum67([6, 8, 1, 6, 7]))
print(sum67([]))
print(sum67([6, 7, 11]))
print(sum67([11, 6, 7, 11]))
print(sum67([2, 2, 6, 7, 7]))