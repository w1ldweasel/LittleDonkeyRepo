#! /usr/bin/python

# script to output the number of days until xmas

import datetime

dt = datetime.datetime

thisyear = dt.now().year
delta = dt(thisyear, 12, 25) - dt.now()

#date formating

#example of how much monthly savings give for xmas
print ("If you would like to save £1000 for Christmas, you will need to save " 
       thisamount " pounds a month from now")

#user input
usersave = input("How much do you need to save for Christmas in Pound Sterling?")

#savings calculation


#output to user
print ("To have " usersave " saved for Christmas, you will need to save '
       otheramount ' per month")
print("This will give you " usersave " to spend on Cyber Monday deals!")


print ('There are ',cmdelta.days, ' days to Cyber Monday')
print ('There are ',delta.days, ' days to Christmas')




