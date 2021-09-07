# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:50:53 2021

@author: Computer Science ~ B
"""

import math

radius = float(input('Input the radius in inches: '))
sphere_volume = (4/3)*math.pi*math.pow(radius, 3)
sphere_volume = round(sphere_volume, 3)

print(f'The volume is {sphere_volume} cubic inches.')