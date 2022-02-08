# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:21:35 2022

@author: Computer Science ~ B
"""

def check_password(userbase, login):
    username = login[0]
    if username in userbase:
        if userbase[username] == login[1]:
            return True
    return False

pw = {'Bob': 'qwerty', 'Sarah': 'camel345', 'Vickie': '1234', 'Sean': 'passwrd'}

print(check_password(pw, ('Sarah', 'camel345')))
print(check_password(pw, ('Roger', '1234')))
print(check_password(pw, ('Sean', 'password')))
print(check_password(pw, ('Bob', 'qwerty')))
print(check_password(pw, ('Sean', 'passwrd')))
