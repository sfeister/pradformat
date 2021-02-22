#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
advanced_radiograph.py: Read and write the HDF5 pradformat "Advanced Radiograph" file structure

Created by Scott Feister on Tue Feb  2 20:33:42 2021
"""

import h5py
import numpy as np
from datetime import datetime
from .__version__ import __version__

PRADFORMAT_VERSION = __version__ # awkward work-around to get __version__ variable into class

class Sensitivity(object):
    group_type = "sensitivity"

    # Categorize the above/below public properties (but not groups) as required or optional
    __req_ds = ["energies", "scale_factors"] # Required datasets
    __opt_ds = ["prescale_factors"] # Optional datasets
    __req_atts = [  # Required attributes
        "group_type", 
        "spec_name", 
        "spec_mass", 
        "spec_charge", 
        ]
    __opt_atts = []  # Optional attributes

    def __init__(self, h5group=None):
        # h5group is an open handle to an already-created HDF5 group
        self.energies = None
        self.scale_factors = None
        self.prescale_factors = None
        
        self.spec_name = None
        self.spec_mass = None
        self.spec_charge = None

        if not isinstance(h5group, type(None)):
            self.load(h5group)

    def __str__(self):
        mystr = "Sensitivity Object\n\n"
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
                raise Exception('Please assign a value to all required properties.\n The following required sensitivity dataset property is not yet assigned in at least one sensitivity: {0}.\n Assign a value via "object.sensitivities[x].{0} = value" and try again.'.format(ds))
        for att in self.__req_atts:
            if isinstance(getattr(self, att), type(None)):
                raise Exception('Please assign a value to all required properties.\n The following required sensitivity attribute property is not yet assigned in at least one sensitivity: {0}.\n Assign a value via "object.sensitivities[x].{0} = value" and try again.'.format(att))
        return

    def save(self, h5group, compression_opts=4):
        """ Saves Sensitivity object into an already-existing HDF5 group handle"""
        self.validate() # Before writing into this group, check that all required properties are set
        
        f = h5group # Let's call the group handle f just for simplicity of syntax relative to other types of objects
        
        # Write required datasets to file within this group
        for ds in self.__req_ds:
            data = getattr(self, ds)
            if not np.isscalar(data):
                f.create_dataset(ds, data=data, compression="gzip", compression_opts=compression_opts)
            else:
                f.create_dataset(ds, data=data) # Don't compress scalar datasets (e.g. single-element arrays)
                
        # Write optional datasets to file within this group
        for ds in self.__opt_ds:
            data = getattr(self, ds)
            if not isinstance(data, type(None)):
                if not np.isscalar(data):
                    f.create_dataset(ds, data=data, compression="gzip", compression_opts=compression_opts) # Compress only for datasets of length greater than one
                else:
                    f.create_dataset(ds, data=data)
            
        # Write required attributes to file within this group
        for att in self.__req_atts:
            f.attrs[att] = getattr(self, att)
            
        # Write optional attributes to file within this group
        for att in self.__opt_atts:
            if not isinstance(getattr(self, att), type(None)): 
                f.attrs[att] = getattr(self, att)

    def load(self, h5group):
        """ Load data from specified HDF5 group handle into this object """
        
        f = h5group # Let's call the group handle f just for simplicity of syntax relative to other types of objects
        
        # Read in required datasets
        for ds in self.__req_ds:
            setattr(self, ds, f[ds][()])
            
        # Read in optional datasets
        for ds in self.__opt_ds:
            if ds in f.keys():
                setattr(self, ds, f[ds][()])
            
        # Read in required attributes
        for att in self.__req_atts:
            if att not in ["group_type"]:
                setattr(self, att, f.attrs[att])
            
        # Read in optional attributes
        for att in self.__opt_atts:
            if att in f.attrs.keys(): 
                setattr(self, att, f.attrs[att])

class AdvancedRadiograph(object):
    """
    Object for storing data and attributes of a single radiograph created by multiple incident species and energies.
    """
    object_type = "radiograph"
    radiograph_type = "advanced"

    # Categorize the above/below public properties (but not groups) as required or optional
    __req_ds = ["image"] # Required datasets
    __opt_ds = ["X", "Y", "T"] # Optional datasets
    __req_atts = [  # Required attributes
        "object_type", 
        "radiograph_type", 
        "pradformat_version", 
        "pixel_width", 
        ]
    __opt_atts = [  # Optional attributes
        "pixel_width_ax2", 
        "source_distance", 
        "ROI_distance", 
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
        self.pixel_width = None
        self.pixel_width_ax2 = None
        self.source_distance = None
        self.ROI_distance = None
        self.label = None
        self.description = None
        self.experiment_date = None
        self.file_date = datetime.now().strftime("%Y-%m-%d")
        self.raw_data_filename = None
        
        self.sensitivities = [] # List of sensitivity objects

        if not isinstance(h5filename, type(None)):
            self.load(h5filename)

    def __str__(self):
        mystr = "Advanced Radiograph Object\n\n"
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
        
        mystr += "\nSensitivities: " + str(self.sensitivities) + "\n"
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
        
        # Validate all sensitivity group objects as well
        if not isinstance(self.sensitivities, type(None)):
            #TODO: Check that self.sensitivities is actually a proper list, and not mistakenly defined by the user as something else
            for sens in self.sensitivities:
                sens.validate()
        
        return

    def save(self, h5filename, compression_opts=4):
        """ Saves AdvancedRadiography object to HDF5 file"""
        self.validate() # Before opening a new HDF5 file, check that all required properties are set
        
        # Create file, overwriting if file already exists
        with h5py.File(h5filename, "w") as f: 
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

            # Write the sensitivity groups
            if not isinstance(self.sensitivities, type(None)):
                nsens = len(self.sensitivities) # Number of sensitivity groups to create
                for i in range(nsens):
                    h5group = f.create_group("sensitivity" + str(i + 1)) # e.g. "sensitivity5" groupname (1-indexed per format spec)
                    self.sensitivities[i].save(h5group) # save this sensitivity object into the above group

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
                    setattr(self, att, f.attrs[att])
                
            # Read in optional attributes
            for att in self.__opt_atts:
                if att in f.attrs.keys(): 
                    setattr(self, att, f.attrs[att])
            
            # Count the number of sensitivity groups (starting at 1 and counting up)
            i = 0
            while "sensitivity" + str(i + 1) in f.keys(): # e.g. sensitivity1, sensitivity2, ... (zero-indexed)
                i+=1
            nsens = i # Number of sensitivities in this file
            
            # Read in the sensitivity groups
            if nsens > 0:
                self.sensitivities = [None]*nsens # create an empty list of length nsens
                for i in range(nsens):
                    h5group = f["/sensitivity" + str(i + 1)]
                    self.sensitivities[i] = Sensitivity(h5group)
                               
if __name__ == "__main__":
    pass
