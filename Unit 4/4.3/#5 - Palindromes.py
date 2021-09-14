# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:04:24 2021

@author: Computer Science ~ B
"""

is_palindrome = True
i = 0
phrase = input('Enter a word or phrase: ')

phrase = phrase.replace(',', '')
phrase = phrase.replace('.', '')
phrase = phrase.replace('!', '')
phrase = phrase.replace('\'', '')
phrase = phrase.replace('?', '')
phrase = phrase.replace(' ', '')
phrase = phrase.lower()

while is_palindrome and i < len(phrase) - i:
    if phrase[i] != phrase[len(phrase) - i - 1]:
        is_palindrome = False
    else:
        i += 1

if is_palindrome:
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')