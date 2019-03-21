#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 19:57:24 2019

@author: maxinemcfarlane
"""
from datetime import date
from datetime import datetime


def proceed_hwnumber2():
    
#user to supply input to program
    name = input("Please tell me your name: ")
    while True:
        try:
            askdob = input(name + ", please tell me your date of birth in the format DD/MM/YYYY: ")
            dob = datetime.strptime(askdob, "%d/%m/%Y").date()
            if dob > date.today():
                print ("You've not been born yet!")
            else:
                break
        except ValueError:
            print ("That's not the correct format!")


#calculate users age today 
    today = date.today()
    yearage1 = today.year - dob.year
    monthage1 = today.month - dob.month
    dayage1 = today.day - dob.day


#output to user    
    print ('Hello World') 
    print ('Hello ' + name)
    if monthage1 < 0 or monthage1 == 0 and dayage1 < 0:
        print ("You are ", yearage1 - 1," years old today")
    else:
        print ("You are ", yearage1 ," years old today")


#calculate if users birthday and print HB if so
    if dob.day == today.day and dob.month == today.month:
        print("Happy Birthday " + name)

    
#code to run first function if program is started in interpreter
if __name__ == "__main__":
  proceed_hwnumber2()
      


#def proceed_hwnumber():
#    
##user to supply input to program
#    name = (input("Please tell me your name: "))
#    yearob = int(input("Please tell me the year you were born (YYYY): "))
#    monthob = int(input("Please tell me what number month you were born: "))
#    dateob = int(input("Please tell me the date you were born: "))
#
#
##calculate users age today
#    today = date.today()
#    yearage = today.year - yearob
#    monthage = today.month - monthob
#    dayage = today.day - dateob
#
#
##output to user    
#    print ('Hello world')
#    print ('Hello ' + name)
#    if monthage < 0 or monthage == 0 and dayage < 0:
#        print ("You are ", yearage - 1," years old today")
#    else:
#        print ("You are ", yearage ," years old today")
#
#
##calculate if users birthday and print HB if so
#    if dateob == today.day and monthob == today.month:
#        print("Happy Birthday " + name)
#
#
##code to run first function if program is started in interpreter
#if __name__ == "__main__":
#  proceed_hwnumber()
#  
  
  

"""
Hi Max, it works but seems rather clunky with the unnatural way to enter the date.  
take a look at the datetime.strptime method
"""
# MM - updated after running within Spyder.  Updated ReadMe to reflect 
