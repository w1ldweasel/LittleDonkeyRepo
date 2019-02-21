# -*- coding: utf-8 -*-
"""
Carneys Hello World
"""

# /usr/bin/python3

import datetime

inputname = ""
dobchk = ""

print("Hello World!")

inputname = input("What is your name? >")
print("Hello " + inputname)
dobask()

def dobask():
    """
    Ask for Date of Birth
    """
    inputdob = input("What is your Date of Birth? (YYYY-MM-DD) > ")
    print("You have entered > " + inputdob)

    date_format = '%Y-%m-%d'

    try:
        dobchk = datetime.datetime.strptime(inputdob, date_format)
        print(dobchk)
        return
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        dobask()

print("Now for some pointless stats about your Birthday")

#print("Now    :" + datetime.datetime.now())
#delta = dobchk - dt.now()
#print ("Its been " + delta.days, " since you were born")

#Say Bye Bye
def byebye():
    """
    Saye Bye Bye
    """
    print("I have to exit now, bye bye " + inputname)



#dt = datetime.datetime
#currentYear = dt.now().year
#delta = dt(currentYear, 12, 25) - dt.now()

#print ('Today\'s date is', dt.now())
#print ('There are ',delta.days, ' to Christmas')
    
