# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:31:48 2021

@author: Computer Science ~ B
"""

word = input('Enter a word: ')
is_abecadarian = True
back_letter = ''

for i in range(len(word)):
    if back_letter <= word[i]:
        back_letter = word[i]
    else:
        is_abecadarian = False
        break

if is_abecadarian:
    print('The word is abecadarian')
else:
    print('The word is NOT abecadarian')