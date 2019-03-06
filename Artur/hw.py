#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime

def user():
    
    user.name = input ("What is your name?")
    while True:
        try:
            getdob = input("What is your date of birth? (DD/MM/YYYY)")
            user.dob = datetime.strptime(getdob, "%d/%m/%Y")
            break
        except ValueError:
            print ("Wrong format, try again...")
                
def main():
    user()
    try:
        print (user.name)
        print (user.dob)
    except AttributeError:
        print ("nah")

main()
