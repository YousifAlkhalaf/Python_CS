# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:26:23 2022

@author: Computer Science ~ B
"""


class Pizza(object):
    order_num = 1

    def __init__(self, toppings=[]):
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

    def __init__(self, toppings=[]):
        super().__init__(toppings)

    def __str__(self):
        self.price = Personal.base_price + len(self.toppings)
        out_str = super().__str__()
        out_str += '  Personal   '
        out_str += f'${self.price}'
        return out_str

    def __name__(self):
        return 'Personal'


class Medium(Pizza):
    base_price = 9.99

    def __init__(self, toppings=[]):
        super().__init__(toppings)

    def __str__(self):
        self.price = Medium.base_price + len(self.toppings)
        out_str = super().__str__()
        out_str += '  Medium   '
        out_str += f'${self.price}'
        return out_str

    def __name__(self):
        return 'Medium'


class Large(Pizza):
    base_price = 12.99

    def __str__(self):
        self.price = Large.base_price + len(self.toppings)
        out_str = super().__str__()
        out_str += '  Large   '
        out_str += f'${self.price}'
        return out_str

    def __name__(self):
        return 'Large'


p3 = Personal(['onions'])
print(p3)

p4 = Large(['onions', 'tomatoes', 'jalapenos'])
print(p4)

p5 = Medium()
print(p5)

orders = [p3, p4, p5]
most_toppings = max(p3.toppings, p4.toppings, p5.toppings)
topping_len = len(most_toppings) + 5
for topping in most_toppings:
    topping_len += len(topping)

if topping_len < 10:
    space = 10
else:
    space = topping_len


print('-' * 60)
print('NUMBER|{:^10s}|{:^{}s}|{:>7s}'.format(
    'SIZE', 'TOPPINGS', space,  'PRICE'))
print('-' * 60)
for order in orders:

    topping_set = ''
    if len(order.toppings) == 0:
        topping_set = 'None'
    else:
        for i in range(0, len(order.toppings) - 1):
            topping_set += order.toppings[i] + ', '
        topping_set += order.toppings[-1]

    size = order.__name__()

    out_str = '{:>6}|{:^10}|{:^{}}|{:>7}'.format(
        order.order_num, size, topping_set, space, '$' + str(order.price))
    print(out_str)
