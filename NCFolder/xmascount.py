#! /usr/bin/python

"""
Script to output the number of days until xmas
"""

import datetime

DT = datetime.datetime

CURRENTYEAR = DT.now().year
DELTA = DT(CURRENTYEAR, 12, 25) - DT.now()

if DT.now() >= DT(CURRENTYEAR, 12, 25):
    print('*** Christmas Week ***')
else:
    print('Today\'s date is', DT.now())
    print('There are ', DELTA.days, ' to Christmas')
