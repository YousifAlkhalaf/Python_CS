# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 13:22:12 2021

@author: Computer Science ~ B
"""

total_seconds = int(input('Enter the number of seconds: '))
hours = total_seconds//3600
minutes = (total_seconds%3600)//60
seconds = total_seconds%60
print('The time is', hours, 'hour(s),', minutes, 'minute(s), and', seconds, 'second(s)')