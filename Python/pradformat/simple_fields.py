#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple_fields.py: Read and write the HDF5 pradformat "Simple Fields" file structure

Created by Scott Feister on Wed Feb  3 16:46:49 2021
"""

import h5py

class SimpleFields(object):
    """
    Object for storing electric and magnetic field values on a uniform grid.
    """
    OBJECT_TYPE = "fields"
    FIELDS_TYPE = "simple"
    
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
        self.rho = None
        self.pradformat_version = "0.0.0"
        self.rho_description = None

    def write(self, f):
        """ Write the radiograph within an open HDF5 file object or filename string f"""
        if isinstance(f, str): # if f is not an open file handle
            filename = f
            f = h5py.File(filename, "w") # Overwrites if file already exists!
        else:
            filename = None
        
        f.attrs["object_type"] = self.OBJECT_TYPE
        f.attrs["fields_type"] = self.FIELDS_TYPE
        f.attrs["pradformat_version"] = self.pradformat_version # TODO: Pull this stamp dynamically
        f.attrs["pradformat_language"] = "Python"
        if not isinstance(self.rho_description, type(None)):
            f.attrs["rho_description"] = self.rho_description
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
        if not isinstance(self.rho, type(None)):
            f.create_dataset("rho", data=self.rho)

        if filename: # Close the file if it wasn't input as an open file handle
            f.close()

if __name__ == "__main__":
    pass
