#! /usr/bin/python

# Written by Maxine
# Date 8/2/2108

import datetime
from datetime import date
from decimal import *

TWOPLACES = Decimal('0.01')

def proceed_shopdays():
    
    dt = datetime.datetime

    thisyear = dt.now().year
    delta = dt(thisyear, 12, 25) - dt.now()

#date formatting
    print ("Today\'s date is " , str(date.today().strftime("%d %b %Y")))


#example of how much monthly savings give for xmas
    exsave = 1000
    
    tdate = dt.now().day
    tmonth = dt.now().month
    
    if tdate >= 20 and tmonth == 11:
        thisamount = exsave
    elif tdate < 20 and tmonth == 12:
        thisamount = exsave / 12
    elif tdate >= 20 and tmonth == 12:
        thisamount = exsave / 11
    elif tdate < 20:
        dmonth = 12 - tmonth
        thisamount = exsave / dmonth
    elif tdate >= 20:
        dmonth = 11 - tmonth
        thisamount = exsave / dmonth

    
    print (" ")
    print ("If you would like to save £", exsave, " for Christmas, you will need to save £", round(thisamount), " a month from now")

   
#user input
    while True:
        try:
            asksave = input("How much do you need to save for Christmas in Pound Sterling?")
            usersave = Decimal(asksave)
#            if usersave != 2 or 1 or 0 decimal places / > 2 decimal places:
# THE BELOW IS A WORK IN PROGRESS, THIS DOESN'T WORK YET!
            if decimal.Inexact == true:
                print ("Please enter a valid Sterling amount i.e. 2 decimal places")
            else:
                break
        except ValueError:
            print ("That's not the correct format, please enter a number to save in Pounds" )
    
#savings calculation
    tdate = dt.now().day
    tmonth = dt.now().month
   
#test case set up
#    tdate = 25
#    tmonth = 7
    
    if tdate >= 20 and tmonth == 11:
        otheramount = usersave
    elif tdate < 20 and tmonth == 12:
        otheramount = usersave / 12
    elif tdate >= 20 and tmonth == 12:
        otheramount = usersave / 11
    elif tdate < 20:
        dmonth = 12 - tmonth
        otheramount = usersave / dmonth
    elif tdate >= 20:
        dmonth = 11 - tmonth
        otheramount = usersave / dmonth


#output to user
    print (" ")
    print("To have £", usersave, " saved for Christmas, you will need to save £", round(otheramount), " per month")
    print("This will give you £", usersave, " to spend on Cyber Monday deals!")

    print (" ")
    print ('There are ',delta.days, ' days to Christmas')

    
#code to run first function if program is started in interpreter
if __name__ == "__main__":
  proceed_shopdays()





