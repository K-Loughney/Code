#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:21:27 2017

@author: KL
"""

import numpy as np
import pulsevpp as vpp
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

filename = '3Triplets_BankArray_MultiplexAll_Run3_HV1_900Vch1andch2_HV2_625Vch1_800Vch2'

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
#####################################

C1t = np.asarray(ch1_t)
C2t = np.asarray(ch2_t)
C3t = np.asarray(ch3_t)

C1C1 = np.asarray(Ch1Cut1)
C1C2 = np.asarray(Ch1Cut2)
C1C3 = np.asarray(Ch1Cut3)

C2C1 = np.asarray(Ch2Cut1)
C2C2 = np.asarray(Ch2Cut2)
C2C3 = np.asarray(Ch2Cut3)

C3C1 = np.asarray(Ch3Cut1)
C3C2 = np.asarray(Ch3Cut2)
C3C3 = np.asarray(Ch3Cut3)

#####################################

nC1, bins, patches = plt.hist(ch1_t, bins=np.linspace(300,650,200), normed =1, alpha=0.75)

nC2, bins, patches = plt.hist(ch2_t, bins=np.linspace(300,650,200), normed =1, alpha=0.75)

nC3, bins, patches = plt.hist(ch3_t, bins=np.linspace(300,650,200), normed =1, alpha=0.75)

nC2C1, bins, patches = plt.hist(Ch2Cut1, bins=np.linspace(300,650,200), normed =1, facecolor='blue', alpha=0.75)

nC2C2, bins, patches = plt.hist(Ch2Cut2, bins=np.linspace(300,650,200), normed =1, facecolor='blue', alpha=0.75)

nC2C3, bins, patches = plt.hist(Ch2Cut3, bins=np.linspace(300,650,200), normed =1, facecolor='blue', alpha=0.75)

nC3C1, bins, patches = plt.hist(Ch3Cut1, bins=np.linspace(300,650,200), normed =1, facecolor='red', alpha=0.75)

nC3C2, bins, patches = plt.hist(Ch3Cut2, bins=np.linspace(300,650,200), normed =1, facecolor='red', alpha=0.75)

nC3C3, bins, patches = plt.hist(Ch3Cut3, bins=np.linspace(300,650,200), normed =1, facecolor='red', alpha=0.75)

#####################################
plt.plot(bins[:-1], nC2C1/nC2)
plt.show()
#plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH2 (Trigger Times<430ns) (07.12.17 - 12.12.17)')
#ax = plt.axes()    
#plt.axis([200,600, 0, 0.02])  
#ax.yaxis.grid(True, linewidth=0.5) 
#ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig(filename+'_TrigTime_Cut1C2.png')
#plt.clf()

#plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH2 (430ns<Trigger Times<490ns) (07.12.17 - 12.12.17)')
#ax = plt.axes()    
#plt.axis([350,600, 0, 0.02])  
#ax.yaxis.grid(True, linewidth=0.5) 
#ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig(filename+'_TrigTime_Cut2C2.png')
#plt.clf()

#plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH2 (Trigger Times>490ns) (07.12.17 - 12.12.17)')
#ax = plt.axes()    
#plt.axis([350,650, 0, 0.02])  
#ax.yaxis.grid(True, linewidth=0.5) 
#ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig(filename+'_TrigTime_Cut3C2.png')
#plt.clf()

#plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH3 (Trigger Times<430ns) (07.12.17 - 12.12.17)')
#ax = plt.axes()    
#plt.axis([200,600, 0, 0.02])  
#ax.yaxis.grid(True, linewidth=0.5) 
#ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig(filename+'_TrigTime_Cut1C3.png')
#plt.clf()

#plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH3 (430ns<Trigger Times<490ns) (07.12.17 - 12.12.17)')
#ax = plt.axes()    
#plt.axis([350,650, 0, 0.02])  
#ax.yaxis.grid(True, linewidth=0.5) 
#ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig(filename+'_TrigTime_Cut2C3.png')
#plt.clf()

#plt.xlabel('Time/ns'), plt.ylabel(''), plt.title('CH3 (Trigger Times>490ns) (07.12.17 - 12.12.17)')
#ax = plt.axes()    
#plt.axis([350,650, 0, 0.02])  
#ax.yaxis.grid(True, linewidth=0.5) 
#ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig(filename+'_TrigTime_Cut3C3.png')
#plt.clf()