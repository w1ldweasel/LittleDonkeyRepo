#! /usr/bin/python

# script to output the number of days until xmas

import datetime


dt = datetime.date
year = dt.now().year
xmas = dt.date(year,12,25)
delta = dt(xmas) - dt.now()
print ('Today\'s date is', dt.now())
print ('There are ',delta.days, ' to Christmas')

#print(delta.days)

"""
I'm getting an error on line 9, 
intepreter is complaining that datetime.date (which is what dt is set to) 
does not have a now attribute
"""