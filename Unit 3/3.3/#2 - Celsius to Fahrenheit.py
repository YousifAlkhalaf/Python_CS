# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 13:32:53 2021

@author: Computer Science ~ B
"""

print('Celsius  |  Fahrenheit\n----------------------')

for celsius in range (0, 101, 10):
    fahrenheit = (celsius * (9/5)) + 32
    fahrenheit = int(fahrenheit)
    print(f'    {celsius:>3}  |  {fahrenheit:>3}')