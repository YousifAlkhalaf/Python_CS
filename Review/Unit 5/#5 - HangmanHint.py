# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:20:53 2022

@author: Computer Science ~ B
"""
def updateHint(word, hint, guess):
    for i in range (0, len(word), 1):
        if word[i] == guess:
            hint = hint[:i] + word[i] + hint[i+1:len(word)]
    return hint

def printHint(word):
    new_word = ''
    for c in word:
        new_word += c + ' '
    return new_word

def makeHint(word):
    hint = ''
    for i in range (0, len(word), 1):
        hint += '_'
    return hint

word = 'happiness'
hint = makeHint(word)
while word != hint:
    guess = input('Type in a guess: ')
    hint = updateHint(word, hint, guess)
    print(printHint(hint))
print('Success!')