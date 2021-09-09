# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:22:23 2021

@author: Computer Science ~ B
"""
import math

def print_spaces(n, word):
    for i in range((n-1)//2, -1, -1):
        for k in range (i, 0, -1):
            print(end = ' ')
        print(word)

s1 = input ('Enter string1: ')
s2 = input ('Enter string2: ')
s3 = input ('Enter string3: ')

l1 = len(s1)
l2 = len(s2)
l3 = len(s3)

if l1 >= l2 and l1 >= l3:
    print(s1)
    print_spaces()
    