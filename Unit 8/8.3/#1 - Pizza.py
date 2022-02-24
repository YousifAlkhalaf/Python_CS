# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:13:55 2022

@author: Computer Science ~ B
"""

class Pizza(object):
    order_num = 1
    
    def __init__(self, toppings = []):
        self.toppings = toppings
        self.order_num = Pizza.order_num
        Pizza.order_num += 1
    
    def __str__(self):
        out_str = f'{self.order_num}: Pizza with'
        if len(self.toppings) == 0:
            out_str += ' no toppings'
        else:
            for topping in self.toppings:
                out_str += ' ' + topping
        return out_str
    
p1 = Pizza(['sausage', 'mushroom'])
print(p1)

p2 = Pizza() # no toppings
print(p2)