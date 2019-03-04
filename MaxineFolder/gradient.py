#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:14:28 2019

@author: maxinemcfarlane
"""

import matplotlib.pyplot as plt
import numpy as np

m = int(input("What is the graident? "))
c = int(input("What is the initial value? "))

#print (c, m)

x = np.arange(0, 30)
y = (m*x) + c
plt.plot(x,y)
plt.show()