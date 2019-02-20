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
    
    print('\n')  
    name = input('What is your name? :') 
    dobinput = input('What is your Date of Birth? Enter in the format DD/MM/CCYY :') 
    dob = datetime.strptime( dobinput, '%d/%m/%Y')  
    
    age_years = relativedelta(today, dob).years
    
    print('\n') 
    print('Hello World!')       
    print ('Hello ', name, ' !')
    print ('You are ', age_years, '!')
    if today.month == dob.month:
        if today.day == dob.day:
            print('Happy Birthday ', name, '!')
        else:print('Bye')
    else:print('Bye')
 
    
if __name__ == '__main__': main()
