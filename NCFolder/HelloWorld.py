# -*- coding: utf-8 -*-

# /usr/bin/python3
"""
Carneys Hello World
"""

import datetime

INPUT_NAME = ""
DOB_CHK = ""
DT = datetime.datetime


#DOB Validation
def dobvalchk(DOB):
    """
    Date of Birth Validation
    """
    date_format = '%Y-%m-%d'

    try:
        datetime.datetime.strptime(DOB, date_format)
    except:
        return False
    else:
        return True
    
#Say Bye Bye
def byebye():
    """
    Saye Bye Bye
    """
    print("I have to exit now, bye bye " + INPUT_NAME)


INPUT_NAME = input("What is your name? >")
print("Hello " + INPUT_NAME)

DOB = input("What is your Date of Birth? (YYYY-MM-DD) > ")

    
def getddob():
    DOB = ""
    i = 0
    # validate date string in dob
    while not dobvalchk(DOB):
        if i == 0:
            DOB = input("Well done you entered the correct format for the date")
        else:
            DOB = input("Idiot, you need to read the date format correctly, Try again")
        i += 1
    return DOB
    
    
    
    

DELTA = DOB() - DT.today()

print("You have entered > " + DOB)
print()
print("Now for some pointless stats about your Birthday")
print()
print("Now    :", DT.today())

print("You are"+ age + "years old today")
print("Its been " + DELTA.days, " days since you were born")
