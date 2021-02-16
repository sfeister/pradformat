#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
example3_particles_list.py: Create an electron particle beam

Created by Scott Feister on Feb 16 2021
"""

import os
import numpy as np
from scipy.stats import uniform, norm
import scipy.constants as sc
import pradformat as prf

if __name__ == "__main__":
    # Construct object
    plist = prf.ParticlesList()

    # Define some general attributes
    plist.label = "ebeam_100MeV"
    plist.description = "100 MeV electrons emitted uniformly into a 3-degree half-cone angle. Source size is 2 microns standard deviation, centered on (0,0,0)."
    
    N = 1000 # Number of particles to generate
    
    # Define particle positions
    source_radius = 2.0e-6 # 2 micron for source radius (normal distribution standard deviation length)
    R = norm.rvs(size=N, scale=source_radius) # Radius is in a normal distribution of standard deviation source_radius
    theta = uniform.rvs(size=N, scale=np.pi) # theta is uniform from 0 to pi
    phi = uniform.rvs(size=N, loc=-np.pi, scale=2*np.pi) # phi is uniform from -pi to pi
    
    plist.x = R * np.sin(theta) * np.cos(phi)
    plist.y = R * np.sin(theta) * np.sin(phi)
    plist.z = R * np.cos(theta)
    
    
   # Define particle momenta
    pmag = 5.403e-21 # Magnitude of momentum for 100 MeV electron, in kg * m/s (I used Wolfram Alpha: https://www.wolframalpha.com/input/?i=100+MeV+electron+to+momentum)
    half_angle = np.deg2rad(3.0) # Allow for a 3-degree half-angle conical divergence of particle emission
    ptheta = uniform.rvs(size=N, scale=half_angle)
    pphi = uniform.rvs(size=N, loc=-half_angle, scale=2*half_angle)

    plist.px = pmag * np.sin(ptheta) * np.cos(pphi)
    plist.py = pmag * np.sin(ptheta) * np.sin(pphi)
    plist.pz = pmag * np.cos(ptheta)
    
    # Define additional particle attributes
    plist.charge = -sc.e
    plist.mass = sc.m_e
    plist.spec_name = "e-"
    plist.id = np.arange(N)

    # Save to file
    if not os.path.isdir("out"):
        os.mkdir("out")
    h5filename = os.path.join("out", "example3-o1.h5")
    plist.save(h5filename)
    
    # For demo purposes, read back in the file you just saved, then write it again
    plist2 = prf.prad_load(h5filename)
    plist2.save(os.path.join("out", "example3-o2.h5"))