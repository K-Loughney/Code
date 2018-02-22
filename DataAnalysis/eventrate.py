#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:44:54 2017

@author: shas
"""
import numpy as np

def eventrate ( filename, avemins = 1, alldata=False) :
    with open(filename) as d:
    
        d=[x.strip() for x in d if x.strip()]
  
        data=[tuple(map(float,x.split())) for x in d[2:]]
        event=[x[0] for x in data]
        ts=[x[1] for x in data]
    
        originT = ts[0]
            
        RelT = (np.asarray(ts) - originT)/1000
        if alldata:
            averageind = 250
            countrate = np.zeros(RelT.shape)
            for i,rt in enumerate(ts):
                if (i>averageind) and (i<len(RelT)-averageind):
                    RT = np.divide(ts[i-averageind:i+averageind], 1000)
                    RangeT = max(RT)-min(RT)
                    countrate[i] = (2*averageind/RangeT)
            return RelT, countrate
        
        print (type(RelT))
        print (len(RelT))
        hist, bin_edges = np.histogram(RelT, bins=np.arange(0,RelT[-1], 60*avemins))
        timescale = 0.5 + np.arange(0,RelT[-1], 60*avemins)
        return timescale[:-1]/60, hist

        
        
        
