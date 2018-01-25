#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:09:50 2017

@author: KL
"""
import numpy as np
import pulsevpp as vpp
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

filename = '3Triplets_BankArray_MultiplexAll_Run2_HV1_900Vch1andch2_HV2_625Vch1_800Vch2'

with open(filename+'.dat') as d:
    
    d=[x.strip() for x in d if x.strip()]
  
data=[tuple(map(float,x.split())) for x in d[2:]]
#ts=[x[1] for x in data]
ch1_t=np.asarray([x[3] for x in data])
ch2_t=np.asarray([x[6] for x in data])
ch3_t=np.asarray([x[9] for x in data])

ch1_tcut1 = np.squeeze(np.asarray(ch1_t)<430)
ch1_tcut2 = np.squeeze((np.asarray(ch1_t)>430)&(np.asarray(ch1_t)<490))
ch1_tcut3 = np.squeeze(np.asarray(ch1_t)>490)


del1 = ch1_tcut3 - ch2_t    
del2 = ch2_t - ch1_tcut3
del3 = ch3_t - ch1_tcut3
del4 = ch1_tcut3 - ch3_t

ch1vpp, ch2vpp, ch3vpp = vpp.pulsevpp(filename+'.dat')

plt.hist2d(del1, ch1vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,100)
plt.title('2D Pulse Height Vs Time of Flight (30.11.17 - 07.12.17) - CH1')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
#plt.axis([-200,200, 20, 300])
plt.savefig(filename+'_PH_TOF2DCOL_CH1_490cut.png')
plt.clf()

plt.hist2d(del4, ch1vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,100)
plt.title('2D Pulse Height Vs Time of Flight (30.11.17 - 07.12.17) - CH1(b)')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
#plt.axis([-200,200, 20, 100])
plt.savefig(filename+'_PH_TOF2DCOL_CH1bred_490cut.png')
plt.clf()

plt.hist2d(del2, ch2vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,100)
plt.title('2D Pulse Height Vs Time of Flight (30.11.17 - 07.12.17) - CH2')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
#plt.axis([-200,200, 30, 400])
plt.savefig(filename+'_PH_TOF2DCOL_CH2_490cut.png')
plt.clf()

plt.hist2d(del3, ch3vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,100)
plt.title('2D Pulse Height Vs Time of Flight (30.11.17 - 07.12.17) - CH3')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
#plt.axis([-200,200, 40, 400])
plt.savefig(filename+'_PH_TOF2DCOL_CH3_490cut.png')
plt.clf()
