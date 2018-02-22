#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:46:27 2017

@author: KL
"""
import numpy as np
import eventrate as e
import pulsevpp as vpp
import timeofflight as t
import pulseheight as ph
import CountrateCuts as cc
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.colors import LogNorm

filename = '3Triplets_BankArray_MultiplexAll_switched_Run19_HV1_900Vch1__HV2_650Vch1_850Vch2_SingleChBank'

# TIME OF FLIGHT FOR EACH CHANNEL

b, c, d, f = t.timeofflight(filename+'.dat')

plt.clf()
plt.hist(b, 80, normed =1, facecolor='green', alpha=0.75)
plt.xlabel('Time/ ns'), plt.ylabel('Frequency'), plt.title('Time of Flight CH2: 18.01.18 - 23.01.18')
#plt.axis([0,50, 0, 0.025])  
plt.savefig(filename+'_TOFCH2.png', bbox_inches = 'tight')
plt.clf()

"""
plt.hist(f, 80, normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Time/ ns'), plt.ylabel('Frequency'), plt.title('Time of Flight CH4: 18.01.18 - 23.01.18')
#plt.axis([0,100, 0, 0.06])  
plt.savefig(filename+'_TOFCH4.png', bbox_inches = 'tight')
plt.clf()
"""

plt.hist(c, 80, normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Time/ ns'), plt.ylabel('Frequency'), plt.title('Time of Flight CH3: 18.01.18 - 23.01.18')
#plt.axis([0,50, 0, 0.03])  
plt.savefig(filename+'_TOFCH3.png', bbox_inches = 'tight')
plt.clf()


plt.hist(d, 80, normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Time/ ns'), plt.ylabel('Frequency'), plt.title('Time of Flight CH4: 18.01.18 - 23.01.18')
#plt.axis([0,100, 0, 0.06])  
plt.savefig(filename+'_TOFCH4.png', bbox_inches = 'tight')
plt.clf()



ts, r = e.eventrate(filename+'.dat', 60)
plt.xlabel('Time/ minutes'), plt.ylabel('Count rate (60 minute bins)'), plt.title('Count rate over time - 18.01.18 - 23.01.18')
plt.plot(ts, r)
#hr1 = -21.85432
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
#plt.axvline(x=(hr1+(720*11)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*12)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*13)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*14)), color='m', linestyle=':')
#EACH LINE REPRESENTS MIDNIGHT/MIDDAY
#plt.axis([9235.36371, 10675.36371, 150, 600])
plt.savefig(filename+'Countrate.png', bbox_inches = 'tight')
plt.clf()

#COUNTRATE FOR EACH CHANNEL WITH VOLTAGE CUTS APPLIED
#vOLTAGE CUTS SET AT 70mV FOR EACH CHANNEL
ts, r2, r3, r4 = cc.countratecuts(filename+'.dat', 60)
plt.xlabel('Time/ minutes'), plt.ylabel('Count rate (60 minute bins)'), plt.title('Count rate over time (Cuts on CH1) - 18.01.18 - 23.01.18')
plt.plot(ts, r2)
#plt.axvline(x=hr1, color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*2)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*4)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*6)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*8)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*10)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*12)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*14)), color='m', linestyle=':')
plt.savefig(filename+'Countrate60mins_ch1_70mVCut.png', bbox_inches = 'tight')
plt.clf()

plt.xlabel('Time/ minutes'), plt.ylabel('Count rate (60 minute bins)'), plt.title('Count rate over time (Cuts on CH2) - 18.01.18 - 23.01.18')
plt.plot(ts, r3)
#plt.axvline(x=hr1, color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*2)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*4)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*6)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*8)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*10)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*12)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*14)), color='m', linestyle=':')
plt.savefig(filename+'Countrate60mins_ch2_70mVCut.png', bbox_inches = 'tight')
plt.clf()

plt.xlabel('Time/ minutes'), plt.ylabel('Count rate (60 minute bins)'), plt.title('Count rate over time (Cuts on CH3) - 18.01.18 - 23.01.18')
plt.plot(ts, r4)
#plt.axvline(x=hr1, color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*2)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*4)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*6)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*8)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*10)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*12)), color='m', linestyle=':')
#plt.axvline(x=(hr1+(720*14)), color='m', linestyle=':')
plt.savefig(filename+'Countrate60mins_ch3_70mVCut.png', bbox_inches = 'tight')
plt.clf()

#PULSE HEIGHT HISTOGRAMS

h1, h2, h3, h4 = ph.pulseheight(filename+'.dat')

n, bins, patches = plt.hist(h1, 80, normed =1, facecolor='green', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH1 Peak-To-Peak Voltages (18.01.18 - 23.01.18)')
ax = plt.axes()    
#plt.axis([0,500, 0, 0.025])  
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_PH_CH1.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist(h2, 80, normed =1, facecolor='blue', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH2 Peak-To-Peak Voltages (18.01.18 - 23.01.18)')
ax = plt.axes()    
#plt.axis([25,250, 0, 0.01]) 
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_PH_CH2.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist(h3, 80, normed =1, facecolor='red', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH3 Peak-To-Peak Voltages (18.01.18 - 23.01.18)')
ax = plt.axes()    
#plt.axis([20,250, 0, 0.01]) 
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_PH_CH3.png', bbox_inches = 'tight')
plt.clf()

n, bins, patches = plt.hist(h4, 80, normed =1, facecolor='yellow', alpha=0.75)
plt.xlabel('Voltage/mV'), plt.ylabel(''), plt.title('CH4 Peak-To-Peak Voltages (18.01.18 - 23.01.18)')
ax = plt.axes()    
plt.axis([20,250, 0, 0.01]) 
ax.yaxis.grid(True, linewidth=0.5) 
ax.xaxis.grid(True, linewidth=0.5)
plt.savefig(filename+'_PH_CH4.png', bbox_inches = 'tight')
plt.clf()


#PULSE HEIGHT VS TIME OF FLIGHT FOR EACH CHANNEL

ch1vpp, ch2vpp, ch3vpp, ch4vpp  = vpp.pulsevpp(filename+'.dat')

plt.scatter(b, ch1vpp, color='green', alpha=0.5)
plt.title('Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH1')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
#plt.axis([-25,60, 0, 250])
plt.savefig(filename+'_PH_TOF_CH1.png', bbox_inches = 'tight')
plt.clf()

plt.scatter(f, ch4vpp, color='green', alpha=0.5)
plt.title('Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH4')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
#plt.axis([-25,60, 0, 250])
plt.savefig(filename+'_PH_TOF_CH4.png', bbox_inches = 'tight')
plt.clf()

plt.scatter(c, ch2vpp, color='red', alpha=0.5)
plt.title('Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH2')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
#plt.axis([-25,100, 0, 525])
plt.savefig(filename+'_PH_TOF_CH2.png', bbox_inches = 'tight')
plt.clf()

plt.scatter(d, ch3vpp, color='blue', alpha=0.5)
plt.title('Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH3')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
#plt.axis([-25,100, 0, 250])
plt.savefig(filename+'_PH_TOF_CH3.png', bbox_inches = 'tight')
plt.clf()

## 2D PLOT WITH COLOUR BAR

plt.hist2d(b, ch2vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,10)
plt.title('2D Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH2')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
plt.axis([-50,250, 20, 400])
plt.savefig(filename+'_PH_TOF2DCOL_CH2.png', pad_inches = 0)
plt.clf()
"""
plt.hist2d(f, ch1vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,10)
plt.title('2D Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH4')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
#plt.axis([-200,50, 20, 300])
plt.savefig(filename+'_PH_TOF2DCOL_CH4.png', pad_inches = 0)
plt.clf()
"""
plt.hist2d(c, ch3vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,10)
plt.title('2D Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH3')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
plt.axis([-50,250, 20, 500])
plt.savefig(filename+'_PH_TOF2DCOL_CH3.png', pad_inches = 0)
plt.clf()

plt.hist2d(d, ch4vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,10)
plt.title('2D Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH4')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
plt.axis([-50,250, 20, 500])
plt.savefig(filename+'_PH_TOF2DCOL_CH4.png', pad_inches = 0)
plt.clf()



plt.hist2d(b, ch1vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,10)
plt.title('2D Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH2')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
plt.axis([-50,250, 20, 400])
plt.savefig(filename+'_PH_TOF2DCOL_CH1_2.png', pad_inches = 0)
plt.clf()

plt.hist2d(c, ch1vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,10)
plt.title('2D Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH3')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
plt.axis([-50,250, 20, 500])
plt.savefig(filename+'_PH_TOF2DCOL_CH1_3.png', pad_inches = 0)
plt.clf()

plt.hist2d(d, ch1vpp, bins=1000, norm = LogNorm())
plt.colorbar()
plt.clim(1,10)
plt.title('2D Pulse Height Vs Time of Flight (18.01.18 - 23.01.18) - CH4')
plt.xlabel('Time of Flight/ns')
plt.ylabel('Pulse Height/mV')
plt.axis([-50,250, 20, 500])
plt.savefig(filename+'_PH_TOF2DCOL_CH1_4.png', pad_inches = 0)
plt.clf()



## GAUSSIAN FIT 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

ph_cut1 = np.squeeze(np.asarray(h1)>20)
ph_cut2 = np.squeeze(np.asarray(h2)>25)
ph_cut3 = np.squeeze(np.asarray(h3)>25)
#ph_cut4 = np.squeeze(np.asarray(h4)>25)

#ph1 = h1[ph_cut1]
#ph2 = h2[ph_cut2]
#ph3 = h3[ph_cut3]
#ph4 = h4[ph_cut4]

hist, bin_edges = np.histogram(b[ph_cut1], 600)
BE = np.zeros(600)
for i,be in enumerate(bin_edges):
    if i<(len(bin_edges)-1):
        BE[i] = (bin_edges[i+1] + bin_edges[i])*0.5
CutB = (BE>-50)&(BE<60)
BE = BE[CutB]
hist=hist[CutB]
popt, pcov = curve_fit(gauss_function, BE, hist, p0 = [1, 0, 5], maxfev=200000)
plt.plot(BE, gauss_function(BE, *popt), label='Fit', color = 'green')
plt.plot(BE, hist,'blue', label='Data')
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)
plt.xlabel('Time/ ns'), plt.ylabel('Frequency'), plt.title('Time of Flight CH1: 18.01.18 - 23.01.18')
#plt.axis([0,60, 0, 5]) 
print (popt)
plt.savefig(filename+'_CH1_Gauss.png', bbox_inches = 'tight')
plt.clf()

hist, bin_edges = np.histogram(c[ph_cut2], 600)
BE = np.zeros(600)
for i,be in enumerate(bin_edges):
    if i<(len(bin_edges)-1):
        BE[i] = (bin_edges[i+1] + bin_edges[i])*0.5
CutB = (BE>-50)&(BE<50)
BE = BE[CutB]
hist=hist[CutB]
popt, pcov = curve_fit(gauss_function, BE, hist, p0 = [1, 0, 5], maxfev=200000)
plt.plot(BE, gauss_function(BE, *popt), label='Fit', color = 'green')
plt.plot(BE, hist,'red', label='Data')
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)
plt.xlabel('Time/ ns'), plt.ylabel('Frequency'), plt.title('Time of Flight CH2: 18.01.18 - 23.01.18')
#plt.axis([-50,50, 0, 0.005]) 
print (popt)
plt.savefig(filename+'_CH2_Gauss.png', bbox_inches = 'tight')
plt.clf()

hist, bin_edges = np.histogram(d[ph_cut3], 600)
BE = np.zeros(600)
for i,be in enumerate(bin_edges):
    if i<(len(bin_edges)-1):
        BE[i] = (bin_edges[i+1] + bin_edges[i])*0.5
CutB = (BE>-50)&(BE<50)
BE = BE[CutB]
hist=hist[CutB]
popt, pcov = curve_fit(gauss_function, BE, hist, p0 = [1, 0, 5], maxfev=200000)
plt.plot(BE, gauss_function(BE, *popt), label='Fit', color = 'green')
plt.plot(BE, hist,'yellow', label='Data')
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)
plt.xlabel('Time/ ns'), plt.ylabel('Frequency'), plt.title('Time of Flight CH3: 18.01.18 - 23.01.18')
#plt.axis([-50,100, 0, 0.005]) 
print (popt)
plt.savefig(filename+'_CH3_Gauss.png', bbox_inches = 'tight')
plt.clf()
