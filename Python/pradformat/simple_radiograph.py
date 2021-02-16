#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
advanced_radiograph.py: Read and write the HDF5 pradformat "Simple Radiograph" file structure

Created by Scott Feister on Tue Feb  2 20:33:42 2021
"""

import h5py

class SimpleRadiograph(object):
    """
    Object for storing data and attributes of a single radiograph created by single species at a single energy.
    """
    object_type = "radiograph"
    radiograph_type = "simple"

    def __init__(self):
        # Attributes.
        self.image = None
        self.X = None
        self.Y = None
        self.Z = None
        
        self.pradformat_version = PRADFORMAT_VERSION
        self.pixel_width = None
        self.scale_factor = None
        self.source_distance = None
        self.ROI_distance = None
        self.spec_name = None
        self.spec_mass = None
        self.spec_charge = None
        self.spec_energy = None

    def save(self, h5filename):
        """ Write out the HDF5 file """
        
        with h5py.File(h5filename, "w") as f: # Overwrites if file already exists!
            # Datasets
            if not isinstance(self.image, type(None)):
                f.create_dataset("image", data=self.image)
            if not isinstance(self.X, type(None)):
                f.create_dataset("X", data=self.X)
            if not isinstance(self.Y, type(None)):
                f.create_dataset("Y", data=self.Y)
            if not isinstance(self.Z, type(None)):
                f.create_dataset("Z", data=self.Z)
            
            # Attributes
            f.attrs["object_type"] = self.OBJECT_TYPE
            f.attrs["radiograph_type"] = self.RADIOGRAPH_TYPE
            f.attrs["pradformat_version"] = self.pradformat_version
            f.attrs["pradformat_language"] = "Python"
            if not isinstance(self.pixel_width, type(None)):
                f.attrs["pixel_width"] = self.pixel_width
            if not isinstance(self.scale_factor, type(None)):
                f.attrs["scale_factor"] = self.scale_factor
            if not isinstance(self.source_distance, type(None)):
                f.attrs["source_distance"] = self.source_distance
            if not isinstance(self.pixel_width, type(None)):
                f.attrs["pixel_width"] = self.pixel_width
            if not isinstance(self.ROI_distance, type(None)):
                f.attrs["ROI_distance"] = self.ROI_distance
            if not isinstance(self.spec_name, type(None)):
                f.attrs["spec_name"] = self.spec_name
            if not isinstance(self.spec_mass, type(None)):
                f.attrs["spec_mass"] = self.spec_mass
            if not isinstance(self.spec_charge, type(None)):
                f.attrs["spec_charge"] = self.spec_charge
            if not isinstance(self.spec_energy, type(None)):
                f.attrs["spec_energy"] = self.spec_energy
    
    def load(self, h5filename):
        """ Load data from HDF5 file into this object """
        
        with h5py.File(h5filename, "r") as f:
            self.image = f["image"][:]
            if "X" in f.keys():
                self.X = f["X"][:]
            if "Y" in f.keys():
                self.Y = f["Y"][:]
            if "Z" in f.keys():
                self.Z = f["Z"][:]
            #TODO: Finish all this jazz

            self.pradformat_version = f.attrs["pradformat_version"]
            self.pixel_width = f.attrs["pixel_width"]
            self.scale_factor = f.attrs["scale_factor"]
            if "source_distance" in f.attrs.keys():
                self.source_distance = f.attrs["source_distance"]
            if "ROI_distance" in f.attrs.keys():
                self.ROI_distance = f.attrs["ROI_distance"]
            if "spec_name" in f.attrs.keys():
                self.spec_name = f.attrs["spec_name"]
            if "spec_mass" in f.attrs.keys():
                self.spec_mass = f.attrs["spec_mass"]
            if "spec_charge" in f.attrs.keys():
                self.spec_charge = f.attrs["spec_charge"]
            if "spec_energy" in f.attrs.keys():
                self.spec_energy = f.attrs["spec_energy"]
                   
if __name__ == "__main__":
    pass
