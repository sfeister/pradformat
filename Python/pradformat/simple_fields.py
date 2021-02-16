#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple_fields.py: Read and write the HDF5 pradformat "Simple Fields" file structure

Created by Scott Feister on Wed Feb  3 16:46:49 2021
"""

import h5py
from .__version__ import __version__

PRADFORMAT_VERSION = __version__ # awkward work-around to get __version__ variable into class

class SimpleFields(object):
    """
    Object for storing electric and magnetic field values on a uniform grid.
    """
    object_type = "fields"
    fields_type = "simple"
    
    # Categorize the above/below public properties as required or optional
    __req_ds = ["X", "Y", "Z", "Ex", "Ey", "Ez", "Bx", "By", "Bz"] # Required datasets
    __opt_ds = ["rho"] # Optional datasets
    __req_atts = [  # Required attributes
        "object_type", 
        "fields_type", 
        "pradformat_version", 
        ]
    __opt_atts = [  # Optional attributes
        "rho_description", 
        "label", 
        "description", 
        "file_date", 
        "raw_data_filename", 
        ]
        
    def __init__(self):
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
        self.pradformat_version = PRADFORMAT_VERSION
        self.rho_description = None
        self.label = None
        self.description = None
        self.file_date = None
        self.raw_data_filename = None

    def validate(self):
        # Validate that all required properties have been set.
        # If some are not, throw an error.
        for ds in self.__req_ds:
            if isinstance(getattr(self, ds), type(None)):
                raise Exception('Please assign a value to all required properties.\n The following required dataset property is not yet assigned: {0}.\n Assign a value via "object.{0} = value" and try again.'.format(ds))
        for att in self.__req_atts:
            if isinstance(getattr(self, att), type(None)):
                raise Exception('Please assign a value to all required properties.\n The following required attribute property is not yet assigned: {0}.\n Assign a value via "object.{0} = value" and try again.'.format(att))
        return

    def save(self, filename):
        """ Saves SimpleFields object to HDF5 file"""
        self.validate() # Before opening a new HDF5 file, check that all required properties are set
        
        # Create file, overwriting if file already exists
        with h5py.File(filename, "w") as f: 
            # Write required datasets to file
            for ds in self.__req_ds:
                f.create_dataset(ds, data=getattr(self, ds))
                
            # Write optional datasets to file
            for ds in self.__opt_ds:
                if not isinstance(getattr(self, ds), type(None)): 
                    f.create_dataset(ds, data=getattr(self, ds))
                
            # Write required datasets to file
            for att in self.__req_atts:
                f.attrs[att] = getattr(self, att)
                
            # Write optional datasets to file
            for att in self.__opt_atts:
                if not isinstance(getattr(self, att), type(None)): 
                    f.attrs[att] = getattr(self, att)

if __name__ == "__main__":
    pass
