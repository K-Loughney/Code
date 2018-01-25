#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:57:33 2017

@author: KL
"""
import numpy as np
import matplotlib.pyplot as plt


filename = '3Triplets_BankArray_MultiplexAll_switched_Run6_HV1_900Vch1_850ch2_HV2_625Vch1_800Vch2'

with open(filename+'.dat') as d:
    
    d=[x.strip() for x in d if x.strip()]
  
data=[tuple(map(float,x.split())) for x in d[2:]]
#ts=[x[1] for x in data]
ch1_t=np.asarray([x[3] for x in data])
ch2_t=np.asarray([x[6] for x in data])
ch3_t=np.asarray([x[9] for x in data])



n, bins, patches = plt.hist(ch1_t, bins=np.linspace(200,650,200), normed =1, facecolor='green', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH1 Trigger Times (12.12.17 - 14.12.17)')
ax = plt.axes()    
plt.axis([400,550, 0, 0.15])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_CH1.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist(ch2_t, bins=np.linspace(200,650,200), normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH2 Trigger Times (12.12.17 - 14.12.17)')
ax = plt.axes()    
plt.axis([200,650, 0, 0.03]) 
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_CH2.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist(ch3_t, bins=np.linspace(200,650,200), normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH3 Trigger Times (12.12.17 - 14.12.17)')
ax = plt.axes()    
plt.axis([200,650, 0, 0.03]) 
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_CH3.png', bbox_inches = 'tight')
plt.clf()