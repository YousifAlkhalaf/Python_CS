# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 13:56:38 2022

@author: Computer Science ~ B
"""

sq_ft = float(input("Enter number of square feet: "))
acres = round(sq_ft / 43560, 2)
print(f'{sq_ft} square feet is {acres} acres')