# read_extended.py: Example of reading in an extended pradformat HDF5 file
#   That is, reading in your own non-pradformat datasets and attributes
#       that you added to a pradformat HDF5 file

import os
import h5py
import numpy as np
import pradformat as prf

## Load pradformat object as usual (only reads in the pradformat HDF5 items)
h5filename = os.path.join('outs', 'myextendedfields.h5')
fld = prf.prad_load(h5filename)

## Load in any custom datasets and attributes you added to the HDF5 file
with h5py.File(h5filename, "r") as f:
    nele = f['nele'][()]
    nion = f['nion'][()]
    run_number = f.attrs['run_number']

## Utilize datasets and attributes in your own scripts
assert isinstance(fld, prf.SimpleFields)

print(fld.pradformat_version)
print(np.mean(fld.Ex))
print(np.mean(nele))
print(np.mean(nion))
print(run_number)