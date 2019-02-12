#! /usr/bin/python

# Written by Maxine
# Date 8/2/2108

import datetime
from datetime import date


def proceed_shopdays():
    
    dt = datetime.datetime

    thisyear = dt.now().year
    delta = dt(thisyear, 12, 25) - dt.now()

#date formatting
    print ("Today\'s date is " , str(date.today().strftime("%d %b %Y")))


#example of how much monthly savings give for xmas
    exsave = 1000
  
#    weekday() == 0 (MON)
#    weekday() == 4 (THUR)
#   last sunday in Nov = thanksgiving
#   cyber monday is monday following that
    
#    cmdelta = dt(cyber mon?) - dt.now()
    
    months = 12 - dt.now().month
    thisamount = exsave / months
    
    print (" ")
    print ("If you would like to save £1000 for Christmas, you will need to save £", round(thisamount), " a month from now")

   
#user input
    usersave = int(input("How much do you need to save for Christmas in Pound Sterling?"))

    
#savings calculation
    otheramount = usersave / months


#output to user
    print (" ")
    print("To have £", usersave, " saved for Christmas, you will need to save £", round(otheramount), " per month")
    print("This will give you £", usersave, " to spend on Cyber Monday deals!")

    print (" ")
#    print ('There are ',cmdelta.days, ' days to Cyber Monday')
    print ('There are ',delta.days, ' days to Christmas')


#code to run first function if program is started in interpreter
if __name__ == "__main__":
  proceed_shopdays()





