#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:39:53 2018

@author: KL
"""
import numpy as np
import pandas as pd
import datetime as dt
import booldetpairs as bdp
import SimDatExtract as SDE
import presscordatacut as pcdc
import matplotlib.pyplot as plt
import weather_underground_parser as wp

filename = '3Triplets_BankArray_MultiplexAll_reversed_Run26_HV1_900Vch1__HV2_775Vch1_875Vch2_SingleChBank'

TS = []
HrE = []
D2HR = []
TSS = []
ts, detp1, detp2, timestamp = pcdc.presscordatacut(filename)

start_datetime = dt.datetime(2018,2,22)
end_datetime = dt.datetime(2018,2,22)
loc = "airport/EGLL"
hp = wp.weather_underground_parser(start_datetime,end_datetime, loc)
pres = hp.pressure
datetime = hp.datetime
temp = hp.temperature
humid = hp.relative_humidity

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
       
while len(d2hr)>0:
    indie = (d2hr==d2hr[0])
    D2HR.append(d2hr[0])
    d2hr = np.delete(d2hr, np.where(indie))
    #print (sum(indie))
    HrE.append(sum(indie))      ## Hourly countrate for muons.
#print(HrE)
R = len(D2HR)
r = len(HrE)

P0 = 1000
A =132

for i,x in enumerate(d2):    
    counttime = (dt.datetime.fromtimestamp(x))  ##Event time from dataset
    hppress = hp.get_pressure(counttime)        ##Pressure from weather underground for Heathrow airport
    Pressure_Correction = np.exp((hppress - P0)/A)  ## Pressure Correction 
    HPRESSCORRECT = np.multiply(HrE,Pressure_Correction) ## Pressure Corrected Countrate
    #print(counttime, hppress, Pressure_Correction, HPRESSCORRECT) 


plt.xlabel('Time/ Hours'), plt.ylabel('Count rate (1 hour bins)')
plt.plot(D2HR[1:R-1], HrE[1:r-1], label="Uncorrected Countrate")
plt.plot(D2HR[1:R-1], HPRESSCORRECT[1:r-1], label = 'Pressure Corrected Countrate')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.savefig(filename+'_PressureCorrectedCountrate', bbox_inches = 'tight')
plt.clf()

TP1D7 = []
TP2D7 = []
TP3D7 = []
TP4D7 = []
TP5D7 = []
TP6D7 = []

TP1D8 = []
TP2D8 = []
TP3D8 = []
TP4D8 = []
TP5D8 = []
TP6D8 = []

TP1D9 = []
TP2D9 = []
TP3D9 = []
TP4D9 = []
TP5D9 = []
TP6D9 = []

D17hr = ()
D27hr = ()
D37hr = ()
D47hr = ()
D57hr = ()
D67hr = ()
D18hr = ()
D28hr = ()
D38hr = ()
D48hr = ()
D58hr = ()
D68hr = ()
D19hr = ()
D29hr = ()
D39hr = ()
D49hr = ()
D59hr = ()
D69hr = ()

D17HR = []
D27HR = []
D37HR = []
D47HR = []
D57HR = []
D67HR = []
D18HR = []
D28HR = []
D38HR = []
D48HR = []
D58HR = []
D68HR = []
D19HR = []
D29HR = []
D39HR = []
D49HR = []
D59HR = []
D69HR = []

HrE17 = []
HrE27 = []
HrE37 = []
HrE47 = []
HrE57 = []
HrE67 = []
HrE18 = []
HrE28 = []
HrE38 = []
HrE48 = []
HrE58 = []
HrE68 = []
HrE19 = []
HrE29 = []
HrE39 = []
HrE49 = []
HrE59 = []
HrE69 = []

AHrE17 = ()
AHrE27 = ()
AHrE37 = ()
AHrE47 = ()
AHrE57 = ()
AHrE67 = ()
AHrE18 = ()
AHrE28 = ()
AHrE38 = ()
AHrE48 = ()
AHrE58 = ()
AHrE68 = ()
AHrE19 = ()
AHrE29 = ()
AHrE39 = ()
AHrE49 = ()
AHrE59 = ()
AHrE69 = ()

HPCor17Ave = ()
HPCor27Ave = ()
HPCor37Ave = ()
HPCor47Ave = ()
HPCor57Ave = ()
HPCor67Ave = ()
HPCor18Ave = ()
HPCor28Ave = ()
HPCor38Ave = ()
HPCor48Ave = ()
HPCor58Ave = ()
HPCor68Ave = ()
HPCor19Ave = ()
HPCor29Ave = ()
HPCor39Ave = ()
HPCor49Ave = ()
HPCor59Ave = ()
HPCor69Ave = ()
#Gets time for the detector pairs
# 1-6 is detectors PL01 - PL06
# 7-9 are the three recieving detectors going from the bottom up

##BOTTOM
TP1D7 = bdp.booldetpairs(filename, 1, 7, TP1D7)
TP2D7 = bdp.booldetpairs(filename, 2, 7, TP2D7)
TP3D7 = bdp.booldetpairs(filename, 3, 7, TP3D7)
TP4D7 = bdp.booldetpairs(filename, 4, 7, TP4D7)
TP5D7 = bdp.booldetpairs(filename, 5, 7, TP5D7)
TP6D7 = bdp.booldetpairs(filename, 6, 7, TP6D7)

##MIDDLE
TP1D8 = bdp.booldetpairs(filename, 1, 8, TP1D8)
TP2D8 = bdp.booldetpairs(filename, 2, 8, TP2D8)
TP3D8 = bdp.booldetpairs(filename, 3, 8, TP3D8)
TP4D8 = bdp.booldetpairs(filename, 4, 8, TP4D8)
TP5D8 = bdp.booldetpairs(filename, 5, 8, TP5D8)
TP6D8 = bdp.booldetpairs(filename, 6, 8, TP6D8)

##TOP
TP1D9 = bdp.booldetpairs(filename, 1, 9, TP1D9)
TP2D9 = bdp.booldetpairs(filename, 2, 9, TP2D9)
TP3D9 = bdp.booldetpairs(filename, 3, 9, TP3D9)
TP4D9 = bdp.booldetpairs(filename, 4, 9, TP4D9)
TP5D9 = bdp.booldetpairs(filename, 5, 9, TP5D9)
TP6D9 = bdp.booldetpairs(filename, 6, 9, TP6D9)

#Converts the time and rounds to the hour
D17hr = bdp.timecorrection(TP1D7, D17hr)
D27hr = bdp.timecorrection(TP2D7, D27hr)
D37hr = bdp.timecorrection(TP3D7, D37hr)
D47hr = bdp.timecorrection(TP4D7, D47hr)
D57hr = bdp.timecorrection(TP5D7, D57hr)
D67hr = bdp.timecorrection(TP6D7, D67hr)

D18hr = bdp.timecorrection(TP1D8, D18hr)
D28hr = bdp.timecorrection(TP2D8, D28hr)
D38hr = bdp.timecorrection(TP3D8, D38hr)
D48hr = bdp.timecorrection(TP4D8, D48hr)
D58hr = bdp.timecorrection(TP5D8, D58hr)
D68hr = bdp.timecorrection(TP6D8, D68hr)

D19hr = bdp.timecorrection(TP1D9, D19hr)
D29hr = bdp.timecorrection(TP2D9, D29hr)
D39hr = bdp.timecorrection(TP3D9, D39hr)
D49hr = bdp.timecorrection(TP4D9, D49hr)
D59hr = bdp.timecorrection(TP5D9, D59hr)
D69hr = bdp.timecorrection(TP6D9, D69hr)
#print(D17HR)

#Finds the Hourly Count Average for each detector pair
AHrE17, HPCor17Ave = bdp.pressurecorrection(D17hr, D17HR, HrE17, AHrE17, HPCor17Ave)
AHrE27, HPCor27Ave = bdp.pressurecorrection(D27hr, D27HR, HrE27, AHrE27, HPCor27Ave)
AHrE37, HPCor37Ave = bdp.pressurecorrection(D37hr, D37HR, HrE37, AHrE37, HPCor37Ave)
AHrE47, HPCor47Ave = bdp.pressurecorrection(D47hr, D47HR, HrE47, AHrE47, HPCor47Ave)
AHrE57, HPCor57Ave = bdp.pressurecorrection(D57hr, D57HR, HrE57, AHrE57, HPCor57Ave)
AHrE67, HPCor67Ave = bdp.pressurecorrection(D67hr, D67HR, HrE67, AHrE67, HPCor67Ave)

AHrE18, HPCor18Ave = bdp.pressurecorrection(D18hr, D18HR, HrE18, AHrE18, HPCor18Ave)
AHrE28, HPCor28Ave = bdp.pressurecorrection(D28hr, D28HR, HrE28, AHrE28, HPCor28Ave)
AHrE38, HPCor38Ave = bdp.pressurecorrection(D38hr, D38HR, HrE38, AHrE38, HPCor38Ave)
AHrE48, HPCor48Ave = bdp.pressurecorrection(D48hr, D48HR, HrE48, AHrE48, HPCor48Ave)
AHrE58, HPCor58Ave = bdp.pressurecorrection(D58hr, D58HR, HrE58, AHrE58, HPCor58Ave)
AHrE68, HPCor68Ave = bdp.pressurecorrection(D68hr, D68HR, HrE68, AHrE68, HPCor68Ave)

AHrE19, HPCor19Ave = bdp.pressurecorrection(D19hr, D19HR, HrE19, AHrE19, HPCor19Ave)
AHrE29, HPCor29Ave = bdp.pressurecorrection(D29hr, D29HR, HrE29, AHrE29, HPCor29Ave)
AHrE39, HPCor39Ave = bdp.pressurecorrection(D39hr, D39HR, HrE39, AHrE39, HPCor39Ave)
AHrE49, HPCor49Ave = bdp.pressurecorrection(D49hr, D49HR, HrE49, AHrE49, HPCor49Ave)
AHrE59, HPCor59Ave = bdp.pressurecorrection(D59hr, D59HR, HrE59, AHrE59, HPCor59Ave)
AHrE69, HPCor69Ave = bdp.pressurecorrection(D69hr, D69HR, HrE69, AHrE69, HPCor69Ave)
#print(HPCor17Ave)

Det6Averages = [AHrE67, AHrE57, AHrE47, AHrE37, AHrE27, AHrE17]
Det7Averages = [AHrE68, AHrE58, AHrE48, AHrE38, AHrE28, AHrE18]
Det8Averages = [AHrE69, AHrE59, AHrE49, AHrE39, AHrE29, AHrE19]

Det6Averages_Pressure_Correction = [HPCor67Ave, HPCor57Ave, HPCor47Ave, HPCor37Ave, HPCor27Ave, HPCor17Ave]
Det7Averages_Pressure_Correction = [HPCor68Ave, HPCor58Ave, HPCor48Ave, HPCor38Ave, HPCor28Ave, HPCor18Ave]
Det8Averages_Pressure_Correction = [HPCor69Ave, HPCor59Ave, HPCor49Ave, HPCor39Ave, HPCor29Ave, HPCor19Ave]

Norm6 = [x/Det6Averages_Pressure_Correction[5] for x in Det6Averages_Pressure_Correction] 
Norm7 = [x/Det7Averages_Pressure_Correction[5] for x in Det7Averages_Pressure_Correction] 
Norm8 = [x/Det8Averages_Pressure_Correction[5] for x in Det8Averages_Pressure_Correction] 


##SIMULATION DATA 
D6PA, D7PA, D8PA, D6PAErr, D7PAErr, D8PAErr, D6PR, D7PR, D8PR, D6PRErr, D7PRErr, D8PRErr, D6PC, D7PC, D8PC = SDE.SimDatExtract('cosmic_rays_planar_config_new_timing_nevents_500k_180cm_run_info.dat')

D6PRNorm = [x/(D6PR[5]) for x in D6PR]
D7PRNorm = [x/(D7PR[5]) for x in D7PR]
D8PRNorm = [x/(D8PR[5]) for x in D8PR]

plt.scatter(D6PA, Det6Averages_Pressure_Correction, color='blue', alpha=0.5, label = "Experimental (Det 6 Pairs) (PC)")
plt.errorbar(D6PA, D6PR, xerr=D8PAErr, yerr=D8PRErr, color='red', alpha=0.5, label = "Simulation (Detector 6 pairs)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.savefig(filename+'Absolute6error.png', bbox_inches = 'tight')
plt.clf()

plt.scatter(D7PA, Det7Averages_Pressure_Correction, color='blue', alpha=0.5, label = "Experimental (Det 7 Pairs) (PC)")
plt.errorbar(D7PA, D7PR, xerr=D8PAErr, yerr=D8PRErr, color='red', alpha=0.5, label = "Simulation (Detector 7 pairs)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.savefig(filename+'Absolute7error.png', bbox_inches = 'tight')
plt.clf()

plt.scatter(D8PA, Det8Averages_Pressure_Correction, color='blue', alpha=0.5, label = "Experimental (Det 8 Pairs) (PC)")
plt.errorbar(D8PA, D8PR, xerr=D8PAErr, yerr=D8PRErr, color='red', alpha=0.5, label = "Simulation (Detector 8 pairs)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.savefig(filename+'Absolute8error.png', bbox_inches = 'tight')
plt.clf()



plt.scatter(D6PA, Norm6, color='blue', alpha=0.5, label = "Experimental (Det 6 Pairs) (PC)")
plt.scatter(D6PA, D6PRNorm, color='red', alpha=0.5, label = "Simulation (Detector 6 pairs)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.savefig(filename+'Absolute6Norm.png', bbox_inches = 'tight')
plt.clf()

plt.scatter(D7PA, Norm7, color='blue', alpha=0.5, label = "Experimental (Det 7 Pairs) (PC)")
plt.scatter(D7PA, D7PRNorm, color='red', alpha=0.5, label = "Simulation (Detector 7 pairs)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.savefig(filename+'Absolute7Norm.png', bbox_inches = 'tight')
plt.clf()

plt.scatter(D8PA, Norm8, color='blue', alpha=0.5, label = "Experimental (Det 8 Pairs) (PC)")
plt.scatter(D8PA, D8PRNorm, color='red', alpha=0.5, label = "Simulation (Detector 8 pairs)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.savefig(filename+'Absolute8Norm.png', bbox_inches = 'tight')
plt.clf()
