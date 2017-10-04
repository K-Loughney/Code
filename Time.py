#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 10:51:24 2017

@author: KL
"""
import matplotlib.pyplot as plt
#import datetime
import pandas as pd
#import numpy as np
TS = []

histTDiff = []
histch1 = []
filename = '6_detContCollect_NewDetArray4_multiplex_ch3andch4_Run2'
with open(filename+'.dat') as d:
    d=[x.strip() for x in d if x.strip()]
    data=[tuple(map(float,x.split())) for x in d[2:]]
    event=[x[0] for x in data]
    ts=[x[1] for x in data]
    
    for x in ts:
        TS.append(x/1000)
        s = TS

    d = pd.to_datetime(s[:], unit = 's')
    df = pd.DataFrame(d)
    TDiff = df.diff()
    print (df)
    
        
 

    
    
"""    
    TDF = np.array([ch1_vpp, TDiff])
    histch1.append(ch1_vpp)     
    histTDiff.append(TDF)
    
n, bins, patches = plt.hist(histTDiff, 50, normed =1, facecolor='green', alpha=0.75)
#plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH1 Peak-To-Peak Voltages (950V)')
ax = plt.axes()    
#plt.axis([0,250, 0, 0.025])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig('Comp_Det3_AND6_CH1_950V_CODE.png')
plt.show()
  
    
    
    #d = (datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')) 
    #print(d)"""    
    
    #dt = time.time()
    #DT = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts[0]))
    #DT1 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(TS))
    #print (DT)
    #datetime = datetime.datetime.fromtimestamp(float(TS)).strftime('%c')