# -*- coding: utf-8 -*-
"""
Spyder Editor

Program to calculate xmas savings budget.
By Max Ng
"""

#!/python


from datetime import datetime
from datetime import date

def main():
    
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
        
if __name__ == '__main__': main()


