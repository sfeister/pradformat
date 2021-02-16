#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
particles_list.py: Read and write the HDF5 pradformat "Particles List" file structure

Created by Scott Feister on Feb 15 2021
"""

import h5py
import numpy as np
from .__version__ import __version__

PRADFORMAT_VERSION = __version__ # awkward work-around to get __version__ variable into class

class ParticlesList(object):
    """
    Object for storing a list of particles and their attributes.
    """
    object_type = "particles"
    particles_type = "list"
    
    # Categorize the above/below public properties as required or optional
    __req_ds = ["x", "y", "z", "px", "py", "pz", "charge", "mass"] # Required datasets
    __opt_ds = ["energy", "weight", "spec_name", "id"] # Optional datasets
    __req_atts = [  # Required attributes
        "object_type", 
        "particles_type", 
        "pradformat_version", 
        ]
    __opt_atts = [  # Optional attributes
        "shuffled", 
        "label", 
        "description", 
        "file_date", 
        "raw_data_filename", 
        ]
                
    def __init__(self, h5filename=None):
        self.x = None
        self.y = None
        self.z = None
        self.px = None
        self.py = None
        self.pz = None
        self.charge = None
        self.mass = None
        self.energy = None
        self.weight = None
        self.spec_name = None
        self.id = None
        self.pradformat_version = PRADFORMAT_VERSION
        self.shuffled = None
        self.label = None
        self.description = None
        self.file_date = datetime.now().strftime("%Y-%m-%d")
        self.raw_data_filename = None
        
        if not isinstance(h5filename, type(None)):
            self.load(h5filename)

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
                if att not in ["object_type", "particles_type"]:
                    setattr(self, att, f.attrs[att])
                
            # Read in optional attributes
            for att in self.__opt_atts:
                if att in f.attrs.keys(): 
                    setattr(self, att, f.attrs[att])

if __name__ == "__main__":
    pass
