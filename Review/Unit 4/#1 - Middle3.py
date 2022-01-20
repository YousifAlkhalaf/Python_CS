# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

word = input("Enter a string with an odd number of characters: ")
midpoint = len(word)//2
new_word = ''
for i in range (0, len(word), 1):
    if i >= midpoint-1 and i <= midpoint+1:
        new_word += word[i]
print(new_word)
    