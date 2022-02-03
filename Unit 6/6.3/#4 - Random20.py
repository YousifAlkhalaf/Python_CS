# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 13:41:42 2022

@author: Computer Science ~ B
"""
def random20(words):
    for i in range(20):
        word = words.pop()
        print(word)
        words.add(word)
    return

words = {'say', 'something', 'I\'m', 'giving', 'up', 'on', 'you', 'I\'ll', 'be', 'the', 'one', 'if'}
random20(words)