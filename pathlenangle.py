#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:51:25 2017

@author: KL
"""

import numpy as np
import matplotlib.pyplot as plt

#dist = 1.70
"""Distance between detectors in meters"""

#detH = (0.155)
"""height of each detector"""
def pathlenangle ():
    HeightD3 = []
    HeightD4 = []
    HeightD6 = []

    HeightP6 = []
    HeightP5 = []
    HeightP4 = []
    HeightP3 = []
    HeightP2 = []
    HeightP1 = []

    HeightP6D6 = []
    HeightP5D6 = []
    HeightP5D4 = []
    HeightP4D6 = []
    HeightP4D4 = []
    HeightP4D3 = []
    HeightP3D6 = []
    HeightP3D4 = []
    HeightP3D3 = []
    HeightP2D6 = []
    HeightP2D4 = []
    HeightP2D3 = []
    HeightP1D6 = []
    HeightP1D4 = []
    HeightP1D3 = []

    HeightD6.append(np.random.uniform(0, 0.155, 80))
    HeightD3.append(np.random.uniform(0.155, 0.310, 80))
    HeightD4.append(np.random.uniform(0.310, 0.465, 80))


    HeightP6.append(np.random.uniform(0, 0.155, 80))
    HeightP5.append(np.random.uniform(0.155, 0.310, 80))
    HeightP4.append(np.random.uniform(0.310, 0.465, 80))
    HeightP3.append(np.random.uniform(0.465, 0.620, 80))
    HeightP2.append(np.random.uniform(0.620, 0.775, 80))
    HeightP1.append(np.random.uniform(0.775, 0.930, 80))

#######################################################

    HeightP6D6 = np.array(np.subtract(HeightP6, HeightD6))
    
    HeightP5D6 = np.array(np.subtract(HeightP5, HeightD6))
    HeightP5D4 = np.array(np.subtract(HeightP5, HeightD4))

    HeightP4D6 = np.array(np.subtract(HeightP4, HeightD6))
    HeightP4D4 = np.array(np.subtract(HeightP4, HeightD4))
    HeightP4D3 = np.array(np.subtract(HeightP4, HeightD3))
    
    HeightP3D6 = np.array(np.subtract(HeightP3, HeightD6))
    HeightP3D4 = np.array(np.subtract(HeightP3, HeightD4))
    HeightP3D3 = np.array(np.subtract(HeightP3, HeightD3))
    
    HeightP2D6 = np.array(np.subtract(HeightP2, HeightD6))
    HeightP2D4 = np.array(np.subtract(HeightP2, HeightD4))
    HeightP2D3 = np.array(np.subtract(HeightP2, HeightD3))
    
    HeightP1D6 = np.array(np.subtract(HeightP1, HeightD6))
    HeightP1D4 = np.array(np.subtract(HeightP1, HeightD4))
    HeightP1D3 = np.array(np.subtract(HeightP1, HeightD3))

#######################################################
 
    for x in HeightP6D6:
        lP6D6 = np.sqrt(2.89+(x**2))

    for x in HeightP5D6:
        lP5D6 = np.sqrt(2.89+(x**2))
    for x in HeightP5D4:
        lP5D4 = np.sqrt(2.89+(x**2))
   
    for x in HeightP4D6:
        lP4D6 = np.sqrt(2.89+(x**2))
    for x in HeightP4D4:
        lP4D4 = np.sqrt(2.89+(x**2))
    for x in HeightP4D3:
        lP4D3 = np.sqrt(2.89+(x**2))
     
    for x in HeightP3D6:
        lP3D6 = np.sqrt(2.89+(x**2))
    for x in HeightP3D4:
        lP3D4 = np.sqrt(2.89+(x**2))
    for x in HeightP3D3:
        lP3D3 = np.sqrt(2.89+(x**2))

    for x in HeightP2D6:
        lP2D6 = np.sqrt(2.89+(x**2))
    for x in HeightP2D4:
        lP2D4 = np.sqrt(2.89+(x**2))
    for x in HeightP2D3:
        lP2D3 = np.sqrt(2.89+(x**2))

    for x in HeightP1D6:
        lP1D6 = np.sqrt(2.89+(x**2))
    for x in HeightP1D4:
        lP1D4 = np.sqrt(2.89+(x**2))
    for x in HeightP1D3:
        lP1D3 = np.sqrt(2.89+(x**2))


######################################################
    LP6D6 = np.array(lP6D6)
    LP5D6 = np.array(lP5D6)
    LP5D4 = np.array(lP5D4)
    LP4D6 = np.array(lP4D6)
    LP4D4 = np.array(lP4D4)
    LP4D3 = np.array(lP4D3)
    LP3D6 = np.array(lP3D6)
    LP3D4 = np.array(lP3D4)
    LP3D3 = np.array(lP3D3)
    LP2D6 = np.array(lP2D6)
    LP2D4 = np.array(lP2D4)
    LP2D3 = np.array(lP2D3)
    LP1D6 = np.array(lP1D6)
    LP1D4 = np.array(lP1D4)
    LP1D3 = np.array(lP1D3)
    
    P6D6 = (HeightP6D6/LP6D6)
    P5D6 = (HeightP5D6/LP5D6)
    P5D4 = (HeightP5D4/LP5D4)
    P4D6 = (HeightP4D6/LP4D6)
    P4D4 = (HeightP4D4/LP4D4)
    P4D3 = (HeightP4D3/LP4D3)
    P3D6 = (HeightP3D6/LP3D6)
    P3D4 = (HeightP3D4/LP3D4)
    P3D3 = (HeightP3D3/LP3D3)
    P2D6 = (HeightP2D6/LP2D6)
    P2D4 = (HeightP2D4/LP2D4)
    P2D3 = (HeightP2D3/LP2D3)
    P1D6 = (HeightP1D6/LP1D6)
    P1D4 = (HeightP1D4/LP1D4)
    P1D3 = (HeightP1D3/LP1D3)
    
    for x in P6D6:
        CosP6D6 = np.degrees(np.arccos(x))
 
    for x in P5D6:    
        CosP5D6 = np.degrees(np.arccos(x))
    for x in P5D4:    
        CosP5D4 = np.degrees(np.arccos(x))
        
    for x in P4D6:
        CosP4D6 = np.degrees(np.arccos(x))
    for x in P4D4:
        CosP4D4 = np.degrees(np.arccos(x))
    for x in P4D3:
        CosP4D3 = np.degrees(np.arccos(x))
    
    for x in P3D6:
        CosP3D6 = np.degrees(np.arccos(x))
    for x in P3D4:
        CosP3D4 = np.degrees(np.arccos(x))
    for x in P3D3:
        CosP3D3 = np.degrees(np.arccos(x))
    
    for x in P2D6:
        CosP2D6 = np.degrees(np.arccos(x))
    for x in P2D4:
        CosP2D4 = np.degrees(np.arccos(x))
    for x in P2D3:
        CosP2D3 = np.degrees(np.arccos(x))
    
    for x in P1D6:
        CosP1D6 = np.degrees(np.arccos(x))
    for x in P1D4:
        CosP1D4 = np.degrees(np.arccos(x))
    for x in P1D3:
        CosP1D3 = np.degrees(np.arccos(x))

#######################################################
    return(HeightP6D6, HeightP5D6, HeightP5D4, HeightP4D6, HeightP4D4, HeightP4D3, HeightP3D6, HeightP3D4, HeightP3D3, HeightP2D6, HeightP2D4, HeightP2D3, HeightP1D6, HeightP1D4, HeightP1D3, LP6D6, LP5D6, LP5D4, LP4D6, LP4D4, LP4D3, LP3D6, LP3D4, LP3D3, LP2D6, LP2D4, LP2D3, LP1D6, LP1D4, LP1D3, CosP6D6, CosP5D6, CosP5D4, CosP4D6, CosP4D4, CosP4D3, CosP3D6, CosP3D4, CosP3D3, CosP2D6, CosP2D4, CosP2D3, CosP1D6, CosP1D4, CosP1D3)