#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:48:58 2017

@author: KL
"""
import numpy as np
import matplotlib.pyplot as plt

dist = 1.70
"""Distance between detectors in meters"""

detH = (0.155)
"""height of each detector"""

Height1 = []
Height2 = []
Height3 = []
Height4 = []
Height5 = []

"""
Generate random numbers within a range - random.uniform is used for decimal values
This will create a list of random numbers, the length of which can be changed."""

Height1.append(np.random.uniform(0, 0.155, 25))
Height2.append(np.random.uniform(0.155, 0.310, 25))
Height3.append(np.random.uniform(0.310, 0.465, 25))
Height4.append(np.random.uniform(0.465, 0.620, 25))
Height5.append(np.random.uniform(0.620, 0.775, 25))
#print('Random heights 1: ', Height1)
#print('Random heights 1: ', Height2)
#print('Random heights 1: ', Height3)
#print('Random heights 1: ', Height4)
#print('Random heights 1: ', Height5)


"""
 For each value in the list of random numbers, the path length is calculated
 using A^2 + B^2 = C^2 
 2.89 is the square of the measured distance between the detectors."""
 
for x in Height1:
    l1 = np.sqrt(2.89+(x**2))
for x in Height2:
    l2 = np.sqrt(2.89+(x**2))
for x in Height3:
    l3 = np.sqrt(2.89+(x**2))
for x in Height4:
    l4 = np.sqrt(2.89+(x**2))
for x in Height5:
    l5 = np.sqrt(2.89+(x**2))
print ('Length 1: ', l1)   
print ('Length 2: ', l2)
print ('Length 3: ', l3)   
print ('Length 4: ', l4) 
print ('Length 5: ', l5)

plt.scatter(Height1, l1, s=15, c='m', marker="o", label='Detector PL05')
plt.scatter(Height2, l2, s=15, c='b', marker="^", label='Detector PL04')
plt.scatter(Height3, l3, s=10, c='c', marker="s", label='Detector PL03')
plt.scatter(Height4, l4, s=15, c='g', marker="p", label='Detector PL02')
plt.scatter(Height5, l5, s=15, c='r', marker="h", label='Detector PL01')
plt.legend(loc=0)
plt.xlabel('Height/m')
plt.ylabel('Path Length/m')
plt.show()
    