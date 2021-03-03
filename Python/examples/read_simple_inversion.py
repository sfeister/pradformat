# read_simple_inversion.py: Template for reading a Simple Inversion file

import os
import numpy as np
import pradformat as prf

## Load object from pradformat file
h5filename = os.path.join('outs', 'myinversion.h5')
siv = prf.prad_load(h5filename)

## Examine your newly loaded object
print(siv)

## Utilize object's datasets and attributes in your own scripts
assert isinstance(siv, prf.SimpleInversion)

# siv.phi # optional* | Deflection potential in the object plane, the gradient of which gives the deflection angles. Omit only if the solution is not representable by a potential -- in which case specifying the deflection angles is required. | meters
# siv.defl_ax1 # optional* | Deflection angle along axis-1 (= grad phi, axis 1 component). Values can be positive (for deflection in +ax1 direction) or negative (for deflection in -ax1 direction). | rad
# siv.defl_ax2 # optional* | Deflection angle along axis-2 (= grad phi, axis 2 component). Values can be positive (for deflection in +ax1 direction) or negative (for deflection in -ax1 direction). | rad
#
# siv.object_type # required | Specification of the HDF5 object type | "inversion" (always this value)
# siv.inversion_type # required | Specification of the inversion sub-type | "simple" (always this value)
# siv.pradformat_version # required | HDF5 pradformat file format version followed | e.g. "0.1.0"
# 
# siv.dr # required | Bin spacing along axis-1, in the object plane | meters
# 
# siv.source_object_dist # required | Approximate distance from the particle source to the object plane (the E & M structures). Used to estimate image magnification. | meters
# siv.object_image_dist # required | Approximate distance from the object plane (the E & M structures) to the image plane (the radiograph). Used to estimate image magnification. | meters
# 
# siv.spec_name # required | Shortname for the particle species**
# siv.spec_mass # required | Particle mass | kg
# siv.spec_charge # required | Particle charge | Coulombs
# siv.spec_energy # required | Particle energy | eV
# 
# siv.dr_ax2 # optional | Bin spacing along axis-2, in the object plane | meters
# siv.source_radius # optional | Approximate characteristic radius of the particle source (set as zero for a point source). Helpful in estimating image resolution. | meters
# siv.label # optional | Short, identifying label for this file (with no spaces or crazy characters). This can be stamped onto plots, etc.
# siv.description # optional | Longer description of this file. This can be read by people trying to figure out where this file came from.
# siv.file_date # optional | Date the (future) file will be created, in the format "YYYY-MM-DD" | You don't need to set this, it will be set automatically
# siv.radiograph_filename # optional | If this is an inversion, the *SimpleRadiograph* pradformat file from which this data was inverted
# siv.fields_filename # optional | If this is an exact solution, the *SimpleFields* pradformat file from which this data was projected


# Dealing with required attributes/datasets
print(siv.pradformat_version)
print(siv.dr)

# Dealing with optional attributes/datasets
if  not isinstance(siv.label, type(None)):
    print(siv.label)
else:
    print("Well, I'd like to show you the label attribute, but I guess it wasn't set. Oh well.")

if isinstance(siv.defl_ax1, type(None)) or  isinstance(siv.defl_ax2, type(None)):
    defl_ax1 = np.gradient(siv.phi, siv.dr, axis=0)
    defl_ax2 = np.gradient(siv.phi, siv.dr, axis=1)

##  Asterixed footnotes referenced above:
#
#  *  Either deflection potential or deflection angles must be specified (or both if you'd like).
#
#  ** For best compatibility, consider using the PlasmaPy particle symbol conventions. https://docs.plasmapy.org/en/stable/api/plasmapy.particles.particle_symbol.html
#     For example, protons can be specified as just "p+", and electrons by "e-". Any arbitrary isotope of Hydrogen can be specified "H-I q+"? where I is the mass number and q is the charge.
#