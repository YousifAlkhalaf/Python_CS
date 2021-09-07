# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:12:26 2021

@author: Computer Science ~ B
"""

meal_cost = float(input('Enter the cost of the meal in dollars and cents: '))
guests = int(input('Enter number of people: '))
tip = int(input('Enter tip percent: '))

if guests >= 6 and tip < 18:
    tip = 18
    print('Tip is too low for {} guests. Tip = 18%'.format(guests))

person_cost = (meal_cost / guests) * (1+tip/100)
person_cost = format(person_cost, '.2f')

print('Cost per person = ${}'.format(person_cost))