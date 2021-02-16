#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
example1_simple_radiograph.py: Read and write the simple radiograph format for HDF5 pradtools

Example 100x300 CR39 radiograph for 14.7 MeV protons

Created by Scott Feister on Thu Feb  4 14:26:36 2021
"""

import os
import numpy as np
import pradformat as prf

if __name__ == "__main__":
    # Construct object
    rad = prf.SimpleRadiograph()
    
    nx = 100
    ny = 300
    rad.image = np.random.randint(5000, size=(nx, ny)) # Random radiograph image
    rad.pixel_width = 100.0e-6 # 100-micron bin size
    rad.scale_factor = 1 # one pixel count represents one particle count
    rad.source_distance = 1.53 # Proton source was 1.53 meters from the CR39
    rad.ROI_distance = 1.45 # Plasma of interest was 1.45 meters from the CR39
    rad.spec_name = "p+"
    rad.spec_mass = 1.67262e-27 # proton mass in kg
    rad.spec_charge = 1.6021766208e-19 # proton charge in Coulombs
    rad.spec_energy = 14.7e6 # 14.7 MeV protons
    
    # Save to file
    if not os.path.isdir("out"):
        os.mkdir("out")
    h5filename = os.path.join("out", "example1-o1.h5")
    rad.save(h5filename)
    
    # For demo purposes, read back in the file you just saved, then write it again
    rad2 = prf.prad_load(h5filename)
    rad2.save(os.path.join("out", "example1-o2.h5"))