# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:03:34 2019

@author: Anieb
"""
import numpy as np
import matplotlib.pyplot as plt

#def inputval():
while True:
    try:
        val_c = int(input( 'what is the initial value?'))
        val_m = int(input('what is the gradient?'))
        break
    except ValueError:
        print('Please use Integers only')
        
val_x = np.arange(0,50)
            
val_y = (val_m*val_x) + val_c
            
plt.scatter(val_x,val_y)

plt.suptitle('Introduction to Graphs')
                    
plt.show()

    
        
#if __name__ == "__main__":
 #  inputval()