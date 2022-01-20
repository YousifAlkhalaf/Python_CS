# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:04:18 2022

@author: Computer Science ~ B
"""
import math

def inscribedRadius(n, s, do_round = True):
    angle = math.radians(180/n)
    radius = s/(2 * math.tan(angle))
    if do_round:
        radius = round(radius, 1)
    return radius

def regPolygonArea(n, s):
    '''Takes number of sides and side length. Returns area.'''
    r = inscribedRadius(n, s)
    area = n * ((s * r)/(2))
    area = '{:.1f}'.format(area)
    return area


value = regPolygonArea(6, 6)
print('regPolygonArea(6, 6)')
print('Expected output: 93.6')
print(f'Output: {value}\n')
value = regPolygonArea(8, 8)
print('regPolygonArea(8, 8)')
print('Expected output: 310.4')
print(f'Output: {value}\n')
value = regPolygonArea(5, 12)
print('regPolygonArea(5, 12)')
print('Expected output: 249.0')
print(f'Output: {value}\n')