# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 13:23:26 2022

@author: Computer Science ~ B
"""

class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.length * self.width

rect1 = Rectangle(3, 5)
rect2 = Rectangle(8, 7)
rect3 = Rectangle(1, 10)

print(f'First rectangle is {rect1.length} by {rect1.width} and has area {rect1.get_area()}')
print(f'Second rectangle is {rect2.length} by {rect2.width} and has area {rect2.get_area()}')
print(f'Third rectangle is {rect3.length} by {rect3.width} and has area {rect3.get_area()}')