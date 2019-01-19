#! /usr/bin/python

# script to output the number of days until xmas

import datetime

dt = datetime.datetime
thisYear = dt.today().year
delta = dt(thisYear, 12, 25) - dt.now()

print ('Today\'s date is', dt.now().strftime("%B %d, %Y"))
print ('There are ',delta.days, ' to Christmas')

#print(delta.days)