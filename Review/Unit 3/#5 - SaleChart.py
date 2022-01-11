# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:25:08 2022

@author: Computer Science ~ B
"""
import math

def printSales(num):
    num = float(num)
    num = math.ceil(num / 100)
    dots = ''
    for i in range (0, num, 1):
        dots += '*'
    return dots

sales1 = int(input('Enter today\'s sales for store 1: '))
sales2 = int(input('Enter today\'s sales for store 2: '))
sales3 = int(input('Enter today\'s sales for store 3: '))
sales4 = int(input('Enter today\'s sales for store 4: '))
sales5 = int(input('Enter today\'s sales for store 5: '))

print('Store 1:', printSales(sales1))
print('Store 2:', printSales(sales2))
print('Store 3:', printSales(sales3))
print('Store 4:', printSales(sales4))
print('Store 5:', printSales(sales5))