# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:35:25 2022

@author: Computer Science ~ B
"""
def findDiscount(num_bought):
    '''Calculates the discount given'''
    if num_bought >= 10 and num_bought <= 19:
        return 0.8
    elif num_bought >= 20 and num_bought <= 49:
        return 0.7
    elif num_bought >= 50 and num_bought <= 99:
        return 0.6
    elif num_bought > 99:
        return 0.5
    else:
        return 1
    

pack_price = 99
num_bought = int(input('Enter the number of packages purchased: '))

#Find discount
