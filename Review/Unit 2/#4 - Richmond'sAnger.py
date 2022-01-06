# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:22:47 2022

@author: Computer Science ~ B
"""

is_frowning = input('Is Mrs. Richmond frowing or smiling? Y for frowning, N for smiling: ')
if is_frowning.lower == 'y':
    is_frowning = True
else:
    is_frowning = False

weather = input('Is the weather foggy or sunny? Y for foggy, N for sunny: ')
if weather.lower == 'y':
    weather = True #Foggy
else:
    weather = False #Sunny

if is_frowning ^ weather:
    print('Be cautious - it\'s difficult to judge')
elif is_frowning == False and weather == False:
    print('No worries - good mood!')
else:
    print('Beware! Bad Mood!')