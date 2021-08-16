# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:08:48 2021

@author: Computer Science ~ B
"""

hours = 3
minutes = 0

errand1 = int(input('How many minutes for the first errand? '))
errand2 = int(input('How many minutes for the second errand? '))
errand3 = int(input('How many minutes for the third errand? '))

errand_time = errand1 + errand2 + errand3

hours += errand_time//60
minutes += errand_time%60
print(f'You will return home at {hours}:{minutes}')