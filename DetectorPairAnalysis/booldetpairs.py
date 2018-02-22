#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:22:08 2018

@author: KL
"""
import numpy as np
import pandas as pd
import datetime as dt
import presscordatacut as pcdc
import weather_underground_parser as wp

start_datetime = dt.datetime(2018,2,22)
end_datetime = dt.datetime(2018,2,22)
loc = "airport/EGLL"
hp = wp.weather_underground_parser(start_datetime,end_datetime, loc)
pres = hp.pressure

P0 = 1000
A =132

def booldetpairs (filename, x,y,z):
    ts, detp1, detp2, timestamp = pcdc.presscordatacut(filename)
    ## Finds timestamp for detector pairs
    for i,p1 in enumerate(detp1):
        if (detp1[i] == x) and (detp2[i] == y):
            z.append(timestamp[i]/1000)
    return z

def timecorrection(z, hour):
    hour = pd.to_datetime((np.floor(np.asarray(z[:])/60./60.)*60.*60.), unit = 's')
    return hour


def pressurecorrection(hour,hourblock,hourcount,avehc,avehcpress):
    while len(hour)>0:
        indie = (hour==hour[0])
        hourblock.append(hour[0])
        hour = np.delete(hour, np.where(indie))
        hourcount.append(sum(indie)) ## Hourly countrate for muons.
        avehc = np.average(hourcount)
        for i,x in enumerate(hourblock):
            hppress = hp.get_pressure(x)        ##Pressure from weather underground for Heathrow airport
            Pressure_Correction = np.exp((hppress - P0)/A)  ## Pressure Correction 
            l = np.multiply(hourcount,Pressure_Correction) ## Pressure Corrected Countrate
        avehcpress = np.average(l)
    return avehc, avehcpress

