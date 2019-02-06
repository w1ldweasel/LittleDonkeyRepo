#! /usr/bin/python

# script to output the number of days until xmas

import datetime

dt = datetime.datetime
currentYear = dt.now().year
delta = dt(currentYear, 12, 25) - dt.now()

print ('Today\'s date is', dt.now())
print ('There are ',delta.days, ' to Christmas')
