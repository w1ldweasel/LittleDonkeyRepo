# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a hello world program file.
By Max Ng
"""

#!/python

from datetime import datetime
from dateutil.relativedelta import relativedelta


def main():
    
    today = datetime.now()
    
    name = input('What is your name? :') 
    valid_date = False
    
    while valid_date == False:

        dobinput = input('What is your Date of Birth? Enter in the format DD/MM/CCYY :') 
        
        try:
            dob = datetime.strptime( dobinput, '%d/%m/%Y')  
            valid_date = True
            if dob > today:
                print('Cannot enter a date in the future, please try again.')
                valid_date = False
        except ValueError:
            print('Not a validate date format, please try again.')
            valid_date = False
        except:
            print('Unexpected error')
            valid_date = False
            raise
              
    age_years = relativedelta(today, dob).years
    
    print('\n') 
    print('Hello World!')       
    print ('Hello ', name, ' !')
    print ('You are ', age_years, '!')
    if today.month == dob.month and today.day == dob.day:
            print('Happy Birthday ', name, '!')
    print('Bye')
 
    
if __name__ == '__main__': main()
