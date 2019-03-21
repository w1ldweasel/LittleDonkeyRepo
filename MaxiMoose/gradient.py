# -*- coding: utf-8 -*-
"""
Spyder Editor

Program to calculate gradient of line from user input.
By Max Ng
"""

import matplotlib.pyplot as plt 

def main():
    get_values()

def get_values():
    
    try: 
        x_value = input('Enter final x value: ') 
        x_value = int(x_value)

        m_value = input('Enter m value the line gradient: ')
        m_value = int(m_value)
                
        c_value = input('Enter c value, the intersection with y: ')
        c_value = int(c_value)
        
        x_list = list(range(x_value + 1))
#        print (x_list)


        plt.plot(x_list, x_list)
                
    except ValueError:
        print('Please enter integers only')
        main()
        
    except:
        print('Problem processing input try again')
        main()
#    
     


if __name__ == "__main__":
    main()
