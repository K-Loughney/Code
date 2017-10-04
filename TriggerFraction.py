#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:23:49 2017

@author: KL
"""
import matplotlib.pyplot as plt
import pandas as pd
import pulseheight as ph
import numpy as np
import timeofflight as t
import math
TS = []

histTDiff = []
histch1 = []
filename = '4_det_Cont_Collection'
with open(filename+'.dat') as d:
    d=[x.strip() for x in d if x.strip()]
    data=[tuple(map(float,x.split())) for x in d[2:]]
    event=[x[0] for x in data]
    ts=[x[1] for x in data]
    
    CH1=[x[2] for x in data]
    CH2=[x[5] for x in data]
    CH3=[x[8] for x in data]
    CH4=[x[11] for x in data]
    

    h1, h2, h3, h4 = ph.pulseheight(filename+'.dat')
    a, b, c = t.timeofflight(filename+'.dat')
    
    ph_cut1 = np.squeeze(np.asarray(h1)>20)
    ph_cut2 = np.squeeze(np.asarray(h2)>50)
    ph_cut3 = np.squeeze(np.asarray(h3)>45)
    ph_cut4 = np.squeeze(np.asarray(h4)>25)
      
    C2_ph = np.asarray(CH2)[ph_cut2]
    C3_ph = np.asarray(CH3)[ph_cut3]
    C4_ph = np.asarray(CH4)[ph_cut4]
    
    C2p = len(C2_ph)/len(CH2)
    C3p = len(C3_ph)/len(CH3)
    C4p = len(C4_ph)/len(CH4) 
    
    t_cut2 = (a>-25)&(a<25)
    t_cut3 = (b>-25)&(b<25)
    t_cut4 = (c>-25)&(c<25)    
    
    C2_t = np.asarray(CH2)[t_cut2]
    C3_t = np.asarray(CH3)[t_cut3]
    C4_t = np.asarray(CH3)[t_cut4]
    
    C2t = len(C2_t)/len(CH2)
    C3t = len(C3_t)/len(CH3)
    C4t = len(C4_t)/len(CH4) 
    
    C2tph_cut = ((a>-25)&(a<25))&(np.squeeze(np.asarray(h2)>20))
    C3tph_cut = ((b>-25)&(b<25))&(np.squeeze(np.asarray(h3)>20))
    C4tph_cut = ((c>-25)&(c<25))&(np.squeeze(np.asarray(h4)>20))

    C2_tph = np.asarray(CH2)[C2tph_cut]
    C3_tph = np.asarray(CH3)[C3tph_cut]
    C4_tph = np.asarray(CH4)[C4tph_cut]
    
    C2E = (1/(math.sqrt(len(C2_tph))))+(1/(math.sqrt(len(CH2))))
    C3E = (1/(math.sqrt(len(C3_tph))))+(1/(math.sqrt(len(CH3))))
    C4E = (1/(math.sqrt(len(C4_tph))))+(1/(math.sqrt(len(CH4))))   
    
    
    C2tph = len(C2_tph)/len(CH2)
    C3tph = len(C3_tph)/len(CH3)
    C4tph = len(C4_tph)/len(CH4)     
    
    
print ('CH2 Voltage Cuts:', C2p)
print ('CH3 Voltage Cuts:', C3p)
print ('CH4 Voltage Cuts:', C4p)

print ('CH2 TOF Cuts:', C2t)
print ('CH3 TOF Cuts:', C3t)
print ('CH4 TOF Cuts:', C4t)

print ('CH2 Voltage and TOF Cuts:', C2tph, '+/- ', C2E*C2tph)
print ('CH3 Voltage and TOF Cuts:', C3tph, '+/- ', C3E*C3tph)
print ('CH4 Voltage and TOF Cuts:', C4tph, '+/- ', C4E*C4tph)
   