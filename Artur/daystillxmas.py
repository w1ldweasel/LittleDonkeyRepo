#! /usr/bin/python

# script to output the number of days until xmas

import datetime


dt = datetime.date
xmas = datetime.date(year,12,25)
delta = dt(xmas) - dt.now()
print ('Today\'s date is', dt.now())
print ('There are ',delta.days, ' to Christmas')

#print(delta.days)


