# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:48:12 2021

@author: Computer Science ~ B
"""
# Make it two-way between metric and customary
# Two stars, long but onlhy slightly challenging

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
    if unit == 'fl oz' or unit == 'gal' or unit == 'mL' or unit == 'L':
        return 1
    elif unit == 'oz' or unit == 'lb' or unit == 'g' or unit == 'kg':
        return 2
    elif unit == 'in' or unit == 'ft' or unit == 'mi' or unit == 'cm' or unit == 'm' or unit == 'km':
        return 3
    
def is_float(str):
    for c in str:
        if c.isdigit() == False and c != '.':
            return False
    return True

def convert(val, unit1, unit2):
    # Fluid ounce
    if unit1 == 'fl oz':
        if unit2 == 'gal':
            return str((1/128) * val) + ' gal'
        elif unit2 == 'mL':
            return str(29.57344 * val) + ' mL'
        elif unit2 == 'L':
            return str((1/33.814) * val) + ' L'
    
    # Gallon
    elif unit1 == 'gal':
        if unit2 == 'fl oz':
            return str(128 * val) + ' fl oz'
        elif unit2 == 'mL':
            return str(3785.4 * val) + ' mL'
        elif unit2 == 'L':
            return str(3.7854 * val) + ' L'
    
    # Milliliter
    elif unit1 == 'mL':
        if unit2 == 'fl oz':
            return str((1/29.574) * val)  + ' fl oz'
        elif unit2 == 'gal':
            return str((1/3785) * val) + ' gal'
        elif unit2 == 'L':
            return str(0.001 * val) + ' L'
    
    # Liter
    elif unit1 == 'L':
        if unit2 == 'fl oz':
            return str(33.814 * val) + ' fl oz'
        elif unit2 == 'gal':
            return str((1/3.785) * val) + ' gal'
        elif unit2 == 'mL':
            return str(1000 * val) + ' mL'
    
    # Ounce
    elif unit1 == 'oz':
        if unit2 == 'lb':
            return str((1/16) * val) + ' lb'
        elif unit2 == 'g':
            return str(28.3495 * val) + ' g'
        elif unit2 == 'kg':
            return str((1/35.274) * val) + ' kg'
    
    # Pound
    elif unit1 == 'lb':
        if unit2 == 'oz':
            return str(16 * val) + ' oz'
        elif unit2 == 'g':
            return str(453.592 * val) + ' g'
        elif unit2 == 'kg':
            return str(0.453592 * val) + ' kg'
        
    # Gram
    elif unit1 == 'g':
        if unit2 == 'oz':
            return str((1/28.35) * val) + ' oz'
        elif unit2 == 'lb':
            return str((1/454) * val) + ' lb'
        elif unit2 == 'kg':
            return str(0.001 * val) + ' kg'
       
    # Kilogram
    elif unit1 == 'kg':
        if unit2 == 'oz':
            return str(35.274 * val) + ' oz'
        elif unit2 == 'lb':
            return str(2.20462 * val) + ' lb'
        elif unit2 == 'g':
            return str(1000 * val) + ' g'
    
    # Inches
    elif unit1 == 'in':
        if unit2 == 'ft':
            return str((1/12) * val) + ' ft'
        elif unit2 == 'mi':
            return str((1/63360) * val) + ' mi'
        elif unit2 == 'cm':
            return str(2.54 * val) + ' cm'
        elif unit2 == 'm':
            return str((1/39.37) * val) + ' m'
        elif unit2 == 'km':
            return str((1/39370) * val) + ' km'
    
    # Feet
    elif unit1 == 'ft':
        if unit2 == 'in':
            return str(12 * val) + ' in'
        elif unit2 == 'mi':
            return str((1/5280) * val) + ' mi'
        elif unit2 == 'cm':
            return str(30.48 * val) + ' cm'
        elif unit2 == 'm':
            return str((1/3.281) * val) + ' m'
        elif unit2 == 'km':
            return str((1/3281) * val) + ' km'
    
    # Mile
    elif unit1 == 'mi':
        if unit2 == 'in':
            return str(63360 * val) + ' in'
        elif unit2 == 'ft':
            return str(5280 * val) + ' ft'
        elif unit2 == 'cm':
            return str(160934 * val) + ' cm'
        elif unit2 == 'm':
            return str(1609.34 * val) + ' m'
        elif unit2 == 'km':
            return str(1.60934 * val) + ' km'
    
    # Centimeter
    elif unit1 == 'cm':
        if unit2 == 'in':
            return str((1/2.54) * val) + ' in'
        elif unit2 == 'ft':
            return str((1/30.48) * val) + ' ft'
        elif unit2 == 'mi':
            return str((1/160934) * val) + ' mi'
        elif unit2 == 'm':
            return str(0.01 * val) + ' m'
        elif unit2 == 'km':
            return str((1/100000) * val) + ' km'
        
    # Meter
    elif unit1 == 'm':
        if unit2 == 'in':
            return str(39.3701 * val) + ' in'
        elif unit2 == 'ft':
            return str(3.28084 * val) + ' ft'
        elif unit2 == 'mi':
            return str((1/1609) * val) + ' mi'
        elif unit2 == 'cm':
            return str(100 * val) + ' cm'
        elif unit2 == 'km':
            return str((1/1000) * val) + ' km'
    
    # Kilometer
    elif unit1 == 'km':
        if unit2 == 'in':
            return str(39370.1 * val) + ' in'
        elif unit2 == 'ft':
            return str(3280.84 * val) + ' ft'
        elif unit2 == 'mi':
            return str((1/1.609) * val) + ' mi'
        elif unit2 == 'cm':
            return str(100000 * val) + ' cm'
        elif unit2 == 'm':
            return str(1000 * val) + ' m'
    
    else:
        return 'ERROR'
            
unit1 = unit_input()
t1 = unit_type(unit1)

while True:
    unit2 = unit_input(False)
    t2 = unit_type(unit2)
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

            
        