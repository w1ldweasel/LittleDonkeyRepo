#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime


def testuser():
    testuser.name = "testuser"
    testuser.dob = datetime.strptime("01/11/1992", "%d/%m/%Y")

def user():
    
    user.name = input ("What is your name?")
    while True:
        try:
            getdob = input("What is your date of birth? (DD/MM/YYYY)")
            user.dob = datetime.strptime(getdob, "%d/%m/%Y")
            break
        except ValueError:
            print ("Wrong format, try again...")

def bday(dob):
    todaysdate = datetime.now().date()
    dobdate = dob.date()
    yeardiff = todaysdate.year - dobdate.year
    bdaydate = datetime.strpti(todaysdate.year, dobdate.month, dobdate.day)
    print (todaysdate)
    print (dobdate)
    print (yeardiff) 
    print (bdaydate)

   

def main():
    testuser()
    bday(testuser.dob)
    print (testuser.name)
    print (testuser.dob)

main()
