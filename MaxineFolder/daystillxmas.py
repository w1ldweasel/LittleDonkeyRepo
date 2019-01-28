#! /usr/bin/python

# script to output the number of days until xmas

import datetime

dt = datetime.datetime
#delta = dt(2019, 12, 25) - dt.now()

thisyear = dt.now().year
delta = dt(thisyear, 12, 25) - dt.now()

print ('Today\'s date is', dt.now())
print ('There are ',delta.days, ' days to Christmas')

#print(delta.days)


