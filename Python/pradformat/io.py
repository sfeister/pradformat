#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
io.py: Reading and writing prad files; mostly wrappers around other functions

Created by Scott Feister on Thu Feb  4 14:33:07 2021
"""

import h5py
from .simple_radiograph import SimpleRadiograph
from .simple_fields import SimpleFields

def prad_load(h5filename):
    """ General reader for pradformat HDF5 file formats"""
    obj = None
    with h5py.File(h5filename, "r") as f:
        object_type = f.attrs["object_type"]
        if object_type == "radiograph":
            radiograph_type =  f.attrs["radiograph_type"]
            if radiograph_type == "simple":
                obj = SimpleRadiograph()
            else:
                raise Exception("Bad radiograph_type.")
        elif object_type == "fields":
            fields_type = f.attrs["fields_type"]
            if fields_type == "simple":
                obj = SimpleFields()
            else:
                raise Exception("Bad fields_type.")
        else:
            raise Exception("Bad object_type.")
    
    if not isinstance(obj, type(None)):
        obj.load(h5filename)
        return obj
    else:
        raise Exception("No object loaded.")

def prad_save(obj, h5filename):
    """ General write of a prad object """
    obj.save(h5filename)

if __name__ == "__main__":
    pass
