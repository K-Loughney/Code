#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:33:26 2017

@author: KL
"""

def pulsevpp (filename) :
    
    with open(filename) as d:
    
        d=[x.strip() for x in d if x.strip()]
  
    data=[tuple(map(float,x.split())) for x in d[2:]]
    event=[x[0] for x in data]
    ts=[x[1] for x in data]
    
      
    ch2_vpp=[x[7] for x in data] 
    
    ch3_vpp=[x[10] for x in data]  
    
    ch4_vpp=[x[13] for x in data]    
    
    return (ch2_vpp, ch3_vpp, ch4_vpp)
