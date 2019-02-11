# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a hello world program file.
By Max Ng
"""

#!/python

from datetime import date
from datetime import datetime
from datetime import timedelta


def main():
    
    today = datetime.now()
    
    print('\n')  
    name = input('What is your name? :') 
    dobinput = input('What is your Date of Birth? Enter in the format DD/MM/CCYY :') 
    dob = datetime.strptime( dobinput, '%d/%m/%Y')  
    
    # print (dob.strftime('%d/%m/%Y') )
    age = today - dob
    
    print('\n') 
    print('Hello World!')       
    print ('Hello ', name, '!')
    print ('You are ', age, '!')
    print('\n')  

    
if __name__ == '__main__': main()
