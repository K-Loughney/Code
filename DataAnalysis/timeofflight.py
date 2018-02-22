#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:44:54 2017

@author: shas
"""
import numpy as np

def timeofflight ( filename, cuts=[-1]) :
    
    
    with open(filename) as d:
    
        d=[x.strip() for x in d if x.strip()]
  
    data=[tuple(map(float,x.split())) for x in d[2:]]
    #ts=[x[1] for x in data]
    ch1_t=np.asarray([x[3] for x in data])
    ch2_t=np.asarray([x[6] for x in data])
    ch3_t=np.asarray([x[9] for x in data])
    ch4_t=np.asarray([x[12] for x in data])
        
    del2 = ch2_t - ch1_t
    del3 = ch3_t - ch1_t
    del4 = ch4_t - ch1_t
        
    if len(cuts)==1:
        cuts=np.ones(del2.shape, dtype=bool)
        
    print (cuts)
        
    return (del2[cuts], del3[cuts], del4[cuts])

        
        
        
