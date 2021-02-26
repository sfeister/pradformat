#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simple_radiograph.py: Read and write the HDF5 pradformat "Simple Radiograph" file structure

Created by Scott Feister on Tue Feb  2 20:33:42 2021
"""

import h5py
import numpy as np
from datetime import datetime
from ._h5sanitize import _h5sanitize
from .__version__ import __version__

PRADFORMAT_VERSION = __version__ # awkward work-around to get __version__ variable into class

class SimpleRadiograph(object):
    """
    Object for storing data and attributes of a single radiograph created by single species at a single energy.
    """
    object_type = "radiograph"
    radiograph_type = "simple"

    # Categorize the above/below public properties as required or optional
    __req_ds = ["image"] # Required datasets
    __opt_ds = ["X", "Y", "T"] # Optional datasets
    __req_atts = [  # Required attributes
        "object_type", 
        "radiograph_type", 
        "pradformat_version", 
        "scale_factor", 
        "pixel_width", 
        ]
    __opt_atts = [  # Optional attributes
        "pixel_width_ax2", 
        "source_distance", 
        "ROI_distance", 
        "spec_name", 
        "spec_mass", 
        "spec_charge", 
        "spec_energy", 
        "label", 
        "description", 
        "experiment_date", 
        "file_date", 
        "raw_data_filename", 
        ]

    def __init__(self, h5filename=None):
        self.image = None
        self.X = None
        self.Y = None
        self.T = None
        
        self.pradformat_version = PRADFORMAT_VERSION
        self.scale_factor = None
        self.pixel_width = None
        self.pixel_width_ax2 = None
        self.source_distance = None
        self.ROI_distance = None
        self.spec_name = None
        self.spec_mass = None
        self.spec_charge = None
        self.spec_energy = None
        self.label = None
        self.description = None
        self.experiment_date = None
        self.file_date = datetime.now().strftime("%Y-%m-%d")
        self.raw_data_filename = None

        if not isinstance(h5filename, type(None)):
            self.load(h5filename)

    def __str__(self):
        mystr = "Simple Radiograph Object\n\n"
        mystr += "Required datasets: \n"
        for ds in self.__req_ds:
            data = getattr(self, ds)
            mystr += "  " + ds + ": "
            if isinstance(data, np.ndarray):
                mystr += str(data.shape) + " ndarray, dtype " + str(data.dtype)
            else:
                mystr += str(data)
            mystr += "\n"
                
        mystr += "\nOptional datasets: \n"
        for ds in self.__opt_ds:
            data = getattr(self, ds)
            mystr += "  " + ds + ": "
            if isinstance(data, np.ndarray):
                mystr += str(data.shape) + " ndarray, dtype " + str(data.dtype)
            else:
                mystr += str(data)
            mystr += "\n"

        mystr += "\nRequired attributes: \n"
        for att in self.__req_atts:
            mystr += "  " + att + ": " + str(getattr(self, att)) + "\n"
            
        mystr += "\nOptional attributes: \n"
        for att in self.__opt_atts:
            mystr += "  " + att + ": " + str(getattr(self, att)) + "\n"
        
        return mystr

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

    def save(self, filename, compression_opts=4):
        """ Saves SimpleFields object to HDF5 file"""
        self.validate() # Before opening a new HDF5 file, check that all required properties are set
        
        # Create file, overwriting if file already exists
        with h5py.File(filename, "w") as f: 
            # Write required datasets to file
            for ds in self.__req_ds:
                data = getattr(self, ds)
                if not np.isscalar(data):
                    f.create_dataset(ds, data=data, compression="gzip", compression_opts=compression_opts)
                else:
                    f.create_dataset(ds, data=data) # Don't compress scalar datasets (e.g. single-element arrays)
                    
            # Write optional datasets to file
            for ds in self.__opt_ds:
                data = getattr(self, ds)
                if not isinstance(data, type(None)):
                    if not np.isscalar(data):
                        f.create_dataset(ds, data=data, compression="gzip", compression_opts=compression_opts) # Compress only for datasets of length greater than one
                    else:
                        f.create_dataset(ds, data=data)
                
            # Write required attributes to file
            for att in self.__req_atts:
                f.attrs[att] = getattr(self, att)
                
            # Write optional attributes to file
            for att in self.__opt_atts:
                if not isinstance(getattr(self, att), type(None)): 
                    f.attrs[att] = getattr(self, att)
    
    def load(self, h5filename):
        """ Load data from HDF5 file into this object """
        with h5py.File(h5filename, "r") as f: 
            # Read in required datasets
            for ds in self.__req_ds:
                setattr(self, ds, f["/" + ds][()])
                
            # Read in optional datasets
            for ds in self.__opt_ds:
                if ds in f.keys():
                    setattr(self, ds, f["/" + ds][()])
                
            # Read in required attributes
            for att in self.__req_atts:
                if att not in ["object_type", "radiograph_type"]:
                    setattr(self, att, _h5sanitize(f.attrs[att]))
                
            # Read in optional attributes
            for att in self.__opt_atts:
                if att in f.attrs.keys(): 
                    setattr(self, att, _h5sanitize(f.attrs[att]))
                   
if __name__ == "__main__":
    pass
