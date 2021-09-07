# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:22:55 2021

@author: Computer Science ~ B
"""

year = int(input('What year were you born in? '))
generation = ''

if year >= 1995:
    generation = 'Gen Z'
elif year >= 1980:
    generation = 'the Milennial generation'
elif year >= 1965:
    generation = 'Gen X'
else:
    generation = 'the Baby Boomer generation'

print('You are a member of ' + generation)