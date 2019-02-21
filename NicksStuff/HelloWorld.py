# -*- coding: utf-8 -*-

# /usr/bin/python3
"""
Carneys Hello World
"""

import datetime
import time as t

INPUT_NAME = ""
INPUT_DOB = ""
DOB_CHK = ""
DT = datetime.datetime

def dobask():
    """
    Ask for Date of Birth
    """
    INPUT_DOB = input("What is your Date of Birth? (YYYY-MM-DD) > ")
    print("You have entered > " + INPUT_DOB)

    date_format = '%Y-%m-%d'

    try:
        DOB_CHK = datetime.datetime.strptime(INPUT_DOB, date_format)
        print("Logging to system as > ", DOB_CHK)
        t.sleep(1)
        return
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        dobask()

#Say Bye Bye
def byebye():
    """
    Saye Bye Bye
    """
    print("I have to exit now, bye bye " + INPUT_NAME)




print("Hello World!")

INPUT_NAME = input("What is your name? >")
print("Hello " + INPUT_NAME)
dobask()

t.sleep(1)
print()
print("Now for some pointless stats about your Birthday")
print()
print("Now    :", DT.today())


# fukkd from here onwards

DELTA = DOB_CHK() - DT.today()
print("Its been " + DELTA.days, " days since you were born")


#dt = datetime.datetime
#currentYear = dt.now().year
#delta = dt(currentYear, 12, 25) - dt.now()

#print ('Today\'s date is', dt.now())
#print ('There are ',delta.days, ' to Christmas')
