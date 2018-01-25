#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:41:34 2017

@author: KL
"""

import numpy as np
import pulsevpp as vpp
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

filename = '3Triplets_BankArray_MultiplexAll_switched_Run6_HV1_900Vch1_850ch2_HV2_625Vch1_800Vch2'

ch1vpp, ch2vpp, ch3vpp = vpp.pulsevpp(filename+'.dat')

with open(filename+'.dat') as d:
    
    d=[x.strip() for x in d if x.strip()]
  
data=[tuple(map(float,x.split())) for x in d[2:]]
#ts=[x[1] for x in data]
ch1_t=np.asarray([x[3] for x in data])
ch2_t=np.asarray([x[6] for x in data])
ch3_t=np.asarray([x[9] for x in data])

tcut1 = np.asarray(ch1_t)<430
tcut2 = (np.asarray(ch1_t)>430)&(np.asarray(ch1_t)<490)
tcut3 = np.asarray(ch1_t)>490



Ch1Cut1 = ch1_t[tcut1]
Ch1Cut2 = ch1_t[tcut2]
Ch1Cut3 = ch1_t[tcut3]

Ch2Cut1 = ch2_t[tcut1]
Ch2Cut2 = ch2_t[tcut2]
Ch2Cut3 = ch2_t[tcut3]

Ch3Cut1 = ch3_t[tcut1]
Ch3Cut2 = ch3_t[tcut2]
Ch3Cut3 = ch3_t[tcut3]

###################################################

n, bins, patches = plt.hist((Ch2Cut1-Ch1Cut1), bins=np.linspace(-150,150,200), normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('Ch2 Cut 1 TOF (12.12.17 - 14.12.17)')
ax = plt.axes()    
#plt.axis([200,600, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_C2Cut1-C1Cut1.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist((Ch2Cut2-Ch1Cut2), bins=np.linspace(-150,150,200), normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('Ch2 Cut 2 TOF (12.12.17 - 14.12.17)')
ax = plt.axes()    
#plt.axis([200,600, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_C2Cut2-C1Cut2.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist((Ch2Cut3-Ch1Cut3), bins=np.linspace(-150,150,200), normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('Ch2 Cut 3 TOF (12.12.17 - 14.12.17)')
ax = plt.axes()    
#plt.axis([200,650, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_C2Cut3-C1Cut3.png', bbox_inches = 'tight')
plt.clf()
###################################################

n, bins, patches = plt.hist((Ch3Cut1-Ch1Cut1), bins=np.linspace(-150,150,200), normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('Ch3 Cut 1 TOF (12.12.17 - 14.12.17)')
ax = plt.axes()    
#plt.axis([200,600, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_C3Cut1-C1Cut1.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist((Ch3Cut2-Ch1Cut2), bins=np.linspace(-150,150,200), normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('Ch3 Cut 2 TOF (12.12.17 - 14.12.17)')
ax = plt.axes()    
#plt.axis([200,600, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_C3Cut2-C1Cut2.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist((Ch3Cut3-Ch1Cut3), bins=np.linspace(-150,150,200), normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('Ch3 Cut 3 TOF (12.12.17 - 14.12.17)')
ax = plt.axes()    
#plt.axis([200,650, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_C3Cut3-C1Cut3.png', bbox_inches = 'tight')
plt.clf()

###################################################
###################################################

n, bins, patches = plt.hist(Ch2Cut1, bins=np.linspace(200,650,200), normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH2 Trigger Times (12.12.17 - 14.12.17)')
ax = plt.axes()    
plt.axis([200,600, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_Ch2Cut1.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist(Ch2Cut2, bins=np.linspace(200,650,200), normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH2 Trigger Times (12.12.17 - 14.12.17)')
ax = plt.axes()    
plt.axis([200,600, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_Ch2Cut2.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist(Ch2Cut3, bins=np.linspace(200,650,200), normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH2 Trigger Times (12.12.17 - 14.12.17)')
ax = plt.axes()    
plt.axis([200,650, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_Ch2Cut3.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist(Ch3Cut1, bins=np.linspace(200,650,200), normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH3 Trigger Times (12.12.17 - 14.12.17)')
ax = plt.axes()    
plt.axis([200,600, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_Ch3Cut1.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist(Ch3Cut2, bins=np.linspace(200,650,200), normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH3 Trigger Times (12.12.17 - 14.12.17)')
ax = plt.axes()    
plt.axis([200,650, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_Ch3Cut2.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist(Ch3Cut3, bins=np.linspace(200,650,200), normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH3 Trigger Times (12.12.17 - 14.12.17)')
ax = plt.axes()    
plt.axis([200,650, 0, 0.03])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_TrigTime_Ch3Cut3.png', bbox_inches = 'tight')
plt.clf()

