#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 10:51:24 2017

@author: KL
"""
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AA
import weather_underground_parser as wp      ## https://github.com/casteer/weather_underground_parser
from mpl_toolkits.axes_grid1 import host_subplot

TS = []
HrE = []
D2HR = []
TSS = []


filename = '3Triplets_BankArray_MultiplexAll_switched_Run20_HV1_900Vch1__HV2_650Vch1_850Vch2_SingleChBank'

#year=2018
#month=1
#day=16

start_datetime = dt.datetime(2018,1,23)
end_datetime = dt.datetime(2018,1,25)
loc = "airport/EGLL"
hp = wp.weather_underground_parser(start_datetime,end_datetime, loc)
pres = hp.pressure
datetime = hp.datetime
temp = hp.temperature
humid = hp.relative_humidity


tss = [d.strftime('%Y-%m-%d %H:%M') for d in datetime]
   
for x in tss:
    TSS.append(x)
    S = np.asarray(TSS)

#dwh = pd.to_datetime(S[:], unit = 'min')
#Dwh = pd.DatetimeIndex.floor(dwh, 'H')
    

with open(filename+'.dat') as g:
    g=[x.strip() for x in g if x.strip()]
    data=[tuple(map(float,x.split())) for x in g[2:]]
    event=[x[0] for x in data]
    ts=[x[1] for x in data]
    
for x in ts:
    TS.append(x/1000)
    s = TS

d = pd.to_datetime(s[:], unit = 's')
df = pd.DataFrame(d)
TDiff = df.diff()
#print (df)
    
d2 = np.floor(np.asarray(s[:])/60./60.)*60.*60.


d2hr = pd.to_datetime(d2, unit = 's')
df2 = pd.DataFrame(d2hr)
TDiff2 = df.diff() 

##To Obtain the hourly countrate:
while len(d2hr)>0:
    indie = (d2hr==d2hr[0])
    D2HR.append(d2hr[0])
    d2hr = np.delete(d2hr, np.where(indie))
    #print (sum(indie))
    HrE.append(sum(indie))      ## Hourly countrate for muons.
#print(HrE)
R = len(D2HR)
r = len(HrE)


P0 = 1000 #Standard Pressure
A =132    #Atmospheric Constant

for i,x in enumerate(d2):    
    counttime = (dt.datetime.fromtimestamp(x))  ##Event time from dataset
    hppress = hp.get_pressure(counttime)        ##Pressure from weather underground for Heathrow airport
    Pressure_Correction = np.exp((hppress - P0)/A)  ## Pressure Correction 
    HPRESSCORRECT = np.multiply(HrE,Pressure_Correction) ## Pressure Corrected Countrate
    print(counttime, hppress, Pressure_Correction, HPRESSCORRECT) 


plt.xlabel('Time/ Hours'), plt.ylabel('Count rate (1 hour bins)')
plt.plot(D2HR[1:R-1], HrE[1:r-1], label="Uncorrected Countrate")
plt.plot(D2HR[1:R-1], HPRESSCORRECT[1:r-1], label = 'Pressure Corrected Countrate')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.savefig(filename+'_PressureCorrectedCountrate', bbox_inches = 'tight')
plt.clf()
#plt.show()

"""
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
par1 = host.twinx()
offset = 60
#plt.plot(D2HR[1:R-1], HrE[1:r-1])
#plt.plot(Dwh, pres)
host.set_xlabel("Time/hours")
host.set_ylabel("Countrate (1 hour Bins)")
par1.set_ylabel("Pressure/hPa")
p1, = host.plot(D2HR[1:R-1], HrE[1:r-1], label="Countrate")
p2, = par1.plot(Dwh, pres, label="Pressure")
host.legend(bbox_to_anchor=(1.15, 1), loc=2)
host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
#plt.show()


    
    
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
par1 = host.twinx()
offset = 60
#plt.plot(D2HR[1:R-1], HrE[1: r-1], label = 'Uncorrected')
#plt.plot(D2HR[1:R-1], HrECor[1:r-1], label = 'Pressure Corrected')
#plt.plot(Dwh, pres, label = 'Pressure')
host.set_xlabel("Time/hours")
host.set_ylabel("Countrate (1 hour Bins)")
par1.set_ylabel("Pressure/hPa")
p1, = host.plot(D2HR[1:R-1], HrE[1:r-1], label="Uncorrected Countrate")
p2, = host.plot(D2HR[1:R-1], HPRESSCORRECT[1:r-1], label = 'Pressure Corrected Countrate')
#p3, = par1.plot(Dwh, pres, label="Pressure")
host.legend(bbox_to_anchor=(1.15, 1), loc=2)
host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
plt.show()
#plt.savefig(filename+'_PressureCorrection', bbox_inches = 'tight')
#plt.clf()
"""
