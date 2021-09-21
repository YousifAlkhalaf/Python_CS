# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:10:37 2021

@author: Computer Science ~ B
"""

def make_bricks(small, big, goal):
    l = 0
    while goal - l >= 5 and big > 0:
        l += 5
        big -= 1
    while goal > l and small > 0:
        l += 1
        small -= 1
    if l == goal:
        return True
    else:
        return False
    
print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))
print(make_bricks(3, 2, 8))
print(make_bricks(3, 2, 9))
print(make_bricks(6, 1, 11))
print(make_bricks(6, 0, 11))
print(make_bricks(1, 4, 11))
print(make_bricks(0, 3, 10))
print(make_bricks(1, 4, 12))