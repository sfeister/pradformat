#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
general.py: Reading and writing prad files; mostly wrappers around other functions

Created by Scott Feister on Thu Feb  4 14:33:07 2021
"""

import h5py
from .simple_radiograph import SimpleRadiograph
from .simple_fields import SimpleFields
from .particles_list import ParticlesList
from .advanced_radiograph import AdvancedRadiograph
from ._h5sanitize import _h5sanitize

def prad_load(h5filename):
    """ General reader for pradformat HDF5 file formats"""
    obj = None
    with h5py.File(h5filename, "r") as f:
        object_type = _h5sanitize(f.attrs["object_type"])
        if object_type == "radiograph":
            radiograph_type = _h5sanitize(f.attrs["radiograph_type"])
            if radiograph_type == "simple":
                return SimpleRadiograph(h5filename)
            elif radiograph_type == "advanced":
                return AdvancedRadiograph(h5filename)
            else:
                raise Exception("Bad radiograph_type.")
        elif object_type == "fields":
            fields_type = _h5sanitize(f.attrs["fields_type"])
            if fields_type == "simple":
                return SimpleFields(h5filename)
            else:
                raise Exception("Bad fields_type.")
        elif object_type == "particles":
            particles_type = _h5sanitize(f.attrs["particles_type"])
            if particles_type == "list":
                return ParticlesList(h5filename)
            else:
                raise Exception("Bad particles_type.")
        else:
            raise Exception("Bad object_type: " + str(object_type))
    
def prad_save(obj, h5filename):
    """ General write of a prad object """
    obj.save(h5filename)

if __name__ == "__main__":
    pass
