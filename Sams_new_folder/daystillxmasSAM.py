# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:55:40 2019

@author: Home
"""
# script to output the number of days until xmas

import datetime

dt = datetime.datetime
#delta = dt(2019, 12, 25) - dt.now()

currentyear = dt.now().year
delta = dt(currentyear, 12, 25) - dt.now()

print ('Today\'s date is', dt.now())
print ('There are ',delta.days, ' to Christmas')

#print(delta.days)
