#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
example4_advanced_radiograph.py: Read and write the simple radiograph format for HDF5 pradtools

Example RCF layer radiograph for 25 MeV protons (but with some sensitivity to higher energy protons)

Created by Scott Feister on Thu Feb  4 14:26:36 2021
"""

import os
import numpy as np
import scipy.constants as sc
import pradformat as prf

if __name__ == "__main__":
    # Construct object
    rad = prf.AdvancedRadiograph()
    rad.label = "MarchDISC_RCF_layer3"
    rad.description = "Layer 3 of the RCF stack on shot number 2 at OMEGA 2021 DISC. This layer is primarily sensitive to 25 MeV protons"
    rad.experiment_date = "2021-02-29"
    
    nx = 100
    ny = 300
    rad.image = np.random.randint(5000, size=(nx, ny)) # Random radiograph image of this RCF layer
    rad.pixel_width = 100.0e-6 # 100-micron bin size
    rad.source_distance = 1.53 # Proton source was 1.53 meters from the RCF layer
    rad.ROI_distance = 1.45 # Plasma of interest was 1.45 meters from the RCF layer

    rad.sensitivities = [] # Must always be a list, even if only one species is included

    # Proton sensitivity
    s = prf.Sensitivity()
    s.spec_name = "p+"
    s.spec_mass = sc.m_p # proton mass in kg
    s.spec_charge = sc.e # proton charge in Coulombs
    s.energies = np.array([20.0, 25.0, 30.0, 40.0]) # energies for which sensitivities are characterized for this species
    s.scale_factors = np.array([1.0e20, 1.0e18, 1.0e19, 1.5e19]) # incident particles/pixel-count for these energies (factoring in the layers in front of this RCF layer)
    rad.sensitivities.append(s)

    # Electron sensitivity
    s = prf.Sensitivity()
    s.spec_name = "e-" 
    s.spec_mass = sc.m_e # electron mass in kg
    s.spec_charge = -sc.e # electron charge in Coulombs (note negative sign)
    s.energies = np.array([20.0, 100.0, 200.0]) # energies for which sensitivities are characterized for this species
    s.scale_factors = np.array([1.0e21, 1.0e20, 1.0e19]) # incident particles/pixel-count for these energies (factoring in the layers in front of this RCF layer)
    rad.sensitivities.append(s)
    
    # Save to file
    if not os.path.isdir("out"):
        os.mkdir("out")
    h5filename = os.path.join("out", "example4-o1.h5")
    rad.save(h5filename)
    
    # For demo purposes, read back in the file you just saved, then write it again
    rad2 = prf.prad_load(h5filename)
    rad2.save(os.path.join("out", "example4-o2.h5"))