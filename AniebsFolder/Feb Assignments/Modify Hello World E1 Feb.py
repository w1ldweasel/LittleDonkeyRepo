# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:00:24 2019

@author: Anieb
"""
from datetime import datetime, date
today = date.today()


string1 = ("hello, World!")
name = input ("Enter your name-->")


print("Please Enter Your date of birth using the following format (yyyy mm dd)")

date_of_birth = datetime.strptime(input("Type here-->"), "%Y %m %d")

string2 = ("Hello  " + name)
string3 = ("Your age is ")
string4 = ("You are now")

def cal_age(DOB):
    
    if ((today.month, today.day) == (DOB.month, DOB.day)):
        print ("Happy Birthday " + name + ("!! Wishing you a great day!!"))
        print (string4)
    elif  ((today.month, today.day) != (DOB.month, DOB.day)):
        print ("Hello " + name )
        print (string1, string3)        
    
    return today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))

age = cal_age(date_of_birth) 
print(age)