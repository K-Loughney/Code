#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:03:44 2017

@author: shas
"""


trig = 0
histch1 = []
histch2 = []
histch3 = []
histch4 = []

def pulseheight (filename) :
    
    with open(filename) as d:
    
        d=[x.strip() for x in d if x.strip()]
  
    data=[tuple(map(float,x.split())) for x in d[2:]]
    event=[x[0] for x in data]
    ts=[x[1] for x in data]
    
    ch1_vpp=[x[4] for x in data]
    histch1.append(ch1_vpp)
    
    ch2_vpp=[x[7] for x in data] 
    histch2.append(ch2_vpp)
    
    ch3_vpp=[x[10] for x in data]  
    histch3.append(ch3_vpp)
    
    ch4_vpp=[x[13] for x in data]    
    histch4.append(ch4_vpp)
    
    return (histch1, histch2, histch3, histch4)
