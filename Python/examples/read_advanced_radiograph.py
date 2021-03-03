# read_advanced_radiograph.py: Template for reading Advanced Radiographs

import os
import numpy as np
import pradformat as prf

## Load object from pradformat file
h5filename = os.path.join('outs', 'myradiograph2.h5')
rad = prf.prad_load(h5filename)

## Examine your newly loaded object
print(rad)
for s in rad.sensitivities:
    print(s)

## Utilize object's datasets and attributes in your own scripts
assert isinstance(rad, prf.AdvancedRadiograph)

# rad.image # required | Radiograph image (cropped and rotated, if desired) | pixel count
# rad.X # optional | X position of pixel centers (radiograph coordinate system*) | meters
# rad.Y # optional | Y position of pixel centers (radiograph coordinate system*) | meters
# rad.T # optional | Change-of-basis matrix (a.k.a. transition matrix) to move from x, y, z radiograph coordinate system* to x', y', z' global coordinate system of the target chamber. [x' y' z'] = T [x y z].
#
# rad.object_type # required | Specification of the HDF5 object type | "radiograph" (always this value)
# rad.radiograph_type # required | Specification of the radiograph sub-type | "advanced" (always this value)
# rad.pradformat_version # required | HDF5 pradformat file format version followed | e.g. "0.1.0"
#
# rad.pixel_width # required | Physical pixel width / bin width, for the first image axis | meters
# rad.pixel_width_ax2 # optional | Physical pixel width / bin width, for the second image axis (not needed if using square pixels) | meters
# rad.source_object_dist # optional | Approximate distance from the particle source to the object plane (the E & M structures). Used to estimate image magnification. | meters
# rad.object_image_dist # optional | Approximate distance from the object plane (the E & M structures) to the image plane (the radiograph). Used to estimate image magnification. | meters
# rad.source_radius # optional | Approximate characteristic radius of the particle source (set as zero for a point source). Helpful in estimating image resolution. | meters
# 
# rad.label # optional | Short, identifying label for this file (with no spaces or crazy characters). This can be stamped onto plots, etc.
# rad.description # optional | Longer description of this file. This can be read by people trying to figure out where this file came from.
# rad.experiment_date # optional | Date of the experiment (or synthetic particle tracing), in the format "YYYY-MM-DD".
# rad.file_date # optional | Date the (future) file will be created, in the format "YYYY-MM-DD" | You don't need to set this, it will be set automatically
# rad.raw_data_filename # optional | Filename of the raw data file (e.g. CSV from MIT, Tiff from scanner, etc) from which this derivative file was created, if applicable.
#
# rad.sensitivities # optional | a cell array filled with Sensitivity objects (one for each species) | must always be a cell array, even if only one species is included
#
# for s in rad.sensitivities:
#     s.spec_name # required | Shortname for the particle species (for this group)**
#     s.spec_mass  # required | Particle mass (for this group) | kg
#     s.spec_charge # # required | Particle charge (for this group) | Coulombs
#     s.energies # required | Particle energy represented by each element of the scale_factors array
#     s.scale_factors # required | Multipliers to convert pixel counts into particle counts (wrapping in the effects of all prior layers in the detector stack)
#     s.prescale_factors # optional | Pre-multipliers by which to adjust the scale factors (e.g. a fudge factor to adjust for RCF batch-to-batch sensitivity differences unrelated to stopping distance)

# Dealing with required attributes/datasets
print(rad.pradformat_version)
print(np.mean(rad.image))

# Dealing with optional attributes/datasets
if  not isinstance(rad.label, type(None)):
    print(rad.label)
else:
    print("Well, I'd like to show you the label attribute, but I guess it wasn't set. Oh well.")

if len(rad.sensitivities) > 1:
    s = rad.sensitivities[1] # Python uses zero-indexed lists, so element '0' is sensitivity1, element '1' is sensitivity2, etc.
    print(s.spec_name)
else:
    print("I wanted to show you the species name for 'sensitivity2', but I guess a second sensitivity wasn't in there.")

##  Asterixed footnotes referenced above:
#
#  * The convention of this format is that the image lies in the z=0 plane of the radiograph coordinate system, and that the z-axis will point towards the particle source. The image may be stored already cropped and rotated by any angle within the x-y radiograph coordinate system, which is why X and Y are specified as arrays rather than vectors.
#
#  ** For best compatibility, consider using the PlasmaPy particle symbol conventions. https://docs.plasmapy.org/en/stable/api/plasmapy.particles.particle_symbol.html
#     For example, protons can be specified as just "p+", and electrons by "e-". Any arbitrary isotope of Hydrogen can be specified "H-I q+"? where I is the mass number and q is the charge.
#
