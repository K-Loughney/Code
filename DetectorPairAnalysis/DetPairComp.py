#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:39:30 2018

@author: KL
"""

import numpy as np
import matplotlib.pyplot as plt

filename = '3Triplets_BankArray_MultiplexAll_switched_Run19_HV1_900Vch1__HV2_650Vch1_850Vch2_SingleChBank'

with open(filename+'.dat') as d:
    
    d=[x.strip() for x in d if x.strip()]
  
data=[tuple(map(float,x.split())) for x in d[2:]]
event=[x[0] for x in data]
ts=[x[1] for x in data]
ch1_t=np.asarray([x[3] for x in data])
ch2_t=np.asarray([x[6] for x in data])
ch3_t=np.asarray([x[9] for x in data])
ch4_t=np.asarray([x[12] for x in data])

print("Total Event Number:", len(event))

ch1tof = ch1_t - ch2_t
ch2tof = ch1_t - ch3_t
ch3tof = ch1_t - ch4_t

t1cut0 = (np.asarray(ch1tof)>-5)&(np.asarray(ch1tof)<20)
t1cut1 = (np.asarray(ch1tof)>25)&(np.asarray(ch1tof)<52)
t1cut2 = (np.asarray(ch1tof)>52)&(np.asarray(ch1tof)<80)
t1cut3 = (np.asarray(ch1tof)>85)&(np.asarray(ch1tof)<120)
t1cut4 = (np.asarray(ch1tof)>140)&(np.asarray(ch1tof)<170)
t1cut5 = (np.asarray(ch1tof)>180)&(np.asarray(ch1tof)<220)
t2cut0 = (np.asarray(ch2tof)>-5)&(np.asarray(ch2tof)<20)
t2cut1 = (np.asarray(ch2tof)>25)&(np.asarray(ch2tof)<52)
t2cut2 = (np.asarray(ch2tof)>52)&(np.asarray(ch2tof)<80)
t2cut3 = (np.asarray(ch2tof)>85)&(np.asarray(ch2tof)<120)
t2cut4 = (np.asarray(ch2tof)>140)&(np.asarray(ch2tof)<170)
t2cut5 = (np.asarray(ch2tof)>180)&(np.asarray(ch2tof)<220)
t3cut0 = (np.asarray(ch3tof)>-5)&(np.asarray(ch3tof)<20)
t3cut1 = (np.asarray(ch3tof)>25)&(np.asarray(ch3tof)<52)
t3cut2 = (np.asarray(ch3tof)>52)&(np.asarray(ch3tof)<80)
t3cut3 = (np.asarray(ch3tof)>85)&(np.asarray(ch3tof)<120)
t3cut4 = (np.asarray(ch3tof)>140)&(np.asarray(ch3tof)<170)
t3cut5 = (np.asarray(ch3tof)>180)&(np.asarray(ch3tof)<220)

Det60 = np.asarray(event)[t1cut0]
Det61 = np.asarray(event)[t1cut1]
Det62 = np.asarray(event)[t1cut2]
Det63 = np.asarray(event)[t1cut3]
Det64 = np.asarray(event)[t1cut4]
Det65 = np.asarray(event)[t1cut5]

Det70 = np.asarray(event)[t2cut0]
Det71 = np.asarray(event)[t2cut1]
Det72 = np.asarray(event)[t2cut2]
Det73 = np.asarray(event)[t2cut3]
Det74 = np.asarray(event)[t2cut4]
Det75 = np.asarray(event)[t2cut5]

Det80 = np.asarray(event)[t3cut0]
Det81 = np.asarray(event)[t3cut1]
Det82 = np.asarray(event)[t3cut2]
Det83 = np.asarray(event)[t3cut3]
Det84 = np.asarray(event)[t3cut4]
Det85 = np.asarray(event)[t3cut5]

print("Detector 6 & 0: ",len(Det60))
print("Detector 6 & 1: ",len(Det61))
print("Detector 6 & 2: ",len(Det62))
print("Detector 6 & 3: ",len(Det63))
print("Detector 6 & 4: ",len(Det64))
print("Detector 6 & 5: ",len(Det65))

NormDet60 = (len(Det60))/(len(Det65))
NormDet61 = (len(Det61))/(len(Det65))
NormDet62 = (len(Det62))/(len(Det65))
NormDet63 = (len(Det63))/(len(Det65))
NormDet64 = (len(Det64))/(len(Det65))
NormDet65 = (len(Det65))/(len(Det65))

NormDet70 = (len(Det70))/(len(Det75))
NormDet71 = (len(Det71))/(len(Det75))
NormDet72 = (len(Det72))/(len(Det75))
NormDet73 = (len(Det73))/(len(Det75))
NormDet74 = (len(Det74))/(len(Det75))
NormDet75 = (len(Det75))/(len(Det75))

NormDet80 = (len(Det80))/(len(Det85))
NormDet81 = (len(Det81))/(len(Det85))
NormDet82 = (len(Det82))/(len(Det85))
NormDet83 = (len(Det83))/(len(Det85))
NormDet84 = (len(Det84))/(len(Det85))
NormDet85 = (len(Det85))/(len(Det85))

print("Normalised Detector 6 & 0: ",(NormDet60))
print("Normalised Detector 6 & 1: ",(NormDet61))
print("Normalised Detector 6 & 2: ",(NormDet62))
print("Normalised Detector 6 & 3: ",(NormDet63))
print("Normalised Detector 6 & 4: ",(NormDet64))
print("Normalised Detector 6 & 5: ",(NormDet65))

###############################################################################
###############################################################################

D60SimN = (1116/81594)
D61SimN = (7584/81594)
D62SimN = (21386/81594)
D63SimN = (39966/81594)
D64SimN = (60600/81594)
D65SimN = (81594/81594)

D70SimN = (4/61140)
D71SimN = (1250/61140)
D72SimN = (7500/61140)
D73SimN = (21484/61140)
D74SimN = (39886/61140)
D75SimN = (61140/61140)

D81SimN = (2/40712)
D82SimN = (1118/40712)
D83SimN = (7768/40712)
D84SimN = (21108/40712)
D85SimN = (40712/40712)

SimNorm6 = [D60SimN, D61SimN, D62SimN, D63SimN, D64SimN, D65SimN]
SimNorm7 = [D70SimN, D71SimN, D72SimN, D73SimN, D74SimN, D75SimN]
SimNorm8 = [D81SimN, D82SimN, D83SimN, D84SimN, D85SimN]
###############################################################################
###############################################################################

Norm6= [NormDet60, NormDet61, NormDet62, NormDet63, NormDet64, NormDet65]
Norm7= [NormDet70, NormDet71, NormDet72, NormDet73, NormDet74, NormDet75]
Norm8= [NormDet81, NormDet82, NormDet83, NormDet84, NormDet85]
Det = [0, 1, 2, 3, 4, 5]
Det8 = [1, 2, 3, 4, 5]

plt.scatter(Det, Norm6, color='blue', alpha=0.5, label = "Experimental (18.01.18)")
plt.scatter(Det, SimNorm6, color='red', alpha=0.5, label = "Simulation (Detector 6 pairs)")
#plt.title('Pulse Height Vs Time of Flight (18.01.18) - CH3')
plt.xlabel('Detector Number')
plt.ylabel('Normalised Count')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
#plt.axis([-25,100, 0, 250])
#plt.show()
plt.savefig(filename+'_Det6Comp.png', bbox_inches = 'tight')
plt.clf()

plt.scatter(Det, Norm7, color='blue', alpha=0.5, label = "Experimental (18.01.18)")
plt.scatter(Det, SimNorm7, color='red', alpha=0.5, label = "Simulation (Detector 7 pairs)")
#plt.title('Pulse Height Vs Time of Flight (18.01.18) - CH3')
plt.xlabel('Detector Number')
plt.ylabel('Normalised Count')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
#plt.axis([-25,100, 0, 250])
#plt.show()
plt.savefig(filename+'_Det7Comp.png', bbox_inches = 'tight')
plt.clf()

plt.scatter(Det8, Norm8, color='blue', alpha=0.5, label = "Experimental (18.01.18)")
plt.scatter(Det8, SimNorm8, color='red', alpha=0.5, label = "Simulation (Detector 8 pairs)")
#plt.title('Pulse Height Vs Time of Flight (18.01.18) - CH3')
plt.xlabel('Detector Number')
plt.ylabel('Normalised Count')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
#plt.axis([-25,100, 0, 250])
#plt.show()
plt.savefig(filename+'_Det8Comp.png', bbox_inches = 'tight')
plt.clf()
