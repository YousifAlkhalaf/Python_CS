# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:26:23 2022

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

class Personal(Pizza):
    base_price = 5.99
    
    def __init__(self, toppings):
        super().__init__(toppings)
        self.price = Personal.base_price + len(toppings)
    
    def __str__(self):
        out_str = super().__str__()
        out_str += '  Personal   '
        out_str += f'${self.price}'
        return out_str

class Medium(Pizza):
    base_price = 9.99
    
    def __init__(self, toppings):
        super().__init__(toppings)
        self.price = Medium.base_price + len(toppings)
    
    def __str__(self):
        out_str = super().__str__()
        out_str += '  Medium   '
        out_str += f'${self.price}'
        return out_str

class Large(Pizza):
    base_price = 12.99
    
    def __str__(self):
        self.price = Large.base_price + len(self.toppings)
        out_str = super().__str__()
        out_str += '  Large   '
        out_str += f'${self.price}'
        return out_str


p3 = Personal(['onions'])
print(p3)

p4 = Large(['onions', 'tomatoes', 'jalapenos'])
print(p4)

p5 = Medium()
print(p5)
