#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:27:30 2017

@author: KL
"""
import numpy as np
import eventrate as e
import CountrateCuts as cc
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AA
from mpl_toolkits.axes_grid1 import host_subplot


filename = '6_det_Array4_Multiplex_ch3andch4_Run13_800Vch2_625Vch1'


with open('WeatherHistory021117_071117.dat') as g:
    g=[x.strip() for x in g if x.strip()]
    data1=[tuple(map(float,x.split())) for x in g[2:]]
    TIME=[x[0] for x in data1]
    temp=[x[1] for x in data1]
    dewpoint=[x[2] for x in data1]
    
#print(TIME)
print(temp)
#print(dewpoint)

with open(filename+'.dat') as d:
    
        d=[x.strip() for x in d if x.strip()]
  
        data=[tuple(map(float,x.split())) for x in d[2:]]
        event=[x[0] for x in data]
        ts=[x[1] for x in data]
    
        originT = ts[0]
            
Relwht = (np.asarray(TIME) - originT)/1000
RelWHT = Relwht/60

print(RelWHT)

ts, r = e.eventrate(filename+'.dat', 30)
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
par1 = host.twinx()
offset = 60
#hr1 = 33.13840+(60*11)
#plt.axvline(x=(hr1 - 720), color='m', linestyle=':')
#plt.axvline(x=hr1, color='m', linestyle=':')
#plt.axvline(x=(hr1+720), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*2)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*3)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*4)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*5)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*6)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*7)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*8)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*9)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*10)), color='m', linestyle=':')
#host.set_xlim(0,3000)
#host.set_xlim(-898.84058, 541.15942)
#host.set_xlim(541.15942, 1981.15942)
#host.set_xlim(1981.15942, 3421.15942)
#host.set_xlim(3421.15942, 4861.15942)
#host.set_xlim(4861.15942, 6301.15942)
#host.set_xlim(6301.15942, 7741.15942)
#host.set_xlim(7741.15942, 9181.15942)
#host.set_xlim(9181.15942, 10675.15942)
#host.set_ylim(150, 1500)
host.set_xlabel("Time/Minutes")
host.set_ylabel("Countrate (30 Minute Bins)")
par1.set_ylabel("Temperature/°C")
p1, = host.plot(ts, r, label="Countrate")
p2, = par1.plot(RelWHT, temp, label="Temperature")
host.legend()
host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
plt.savefig(filename+'CountrateTemp.png')
plt.clf()



#COUNTRATE FOR EACH CHANNEL WITH VOLTAGE CUTS APPLIED
#vOLTAGE CUTS SET AT 70mV FOR EACH CHANNEL

ts1, r2, r3, r4 = cc.countratecuts(filename+'.dat', 30)
#plt.title('Count rate over time (Cuts on CH2) - 12.10.17 - 17.10.17')
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
par1 = host.twinx()
offset = 60
#plt.axvline(x=hr1, color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*2)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*4)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*6)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*8)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*10)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*12)), color='m', linestyle=':')
#EACH LINE REPRESENTS MIDNIGHT
#host.set_xlim(9181.15942, 10675.15942)
#host.set_ylim(140, 220)
#host.set_xlim(0,3000)
host.set_xlabel("Time/Minutes")
host.set_ylabel("Countrate (30 Minute Bins)")
par1.set_ylabel("Temperature/°C")
host.set_title("Count rate over time (Cuts on CH2) - 02.11.17 - 07.11.17")
p1, = host.plot(ts1, r2, label="Countrate")
p2, = par1.plot(RelWHT, temp, label="Temperature")
host.legend(loc=0)
host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
plt.savefig(filename+'CountrateTemp30mins_ch2_70mVCut.png')
plt.clf()



host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
par1 = host.twinx()
offset = 60
#plt.axvline(x=hr1, color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*2)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*4)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*6)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*8)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*10)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*12)), color='m', linestyle=':')
#EACH LINE REPRESENTS MIDNIGHT
#host.set_xlim(9181.15942, 10675.15942)
#host.set_ylim(230, 320)
#host.set_xlim(0,3000)
host.set_xlabel("Time/Minutes")
host.set_ylabel("Countrate (30 Minute Bins)")
par1.set_ylabel("Temperature/°C")
host.set_title("Count rate over time (Cuts on CH3) - 02.11.17 - 07.11.17")
p4, = host.plot(ts1, r3, label="Countrate")
p2, = par1.plot(RelWHT, temp, label="Temperature")
host.legend(loc=4)
host.axis["left"].label.set_color(p4.get_color())
par1.axis["right"].label.set_color(p2.get_color())
plt.savefig(filename+'CountrateTemp30mins_ch3_70mVCut.png')
plt.clf()



host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
par1 = host.twinx()
offset = 60
#plt.axvline(x=hr1, color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*2)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*4)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*6)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*8)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*10)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*12)), color='m', linestyle=':')
#EACH LINE REPRESENTS MIDNIGHT
#host.set_xlim(9181.15942, 10675.15942)
#host.set_ylim(160, 290)
#host.set_xlim(0,3000)
host.set_xlabel("Time/Minutes")
host.set_ylabel("Countrate (30 Minute Bins)")
par1.set_ylabel("Temperature/°C")
host.set_title("Count rate over time (Cuts on CH4) - 02.11.17 - 07.11.17")
p5, = host.plot(ts1, r4, label="Countrate")
p2, = par1.plot(RelWHT, temp, label="Temperature")
host.legend(loc=0)
host.axis["left"].label.set_color(p5.get_color())
par1.axis["right"].label.set_color(p2.get_color())
plt.savefig(filename+'CountrateTemp30mins_ch4_70mVCut.png')
plt.clf()
