# -*- coding: utf-8 -*-
"""
Spyder Editor

Program to calculate gradient of line from user input.
By Max Ng
"""

import matplotlib.pyplot as plt 
from decimal import Decimal

def main():
    get_values()

def get_values():
    
    inputs_valid = False
    
    while inputs_valid == False:    
        try: 
            x_value = input('Enter final x value: ') 
            x_value = int(x_value)
    
            m_value = input('Enter m value the line gradient: ')
            #m_value = int(m_value)
            m_value = Decimal(m_value).quantize(Decimal('0.01'), rounding=ROUND_UP)
            c_value = input('Enter c value, the intersection with y: ')
            #c_value = int(c_value)
            c_value = Decimal(c_value).quantize(Decimal('0.01'), rounding=ROUND_UP)
            
            x_list = list(range(x_value + 1))
            y_list = []
#            for x in x_list:
#                y_list.append(x * m_value)
#            print (x_list)
    
            plot_graph(x_list, x_list)
#            plt.plot(x_list, x_list, c_value)
                
        except ValueError:
            print('Please enter x as an integer and valid numbers for m and c')
            user_reply = input('Do you want to continue (enter y to continue)?: ')
            if user_reply.low() == 'y':
                main()
            else: print('Bye')
            
        except:
            print('Problem processing input try again')
            user_reply = input('Do you want to continue (enter y to continue)?: ')
            if user_reply.low() == 'y':
                main()
            else: print('Bye')

def plot_graph(x_values, y_values, c_value):
    # plotting the points  
    plt.plot(x_values, y_values, color='green', linestyle='dashed', linewidth = 3, 
    marker='o', markerfacecolor='blue', markersize=12) 
    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis') 
  
    plt.title('Line Gradient') 
  
    plt.show() 


if __name__ == "__main__":
    main()
