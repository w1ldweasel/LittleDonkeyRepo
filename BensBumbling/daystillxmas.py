#! /usr/bin/python

# script to output the number of days until xmas

import datetime

dt = datetime.datetime
delta = dt(2017, 12, 25) - dt.now()

print delta.days


