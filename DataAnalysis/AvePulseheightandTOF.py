#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:18:51 2017

@author: KL
"""
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
import timeofflight as t

filename = '6_detContCollect_NewDetArray4_multiplex_ch3andch4_Run4'
with open(filename + '.dat') as d:
    
    d=[x.strip() for x in d if x.strip()]
  
    data=[tuple(map(float,x.split())) for x in d[2:]]
    event=[x[0] for x in data]
    ts=[x[1] for x in data]
    ch1_t=np.asarray([x[3] for x in data])
    ch2_t=np.asarray([x[6] for x in data])
    ch3_t=np.asarray([x[9] for x in data])
    ch4_t=np.asarray([x[12] for x in data])
        
    del2 = ch2_t - ch1_t
    del3 = ch3_t - ch1_t
    del4 = ch4_t - ch1_t
      
    ch2_vpp=[x[7] for x in data] 

    ch3_vpp=[x[10] for x in data]  

    ch4_vpp=[x[13] for x in data] 
    
    a, b, c = t.timeofflight(filename+'.dat')

    ph_cut3 = np.squeeze(np.asarray(ch3_vpp)>15)
    ph_cut4 = np.squeeze(np.asarray(ch4_vpp)>12)

    C3_ph = np.asarray(ch3_vpp)[ph_cut3]
    C4_ph = np.asarray(ch4_vpp)[ph_cut4]

    ave2 = sum(C3_ph)/(len(C3_ph))
    ave3 = sum(C4_ph)/(len(C4_ph))
    
    t_cut2 = (a>0)&(a<35)
    t_cut3 = (b>0)&(b<26)
    t_cut4 = (c>0)&(c<28)    
    
    C2_t = np.asarray(del2)[t_cut2]
    C3_t = np.asarray(del3)[t_cut3]
    C4_t = np.asarray(del4)[t_cut4]
    
    C2t = sum(C2_t)/len(C2_t)
    C3t = sum(C3_t)/len(C3_t)
    C4t = sum(C4_t)/len(C4_t) 
    
    C3tph_cut = ((b>0)&(b<27))&(np.squeeze(np.asarray(ch3_vpp)>15))
    C4tph_cut = ((c>0)&(c<30))&(np.squeeze(np.asarray(ch4_vpp)>12))


    C3_tph = np.asarray(del3)[C3tph_cut]
    C4_tph = np.asarray(del4)[C4tph_cut]
    
    C3tph = sum(C3_tph)/len(C3_tph)
    C4tph = sum(C4_tph)/len(C4_tph)

print(ave2)
print(ave3)

print(C3tph)
print(C4tph)

Ch3vpp_norm = ch3_vpp/ave2
Ch4vpp_norm =ch4_vpp/ave3

Ch3t_norm = del3/C3tph
Ch4t_norm = del4/C4tph

plt.hist2d(Ch3t_norm, Ch3vpp_norm, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,200)
plt.title('2D Pulse Height Vs Time of Flight (28.09.17 - 04.10.17) - CH3')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
plt.axis([0,5, 0, 4])
plt.savefig(filename+'_PH_TOF2DCOLNORM_CH3.png')
plt.clf()

plt.hist2d(Ch4t_norm, Ch4vpp_norm, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,200)
plt.title('2D Pulse Height Vs Time of Flight (28.09.17 - 04.10.17) - CH4')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
plt.axis([0,5, 0, 4])
plt.savefig(filename+'_PH_TOF2DCOLNORM_CH4.png')
plt.clf()

Vpp_diff = (Ch4vpp_norm - Ch3vpp_norm)
T_diff = (Ch3t_norm - Ch4t_norm)

plt.hist2d(Ch3t_norm, Vpp_diff, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,200)
plt.title('2D Pulse Height Vs Time of Flight (28.09.17 - 04.10.17) - Difference')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
plt.axis([0,5, -5, 5])
plt.savefig(filename+'_PH_TOF2DCOLNORM_DiffCH4-CH3.png')
plt.clf()
