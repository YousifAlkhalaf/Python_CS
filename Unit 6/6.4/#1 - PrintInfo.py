# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 13:51:02 2022

@author: Computer Science ~ B
"""
def unpack_info(info):
    out_str = f'{info[0]}, age {info[1]}, height {info[2]} inches, weight {info[3]} pounds'
    return out_str

name = input('Enter name: ')
age = int(input('Enter age: '))
height = int(input('Enter height, in inches: '))
weight = int(input('Enter your weight in pounds: '))

info = (name, age, height, weight,)
print(unpack_info(info))
