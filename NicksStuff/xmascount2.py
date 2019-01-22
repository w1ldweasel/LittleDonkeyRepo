#! /usr/bin/python

# script to output the number of days until xmas

import datetime

dt = datetime.datetime

currentYear = dt.now().year
delta = dt(currentYear, 12, 25) - dt.now()

if dt.now() >= dt(currentYear, 12, 25):
print ('*** Christmas Week ***')
else:
print ('Today's date is', dt.now())
print ('There are ',delta.days, ' to Christmas')
