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
from .simple_inversion import SimpleInversion
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
                raise Exception("The loaded file has the 'radiograph_type' attribute set to '" + str(radiograph_type) + "' which is not a supported value for this object type: '" + str(object_type) + "'. See pradformat format specs.")
        elif object_type == "fields":
            fields_type = _h5sanitize(f.attrs["fields_type"])
            if fields_type == "simple":
                return SimpleFields(h5filename)
            else:
                raise Exception("The loaded file has the 'fields_type' attribute set to '" + str(fields_type) + "' which is not a supported value for this object type: '" + str(object_type) + "'. See pradformat format specs.")
        elif object_type == "particles":
            particles_type = _h5sanitize(f.attrs["particles_type"])
            if particles_type == "list":
                return ParticlesList(h5filename)
            else:
                raise Exception("The loaded file has the 'particles_type' attribute set to '" + str(particles_type) + "' which is not a supported value for this object type: '" + str(object_type) + "'. See pradformat format specs.")
        elif object_type == "inversion":
            inversion_type = _h5sanitize(f.attrs["inversion_type"])
            if inversion_type == "simple":
                return SimpleInversion(h5filename)
            else:
                raise Exception("The loaded file has the 'inversion_type' attribute set to '" + str(inversion_type) + "' which is not a supported value for this object type: '" + str(object_type) + "'. See pradformat format specs.")
        else:
            raise Exception("The loaded file has the 'object_type' attribute set to '" + str(object_type) + "' which is not a supported value. See pradformat format specs.")
    
def prad_save(obj, h5filename):
    """ General write of a prad object """
    obj.save(h5filename)

if __name__ == "__main__":
    pass
