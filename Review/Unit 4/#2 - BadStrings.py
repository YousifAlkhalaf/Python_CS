# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:34:26 2022

@author: Computer Science ~ B
"""

word = input('Enter a string: ')
if word.find('bad') < 2 and word.find('bad') != -1:
    print('BAD')
else:
    print('not BAD')