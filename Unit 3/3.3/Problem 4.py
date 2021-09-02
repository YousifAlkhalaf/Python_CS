# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:06:08 2021

@author: Computer Science ~ B
"""
import math

years = 0
balance = float(input('Enter the initial investment in dollars: '))
interest_rate = float(input('Enter the interest rate, in percent: '))

while balance < math.pow(10, 6):
    balance += (balance * (interest_rate/100))
    years += 1
print(f'Your investment will reach $1 million in {years} years')