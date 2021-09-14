# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:45:04 2021

@author: Computer Science ~ B
"""
def is_vowel(letter):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return True
    else:
        return False
    
word = input('Enter a word: ')
word = word.lower()
i = 0
pig = ''

if is_vowel(word[i]):
    pig = word + 'yay'
else:
    while i < len(word) and is_vowel(word[i]) == False:
        i += 1
    pig = word[i: len(word)] + word[0: i] + 'ay'

print(f'New word: {pig}')