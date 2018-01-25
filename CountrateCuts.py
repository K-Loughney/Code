#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:14:49 2017

@author: KL
"""
import numpy as np



def countratecuts ( filename, avemins = 1, alldata=False) :
    with open(filename) as d:
    
        d=[x.strip() for x in d if x.strip()]
  
        data=[tuple(map(float,x.split())) for x in d[2:]]
        event=[x[0] for x in data]
        ts=[x[1] for x in data]
        ch1_vpp=[x[4] for x in data]
        ch2_vpp=[x[7] for x in data] 
        ch3_vpp=[x[10] for x in data]  
        ch4_vpp=[x[13] for x in data]
        
        ph_cut1 = np.squeeze(np.asarray(ch1_vpp)>70)
        ph_cut2 = np.squeeze(np.asarray(ch2_vpp)>70)
        ph_cut3 = np.squeeze(np.asarray(ch3_vpp)>70)
        
        
        originT = ts[0]
              
        RelT = (np.asarray(ts) - originT)/1000
    
        RelTCut1 = (RelT[ph_cut1])
        RelTCut2 = (RelT[ph_cut2])
        RelTCut3 = (RelT[ph_cut3])
    
        if alldata:
            averageind = 250
            countrate = np.zeros(RelTCut2.shape)
            for i,rt in enumerate(ts):
                if (i>averageind) and (i<len(RelTCut1)-averageind):
                    RT = np.divide(ts[i-averageind:i+averageind], 1000)
                    RangeT = max(RT)-min(RT)
                    countrate[i] = (2*averageind/RangeT)
                if (i>averageind) and (i<len(RelTCut2)-averageind):
                    RT = np.divide(ts[i-averageind:i+averageind], 1000)
                    RangeT = max(RT)-min(RT)
                    countrate[i] = (2*averageind/RangeT)
                if (i>averageind) and (i<len(RelTCut3)-averageind):
                    RT = np.divide(ts[i-averageind:i+averageind], 1000)
                    RangeT = max(RT)-min(RT)
                    countrate[i] = (2*averageind/RangeT)
            return (RelTCut2, countrate)
                    
        print(len(RelT))
        print(len(RelTCut1))
        print(len(RelTCut2))
        print(len(RelTCut3))

        hist1, bin_edges = np.histogram(RelTCut1, bins=np.arange(0,RelT[-1], 60*avemins))
        hist2, bin_edges = np.histogram(RelTCut2, bins=np.arange(0,RelT[-1], 60*avemins))
        hist3, bin_edges = np.histogram(RelTCut3, bins=np.arange(0,RelT[-1], 60*avemins))
        timescale = 0.5 + np.arange(0,RelT[-1], 60*avemins)
        return timescale[:-1]/60, hist1, hist2, hist3