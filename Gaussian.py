#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:02:16 2017

@author: shas
"""
import matplotlib.pyplot as plt
import timeofflight as t
import eventrate as e
from scipy.optimize import curve_fit
import numpy as np

b, c, d = t.timeofflight("4_det_Cont_Collection.dat")

#plt.hist(b, 800, normed =1, facecolor='yellow', alpha=0.75)
#plt.xlabel('Time/ ns'), plt.ylabel('Frequency'), plt.title('Time of Flight CH2: August 2017')
#plt.axis([-50,50, 0, 0.01]) 
plt.clf()
hist, bin_edges = np.histogram(d, 425)
BE = np.zeros(425)
for i,be in enumerate(bin_edges):
    if i<(len(bin_edges)-1):
        BE[i] = (bin_edges[i+1] + bin_edges[i])*0.5
        
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

CutB = (BE>-25)&(BE<25)
BE = BE[CutB]
hist=hist[CutB]
popt, pcov = curve_fit(gauss_function, BE, hist, p0 = [1, 0, 5], maxfev=20000)

plt.plot(BE, gauss_function(BE, *popt), label='Fit', color = 'blue')
plt.plot(BE, hist,'green', label='Data')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Time/ ns'), plt.ylabel('Frequency'), plt.title('Time of Flight CH4: June-July 2017')
#plt.axis([-50,50, 0, 0.005]) 
print (popt)
plt.savefig('4ContColOD_CH4_Gauss.png')
