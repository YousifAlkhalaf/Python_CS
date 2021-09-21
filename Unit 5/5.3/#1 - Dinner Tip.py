# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:31:08 2021

@author: Computer Science ~ B
"""

def calc_total(sub, tip = 20):
    return sub + (sub * (tip/100))

print('The total is', round(calc_total(124.38, 15), 2))
print('The total is', round(calc_total(124.38), 2))
print('The total is', round(calc_total(81.59, 20), 2))
print('The total is', round(calc_total(81.59), 2))