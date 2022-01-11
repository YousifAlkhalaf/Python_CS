# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

num = int(input('Enter a positive integer greater than one: '))
i = 2
while i <= num:
    print(i, end=' ')
    i += 2
print()
for i in range (2, num+1, 2):
    print(i, end=' ')