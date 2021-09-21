# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:38:56 2021

@author: Computer Science ~ B
"""

def num_bars(goal, big_bars):
    if goal <= (5 * big_bars):
        if goal < 5:
            return goal
        else:
            return 0
    else:
        return goal - (5 * big_bars)

print(num_bars(12, 2))
print(num_bars(3, 2))
print(num_bars(50, 2))
print(num_bars(20, 6))