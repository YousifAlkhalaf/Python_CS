# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:48:12 2021

@author: Computer Science ~ B
"""

def unit_input():
    unit = 'invalid'
    while unit == 'invalid':
        unit = input('Enter a unit to convert from: ')
        unit = unit.lower()
        if unit == 'gallons' or unit == 'gal':
            unit = 'gal'
        elif unit == 'fl oz' or unit == 'fluid oz' or unit == 'fluid ounces':
            unit = 'fl oz'
        elif unit == 'oz' or unit == 'ounces':
            unit = 'oz'
        elif unit == 'lb' or 'pounds':
            unit = 'lb'
        elif unit == 'in' or unit == 'inches':
            unit = 'in'
        elif unit == 'ft' or unit == 'feet':
            unit = 'ft'
        elif unit == 'mi' or unit == 'miles':
            unit = 'mi'
        elif unit == 'ml' or unit == 'milliliters':
            unit = 'mL'
        elif unit == 'l' or unit == 'liters':
            unit = 'L'
        elif unit == 'g' or unit == 'grams':
            unit = 'g'
        elif unit == 'kg' or unit == 'kilograms':
            unit = 'kg'
        elif unit == 'm' or unit == 'meters':
            unit = 'm'
        elif unit == 'cm' or unit == 'centimeters':
            unit = 'cm'
        elif unit == 'km' or unit == 'kilometers':
            unit = 'km'
        else:
            unit = 'invalid'
            print('Invalid input')

unit_input()
            
        