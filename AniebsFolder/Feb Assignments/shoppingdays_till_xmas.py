# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:27:20 2019

@author: Anieb
"""

import datetime

now = datetime.datetime.now()
dt = datetime.datetime

currentyear = now.year

delta = dt(currentyear, 12, 2) - now
print ("current Date: " + now.strftime("%d - %b - %Y"))

SavingTarget = input ("Please enter how much you would like to save £")
SavingTargetConvert = int(SavingTarget) * 1
print ("in order to save £" + SavingTarget + ' for Cyber monday') 

MonthCalculation = (delta.days / 7 / 4)


MonthlySaving = (SavingTargetConvert / MonthCalculation)
MonthlySavingAmount = float(MonthlySaving) *1
MonthlySavingAmount = str(round(MonthlySavingAmount, 2))


MonthCalculation = str(round(MonthCalculation, 2))
SavingTargetConvert = str(round(SavingTargetConvert, 2))

print ("You need to save £" + MonthlySavingAmount + " a month for the next " + MonthCalculation + " Months")
print ("There are only",delta.days, 'days to Cyber Monday Get Saving to Reach Your Goal!!')

"""
MN 
The value of Cyber Monday has been hardcoded, that is a programming no no
This calculation will be more precise by calculating the number of pay days to christmas 
or even more correct depending on which part of the month its run
"""
