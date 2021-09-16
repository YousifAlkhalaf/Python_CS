# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:36:50 2021

@author: Computer Science ~ B
"""

def solve_quadratic(a, b, c, x):
    solution = a*(x**2) + b*x + c
    return solution

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
x = float(input('Enter x: '))

quad = solve_quadratic(a, b, c, x)
print(f'Solution is {quad}')