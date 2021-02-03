#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_radiograph.py: Example of writing radiograph data to a properly-formatted HDF5 file

Example of writing a monochromatic radiograph to file.

Created by Scott Feister on Wed Feb  3 14:37:45 2021
"""

import os
import numpy as np
import scipy.constants as sc
from flsuite import sftools as sf
import pradtools as pr
import h5py

if __name__ == "__main__":
    # Create synthetic radiograph image for 10 cm x 15 cm CR39 scan of 14.7 MeV protons, with 25um bin size       
    nx = np.int(np.round(10.0e-2 / 25.0e-6)) # Number of bins in x-dimension (10 cm / 25 microns = 4000 bins)
    ny = np.int(np.round(15.0e-2 / 25.0e-6)) # Number of bins in y-dimension (15 cm / 25 microns = 6000 bins)

    outdir = sf.subdir2(".", "out")
    h5fn = os.path.join(outdir, "example1.hdf5") # Output HDF5 filename
    
    rad = pr.Radiograph()

    rad.image = np.random.randint(1000, size=(nx, ny)) # CR39 flux image
    rad.xmin = -5.0e-2 # CR39 image coordinates, in meters
    rad.xmax = 5.0e-2
    rad.dx = 25.0e-6 # 25-um bin size
    rad.ymin = -7.5e-2
    rad.ymax = 7.5e-2
    rad.dy = 25.0e-6
    rad.source_distance = 1.505 # Distance from the radiograph to the particle source, in meters
    rad.ROI_distance = 1.452 # Distance from the radiograph to the imaged region of interest, in meters
    
    spec = pr.Species(name="proton", mass=sc.m_p, charge=sc.e)
    sens = pr.Sensitivity(energy=[14.7e6], sensitivity=[1.0], species=spec)
    rad.sensitivities = [sens] # List of sensitivity objects (one per species)
    
    with h5py.File(h5fn, "w") as f:
        rad.write(f)
