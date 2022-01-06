# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:37:20 2022

@author: Computer Science ~ B
"""
bought_shares = 0
commission = 0

# Input funds & stock prices
start_money = float(input('How much will you invest? $'))
old_price = float(input('What is the stock price? $'))

# Calculates amount of shares to buy, lowers money amount
while (bought_shares + 1) * old_price < 0.98 * start_money:
    bought_shares += 1;
print(f'{bought_shares} shares purchased')

# Calculates commission cost
commission = 0.02 * (bought_shares * old_price)
str_comm = str('{:.2f}').format(commission)
print(f'Your broker collects ${str_comm}')

#Prints remaining money
money = start_money - (bought_shares * old_price) - commission
print('You have ${:.2f} left over'.format(money))

print('\nTime to sell!\n')

#Calculate new commission cost & revenue
new_price = float(input('What is the new stock price? $'))
new_money = bought_shares * new_price
print('You collect ${:.2f}'.format(new_money))
commission = 0.02 * new_money
print('Your broker collects ${:.2f}'.format(commission))
money = money + new_money - commission
print('You now have ${:.2f}'.format(money))
print('Your profit/loss is ${:.2f}'.format(money - start_money))

