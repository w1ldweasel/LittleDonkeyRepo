# -*- coding: utf-8 -*-
"""
Spyder Editor

Program to calculate xmas (Cyber Monday) savings budget.
By Max Ng
"""

#!/python


from datetime import datetime
from datetime import date
from decimal import *

def main():
    get_days_to_xmas()
    get_monthly_savings()

def get_days_to_xmas():
    today = date.today()
    this_year = today.year
    xmas_day = date(this_year, 12, 25)
    next_yr_xmas_day = date(this_year + 1, 12, 25)
    
#    print (this_year)
#    print (xmas_day)
#    print (next_yr_xmas_day)
    
    print('\n')   
    #print ('Today\'s date is ', datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))
    print ('Today\'s date is ', datetime.now().strftime("%d %B %Y"))
    
    if today < xmas_day:
        days_to_xmas = xmas_day - today
        print ('There are ', days_to_xmas.days, ' days to xmas')
    elif today == xmas_day:
        print ('Its Christmas today!')
    else:     
        print ('There are ', (next_yr_xmas_day - today).days, ' days to Christmas next year.')
        
def get_monthly_savings():
    today = date.today()
    this_year = today.year
    #next_year = today.year + 1
    this_month = today.month
    
    if today <= date(this_year, this_month, 20): 
        add_first_month = 1
    else: add_first_month = 0 
    """Only including this month towards saving if it is on or before pay day (20th) for the month
    Allowing the salary to be included if pay day is 1-2 days earlier if 20th is on the weekend
    Can add simple check to exclude if week of the day is Saturday or Sunday"""
         
    print ('What is your target savings amount for Cyber Monday?')
    
    valid_amount = False
    while valid_amount == False:
        try: 
            getcontext().clear_flags()
            saving_target_input = input('Enter savings figure: £ ')  
            saving_target = Decimal(saving_target_input).quantize(Decimal('0.01'), rounding=ROUND_UP)
#            print (saving_target)
#            print(getcontext().flags )
            if getcontext().flags[Inexact] == False:
                valid_amount = True
            else: 
                print ('Invalid monetary amount entered, please try again.')
        except InvalidOperation:
            print ('Invalid savings amount entered, please try again.')
            valid_amount = False
        
    month_count = 0    
    current_month = this_month + 1

    while current_month < 12:
        current_month = current_month + 1
        month_count = month_count + 1

    month_count = month_count + add_first_month

    if month_count == 0:
        monthly_saving = saving_target/12
        message = 'You\'ve passed the point to save for spending this year, for next Cyber Monday you need to save '
    else: 
        monthly_saving = saving_target / month_count
        message = 'To hit your target by Cyber Monday you need to save '
    
    print (message, '£',Decimal(monthly_saving).quantize(Decimal('.01'), rounding=ROUND_UP), 'each month')
        
if __name__ == '__main__': main()


