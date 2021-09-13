# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:22:23 2021

@author: Computer Science ~ B
"""

s1 = input('Enter string1: ')
s2 = input('Enter string2: ')
s3 = input('Enter string3: ')

max_length = 0

if len(s1) >= len(s2) and len(s1) >= len(s3):
    max_length = len(s1)
elif len(s2) >= len(s1) and len(s2) >= len(s3):
    max_length = len(s2)
else:
    max_length = len(s3)
    
print(s1.center(max_length))
print(s2.center(max_length))
print(s3.center(max_length))