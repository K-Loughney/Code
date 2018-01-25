#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 10:27:15 2017

@author: KL
"""

import matplotlib.pyplot as plt
from xml.dom import minidom
          
xmldoc = minidom.parse('/home/shas/Documents/Kerri/Masters/Multiple Detectors/4Detector_1Week/4Detector_1Week.xml')
#xmldoc = minidom.parse('/home/shas/Documents/Kerri/Masters/Coincidence_28_4_17and5_5_17/Coincidence_chris_001.xml')

itemlist = xmldoc.getElementsByTagName('Data') 
print ("Data: ", len(itemlist))

V = []

histmin1 = []
histmin2 = []
histmin3 = []
histmin4 = []

events = xmldoc.getElementsByTagName('Event')

for ev in events:
    chn1 = ev.getElementsByTagName('CHN1')[0]
    #print (chn1)
    data1 = chn1.getElementsByTagName('Data')[:]
    mindata1 = 0
    for num in range (0, 1024):
        V1 = float(data1[num].childNodes[0].data.split(',')[1])
        if V1<mindata1:
            mindata1 = V1
        T1 = data1[num].childNodes[0].data.split(',')[0]
             
    histmin1.append(mindata1)   
        
    chn2 = ev.getElementsByTagName('CHN2')[0]
    data2 = chn2.getElementsByTagName('Data')[:]
    mindata2 = 0 
    for num in range (0, 1024):
        V2 = float(data2[num].childNodes[0].data.split(',')[1])
        if V2<mindata2:
            mindata2 = V2
        T2 = data2[num].childNodes[0].data.split(',')[0]
    #print (mindata2)
    histmin2.append(mindata2)
    
        
    chn3 = ev.getElementsByTagName('CHN3')[0]
    data3 = chn3.getElementsByTagName('Data')[:]
    mindata3 = 0 
    for num in range (0, 1024):
        V3 = float(data3[num].childNodes[0].data.split(',')[1])
        if V3<mindata3:
            mindata3 = V3
        T3 = data3[num].childNodes[0].data.split(',')[0]
    #print (mindata2)
    histmin3.append(mindata3)
    
    chn4 = ev.getElementsByTagName('CHN4')[0]
    data4 = chn4.getElementsByTagName('Data')[:]
    mindata4 = 0 
    for num in range (0, 1024):
        V4 = float(data4[num].childNodes[0].data.split(',')[1])
        if V4<mindata4:
            mindata4 = V4
        T4 = data4[num].childNodes[0].data.split(',')[0]
    #print (mindata2)
    histmin4.append(mindata4)


n, bins, patches = plt.hist(histmin1, 50, normed =1, facecolor='green', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH1 Peak-To-Peak Voltages')
ax = plt.axes()    
#plt.axis([0,-600, 0, 0.04])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig('Coinc_WL_CH1.png')
plt.show()

n, bins, patches = plt.hist(histmin2, 50, normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH2 Peak-To-Peak Voltages')
ax = plt.axes()
#plt.axis([0,-600, 0, 0.07])          
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig('Coinc_WL_CH2.png')
plt.show()

n, bins, patches = plt.hist(histmin3, 50, normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH1 Peak-To-Peak Voltages')
ax = plt.axes()    
#plt.axis([0,-600, 0, 0.04])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig('Coinc_WL_CH1.png')
plt.show()

n, bins, patches = plt.hist(histmin4, 50, normed =1, facecolor='Yellow', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH2 Peak-To-Peak Voltages')
ax = plt.axes()
#plt.axis([0,-600, 0, 0.07])          
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
#plt.savefig('Coinc_WL_CH2.png')
plt.show()