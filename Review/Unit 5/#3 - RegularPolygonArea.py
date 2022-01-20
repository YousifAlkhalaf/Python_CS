# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:33:00 2022

@author: Computer Science ~ B
"""

def regPolygonArea(n, s, f):
    '''Takes number of sides, side length, and diameter of inscribed circle. Returns area.'''
    area = n * ((s * 0.5 * f)/(2))
    area = '{:.1f}'.format(area)
    return area

value = regPolygonArea(6, 6, 10.4)
print('regPolygonArea(6, 6, 10.4)')
print('Expected output: 93.6')
print(f'Output: {value}\n')
value = regPolygonArea(8, 8, 19.4)
print('regPolygonArea(8, 8, 19.4)')
print('Expected output: 310.4')
print(f'Output: {value}\n')
value = regPolygonArea(5, 12, 16.6)
print('regPolygonArea(5, 12, 16.6)')
print('Expected output: 249.0')
print(f'Output: {value}\n')