# write_simple_inversion.py: A template for writing your own Simple Inversion

import os
import numpy as np
import pradformat as prf

## Construct object
siv = prf.SimpleInversion()

## Set datasets and attributes
M = 800 # image first dimension
N = 600 # image second dimension

siv.phi = np.zeros((M, N)) # optional* | Deflection potential in the object plane, the gradient of which gives the deflection angles. Omit only if the solution is not representable by a potential -- in which case specifying the deflection angles is required. | meters
# siv.defl_ax1 = np.zeros((M,N)) # optional* | Deflection angle along axis-1 (= grad phi, axis 1 component). Values can be positive (for deflection in +ax1 direction) or negative (for deflection in -ax1 direction). | rad
# siv.defl_ax2 = np.zeros((M,N)) # optional* | Deflection angle along axis-2 (= grad phi, axis 2 component). Values can be positive (for deflection in +ax1 direction) or negative (for deflection in -ax1 direction). | rad

# print(siv.object_type) # already-set | Specification of the HDF5 object type | "inversion" (always this value)
# print(siv.inversion_type) # already-set | Specification of the inversion sub-type | "simple" (always this value)
# print(siv.pradformat_version) # already-set | HDF5 pradformat file format version followed | e.g. "0.1.0"

siv.dr = 2.5e-6 # required | Bin spacing along axis-1, in the object plane | meters
siv.defl_ax1 = np.gradient(siv.phi, siv.dr, axis=0)
siv.defl_ax2 = np.gradient(siv.phi, siv.dr, axis=1)

siv.source_object_dist = 0.11 # required | Approximate distance from the particle source to the object plane (the E & M structures). Used to estimate image magnification. | meters
siv.object_image_dist = 1.45 # required | Approximate distance from the object plane (the E & M structures) to the image plane (the radiograph). Used to estimate image magnification. | meters

siv.spec_name = "p+" # required | Shortname for the particle species**
siv.spec_mass = 1.67262e-27 # required | Particle mass | kg
siv.spec_charge = 1.6021766208e-19 # required | Particle charge | Coulombs
siv.spec_energy = 14.7e6 # required | Particle energy | eV

# siv.dr_ax2 = 5.0e-6 # optional | Bin spacing along axis-2, in the object plane | meters
siv.source_radius = 80.0e-6 # optional | Approximate characteristic radius of the particle source (set as zero for a point source). Helpful in estimating image resolution. | meters
siv.label = "PROBLEM_inversion_shot3" # optional | Short, identifying label for this file (with no spaces or crazy characters). This can be stamped onto plots, etc.
siv.description = "Inversion using PROBLEM of a CR39 radiograph from shot 3 on the February 2021 NIF DISC run." # optional | Longer description of this file. This can be read by people trying to figure out where this file came from.
# print(siv.file_date) # automatically-set | Date the (future) file will be created, in the format "YYYY-MM-DD" | You don't need to set this, it will be set automatically
# siv.radiograph_filename = "/home/scott/prad/myradiograph.h5" # optional | If this is an inversion, the *SimpleRadiograph* pradformat file from which this data was inverted
# siv.fields_filename = "/home/scott/synth/myfields.h5" # optional | If this is an exact solution, the *SimpleFields* pradformat file from which this data was projected

## Pretty print your newly-minted radiograph object
print(siv)

## Save to file
if not os.path.isdir("outs"):
    os.mkdir("outs")
h5filename = os.path.join('outs', 'myinversion.h5')
siv.save(h5filename)

##  Asterixed footnotes referenced above:
#
#  *  Either deflection potential or deflection angles must be specified (or both if you'd like).
#
#  ** For best compatibility, consider using the PlasmaPy particle symbol conventions. https://docs.plasmapy.org/en/stable/api/plasmapy.particles.particle_symbol.html
#     For example, protons can be specified as just "p+", and electrons by "e-". Any arbitrary isotope of Hydrogen can be specified "H-I q+"? where I is the mass number and q is the charge.
#