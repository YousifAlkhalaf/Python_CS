# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:48:12 2021

@author: Computer Science ~ B
"""

def unit_input(is_input = True):
    unit = -1
    while unit == -1:
        if is_input:
            unit = input('Enter a unit to convert from: ')
        else:
            unit = input('Enter a unit to convert to: ')
        unit = unit.lower()
        # Volume
        if unit == 'gallons' or unit == 'gal':
            unit = 'gal'
        elif unit == 'fl oz' or unit == 'fluid oz' or unit == 'fluid ounces':
            unit = 'fl oz'
        elif unit == 'ml' or unit == 'milliliters':
            unit = 'mL'
        elif unit == 'l' or unit == 'liters':
            unit = 'L'
        
        # Weight
        elif unit == 'oz' or unit == 'ounces':
            unit = 'oz'
        elif unit == 'lb' or unit == 'pounds':
            unit = 'lb'          
        elif unit == 'g' or unit == 'grams':
            unit = 'g'
        elif unit == 'kg' or unit == 'kilograms':
            unit = 'kg'
            
        # Distance
        elif unit == 'in' or unit == 'inches':
            unit = 'in'
        elif unit == 'ft' or unit == 'feet':
            unit = 'ft'
        elif unit == 'mi' or unit == 'miles':
            unit = 'mi'
        elif unit == 'm' or unit == 'meters':
            unit = 'm'
        elif unit == 'cm' or unit == 'centimeters':
            unit = 'cm'
        elif unit == 'km' or unit == 'kilometers':
            unit = 'km'
        
        else:
            unit = -1
            print('Invalid input')
        
        if unit != -1:
            return unit

# 1 = volume
# 2 = weight
# 3 = distance
def unit_type(unit):
    if unit == 'gal' or unit == 'fl oz' or unit == 'mL' or unit == 'L':
        return 1
    elif unit == 'oz' or unit == 'lb' or unit == 'g' or unit == 'kg':
        return 2
    elif unit == 'in' or unit == 'ft' or unit == 'mi' or unit == 'm' or unit == 'cm' or unit == 'km':
        return 3
    
def is_float(str):
    for c in str:
        if c.isdigit() == False and c != '.':
            return False
    return True

def convert(val, unit1, unit2):
    # Gallon
    if unit1 == 'gal':
        if unit2 == 'fl oz':
            return str(128 * val) + ' fl oz'
        elif unit2 == 'mL':
            return str(3785.4 * val) + ' mL'
        elif unit2 == 'L':
            return str(3.7854 * val) + ''
    
    # Fluid ounce
    if unit1 == 'fl oz':
        if unit2 == 'gal':
            return 0.0078125 * val
        elif unit2 == 'mL':
            return 29.57344 * val
        elif unit2 == 'L':
            return 0.02957344 * val
        
    # Milliliter
    if unit1 == 'mL':
        if unit2 == 'gal':
            return str(0.0002641729 * val) + ' gal'
        elif unit2 == 'fl oz':
            return str(0.03381413 * val)  + ' fl oz'
        elif unit2 == 'L':
            return str(0.001 * val) + ' L'
    
    # Liter
    if unit1 == 'L':
        if unit2 == 'gal':
            return 0.2641729 * val
        
        
            
unit1 = unit_input()
t1 = unit_type(unit1)
print(t1)
while True:
    unit2 = unit_input(False)
    t2 = unit_type(unit2)
    print(t2)
    if unit_type(unit2) != t1 or unit2 == unit1:
        print('Invalid unit. Try again.')
    else:
        break

while True:
    v1 = input('Enter input value: ')
    if is_float(v1):
        v1 = float(v1)
        break
    else:
        print('Invalid input')

v2 = convert(v1, unit1, unit2)
print(f'The value is {v2}.')

            
        