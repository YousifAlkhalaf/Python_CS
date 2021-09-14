# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:23:16 2021

@author: Computer Science ~ B
"""

def beer(bottles):
    if bottles > 1:
        print(f'''{bottles} bottles of beer on the wall,
{bottles} bottles of beer!''')
    else:
        print('''1 bottle of beer on the wall,
1 bottle of beer!''')
    print('Take one down, and pass it around,')
    bottles -= 1
    if bottles == 0:
        print('NO MORE BOTTLES OF BEER ON THE WALL')
    elif bottles == 1:
        print('1 bottle of beer on the wall.\n')
    else:
        print(f'{bottles} bottles of beer on the wall.\n')

for i in range (5, 0, -1):
    beer(i)