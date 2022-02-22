# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:30:07 2022

@author: Computer Science ~ B
"""
import random

names = []

for i in range(5):
    num = random.randint(1, 11)
    names.append((input('Enter a name: '), str(num)))

f = open('Names.txt', 'w')
for pair in names:
    write_str = f'{pair[0]} - {pair[1]}\n'
    f.write(write_str)
f.close()