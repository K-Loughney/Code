#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:02:09 2018

@author: KL
"""
import numpy as np
from numpy import ma


def presscordatacut(filename):
    with open(filename+'.dat') as g:
        g=[x.strip() for x in g if x.strip()]
        data=[tuple(map(float,x.split())) for x in g[1:]]
        event=[x[0] for x in data]
        ts=[x[1] for x in data]
        ch1_t=np.asarray([x[3] for x in data])
        ch2_t=np.asarray([x[6] for x in data])
        ch3_t=np.asarray([x[9] for x in data])
        ch4_t=np.asarray([x[12] for x in data])
        
        v1 = np.asarray([x[4] for x in data])
        v2 = np.asarray([x[7] for x in data])
        v3 = np.asarray([x[10] for x in data])
        v4 = np.asarray([x[13] for x in data])
    
    ## Boolean array of all events where the channel has been triggered (>-100)
    ch2tbool = ch2_t > -100
    ch3tbool = ch3_t > -100
    ch4tbool = ch4_t > -100

    ## Time Difference for all events where boolean is True
    timedifference = ch1_t - (ch2tbool*ch2_t + ch3tbool*ch3_t + ch4tbool*ch4_t)
    
    Dtime = ma.array(timedifference)
    
    ## Masks all values outside of the given ranges 
    ## (Returns TRUE if the value has been masked)
    ## Seperates into the different detectors connected to Ch1
    PL01TD = ma.masked_outside(Dtime, 180, 230)
    PL02TD = ma.masked_outside(Dtime, 130, 170)
    PL03TD = ma.masked_outside(Dtime, 92, 104)
    PL04TD = ma.masked_outside(Dtime, 52, 66)
    PL05TD = ma.masked_outside(Dtime, 40, 50)
    PL06TD = ma.masked_outside(Dtime, -5, 10)


    cv11 = (v1 > 45)&(v1<150)
    cv12 = (v1 > 50)&(v1<170)
    cv13 = (v1 > 50)&(v1<130)
    cv14 = (v1 > 145)&(v1<350)
    cv15 = (v1 > 55)&(v1<110)
    cv16 = (v1 > 75)&(v1<200)
    cv2 = (v2 > 50)&(v2<375)
    cv3 = (v3 > 40)&(v3<375)
    cv4 = (v4 > 50)&(v4<375)
    
    ## Convert to Detector number that has been triggered plus corresponding timestamp
    detp1 = 1*np.logical_not(PL01TD.mask)*cv11 + 2*np.logical_not(PL02TD.mask)*cv12+ 3*np.logical_not(PL03TD.mask)*cv13+ 4*np.logical_not(PL04TD.mask)*cv14+ 5*np.logical_not(PL05TD.mask)*cv15+ 6*np.logical_not(PL06TD.mask)*cv16
    detp2 = 7*ch2tbool*cv2 + 8*ch3tbool*cv3 + 9*ch4tbool*cv4
    timestamp = ts*np.logical_not(PL01TD.mask)*cv11 + ts*np.logical_not(PL02TD.mask)*cv12+ ts*np.logical_not(PL03TD.mask)*cv13+ ts*np.logical_not(PL04TD.mask)*cv14+ ts*np.logical_not(PL05TD.mask)*cv15+ ts*np.logical_not(PL06TD.mask)*cv16
    #print(detp1, detp2, timestamp)
    
    return ts, detp1, detp2, timestamp