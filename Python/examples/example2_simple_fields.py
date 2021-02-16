#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
example2_simple_fields.py: Write and read the simple fields format for HDF5 pradformat

Example 100 x 300 x 400 spatial grid

Covering the XYZ spatial coordinate ranges (-5.0, 5.0) meters, (-15.0, 15.0) meters,
and (-20.0, 20.0) meters, respectively.

Created by Scott Feister on Feb 15 2021
"""

import os
import numpy as np
import pradformat as prf

if __name__ == "__main__":
    # Construct object
    fld = prf.SimpleFields()

    nx = 100
    ny = 300
    nz = 400
    x = np.linspace(-5.0, 5.0, nx)
    y = np.linspace(-10.0, 10.0, ny)
    z = np.linspace(-20.0, 20.0, nz)
    [X,Y,Z] = np.meshgrid(x,y,z, indexing="ij")
    fld.X = X
    fld.Y = Y
    fld.Z = Z
    fld.Ex = X**2 + Y**2 # Electric fields that depend on X, Y, and Z
    fld.Ey = 0.0 # Electric fields that depend on X, Y, and Z
    fld.Ez = 5.823 * X**2 + Z**2 # Electric fields that depend on X, Y, and Z
    fld.Bx = X**4 + Z**2 # Magnetic fields that depend on X, Y, and Z
    fld.By = 2.191 + Y + Z**2; # Magnetic fields that depend on X, Y, and Z
    fld.Bz = 8.123 # Magnetic fields that depend on X, Y, and Z

    # Save to file
    if not os.path.isdir("out"):
        os.mkdir("out")
    h5filename = os.path.join("out", "example2.h5")
    fld.save(h5filename)
    
    # For demo purposes, read back in the file you just saved, then write it again
    #fld2 = prf.prad_load(h5filename)
    #fld2.save(h5filename)