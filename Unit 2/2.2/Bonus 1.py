# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:28:39 2021

@author: Computer Science ~ B
"""

wanted_length = int(input('Enter the desired length: '))
big_num = int(input('Enter the number of big bricks: '))
small_num = int(input('Enter the number of small bricks: '))

big_bricks = wanted_length//5

if big_bricks > big_num:
    big_bricks = big_num

wanted_length -= big_bricks * 5

small_bricks = wanted_length
if small_bricks > small_num:
    print('Sorry, cannot build')
else:
    print('Use {} big brick(s) and {} small brick(s)'.format(big_bricks, small_bricks))