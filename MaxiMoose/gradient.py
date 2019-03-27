# -*- coding: utf-8 -*-
"""
Spyder Editor

Program to calculate gradient of line from user input.
By Max Ng
"""

import matplotlib.pyplot as plt 
from decimal import *

def main():
    get_values()
    print('End')

def get_values():
    do_not_continue = False
    while do_not_continue == False:    
        try: 
            x_value = input('Enter final x value as an integer: ') 
            x_value = int(x_value)
    
            m_value_input = input('Enter m value the line gradient: ')
            m_value = Decimal(m_value_input).quantize(Decimal('0.01'), rounding=ROUND_UP)
            c_value_input = input('Enter c value, the intersection with y: ')
            c_value = Decimal(c_value_input).quantize(Decimal('0.01'), rounding=ROUND_UP)
            x_list = list(range(x_value + 1))
            x_axis = []
            y_axis = []
            for x in x_list:
                x_decimalised = Decimal(x)
                y = (x_decimalised * m_value + c_value)
                xval = float(x)
                yval = float(y)
                x_axis.append(xval)
                y_axis.append(yval)
#            print (x_axis)
#            print (y_axis)
            do_not_continue = True
            plot_graph(x_axis, y_axis)
         
        except ValueError:
            print('Please enter x as an integer and valid numbers for m and c')
            user_reply = input('Do you want to continue (enter y to continue)?: ')
            if user_reply.lower() == 'y':
                main()
            else: 
                do_not_continue = True
      
        except:
            print('Problem processing input')
            user_reply = input('Do you want to continue (enter y to continue)?: ')
            if user_reply.lower() == 'y':
                main()
            else: 
                do_not_continue = True

        
def plot_graph(x_values, y_values):
    # plotting the points  
    plt.plot(x_values, y_values, color='green', linestyle='solid', linewidth = 1, 
    marker='o', markerfacecolor='red', markersize=6) 
    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis') 
    plt.title('Line Gradient') 
    plt.show() 


if __name__ == "__main__":
    main()
