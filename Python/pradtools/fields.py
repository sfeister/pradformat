#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fields.py: Read and write the HDF5 pradtools "Fields" file structure

A grid of E & M field values like Ex, Ey, Ez, Bx, By, Bz.

This is a relatively simple file format. Perhaps more complicated file formats will be needed in the future.

Created by Scott Feister on Wed Feb  3 16:46:49 2021
"""

import h5py

class Fields(object):
    """
    Object for storing electric and magnetic field values on a uniform grid.
    """
    def __init__(self):
        # Attributes.
        self.X = None
        self.Y = None
        self.Z = None
        self.Ex = None
        self.Ey = None
        self.Ez = None
        self.Bx = None
        self.By = None
        self.Bz = None
        self.units = "SI"

    def write(self, f):
        """ Write the radiograph within an open HDF5 file object or filename string f"""
        if isinstance(f, str): # if f is not an open file handle
            filename = f
            f = h5py.File(filename, "w") # Overwrites if file already exists!
        else:
            filename = None
        
        f.attrs["type"] = "fields"
        f.attrs["pradtools_version"] = "0.0.0" # TODO: Pull this stamp dynamically
        f.attrs["pradtools_language"] = "Python"
        if not isinstance(self.units, type(None)):
            f.attrs["units"] = self.units
            f.attrs["units_description"] = "Units system used for all attribute values of this radiograph."
        if not isinstance(self.X, type(None)):
            f.create_dataset("X", data=self.X)
        if not isinstance(self.Y, type(None)):
            f.create_dataset("Y", data=self.Y)
        if not isinstance(self.Z, type(None)):
            f.create_dataset("Z", data=self.Z)
        if not isinstance(self.Ex, type(None)):
            f.create_dataset("Ex", data=self.Ex)
        if not isinstance(self.Ey, type(None)):
            f.create_dataset("Ey", data=self.Ey)
        if not isinstance(self.Ez, type(None)):
            f.create_dataset("Ez", data=self.Ez)
        if not isinstance(self.Bx, type(None)):
            f.create_dataset("Bx", data=self.Bx)
        if not isinstance(self.By, type(None)):
            f.create_dataset("By", data=self.By)
        if not isinstance(self.Bz, type(None)):
            f.create_dataset("Bz", data=self.Bz)

        if filename: # Close the file if it wasn't input as an open file handle
            f.close()

if __name__ == "__main__":
    pass
