#! /usr/bin/python

# script to output the number of days until xmas

import datetime

dt = datetime.datetime

currentyear = dt.now().year
delta = dt(currentyear, 12, 25) - dt.now()



print ('Today\'s date is', dt.now())
print ('T-Minus',delta.days, 'days to Christmas')