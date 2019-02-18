#! /usr/bin/python
# script to output the number of days until xmas

import datetime

time = datetime.datetime.now()

#work out the year we are in
currentYear = time.strftime('%Y')

#how many days calc
dt = datetime.datetime
xmas = dt(int(currentYear), 12, 25) - dt.now()

#output
print ("It is the year", currentYear, ". Today is day", time.strftime('%d'), 'of the', time.strftime('%m'), 'month. This means there are', xmas.days, 'days until xmas.')


