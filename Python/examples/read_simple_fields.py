# read_simple_fields.py: Template for reading Simple Fields

import os
import numpy as np
import pradformat as prf

## Load object from pradformat file
h5filename = os.path.join('outs', 'myfields.h5')
fld = prf.prad_load(h5filename)

## Examine your newly loaded object
print(fld)

## Utilize object's datasets and attributes in your own scripts
assert isinstance(fld, prf.SimpleFields)

# fld.X # required | X values | meters
# fld.Y # required | Y values | meters
# fld.Z # required | Z values | meters
# fld.Ex # required | Electric field, x-component | Volts/meter
# fld.Ey # required | Electric field, y-component | Volts/meter
# fld.Ez # required | Electric field, z-component | Volts/meter
# fld.Bx # required | Magnetic field, x-component | Tesla
# fld.By # required | Magnetic field, y-component | Tesla
# fld.Bz # required | Magnetic field, z-component | Tesla
# fld.rho # optional | Mass density | kg / m**3
# 
# fld.object_type # required | Specification of the HDF5 object type | "fields" (always this value)
# fld.fields_type # required | Specification of the fields sub-type | "simple" (always this value)
# fld.pradformat_version # required | HDF5 pradformat file format version followed | e.g. "0.1.0"
# 
# fld.rho_description # optional | A qualitative description of the material represented by rho.
# fld.label # optional | Short, identifying label for this file (with no spaces or crazy characters). This can be stamped onto plots, etc.
# fld.description # optional | Longer description of this file. This can be read by people trying to figure out where this file came from.
# fld.file_date # optional | Date the (future) file will be created, in the format "YYYY-MM-DD" | You don't need to set this, it will be set automatically
# fld.raw_data_filename # optional | Filename of the raw data file (e.g. simulation output) from which this derivative file was created, if applicable.

# Dealing with required attributes/datasets
print(fld.pradformat_version)
print(np.mean(fld.Ex))

# Dealing with optional attributes/datasets
if  not isinstance(fld.label, type(None)):
    print(fld.label)
else:
    print("Well, I'd like to show you the label attribute, but I guess it wasn't set. Oh well.")