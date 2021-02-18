# read_simple_radiograph.py: Template for reading Simple Radiographs

import os
import pradformat as prf

## Load object from pradformat file
h5filename = os.path.join('outs', 'myradiograph.h5')
rad = prf.prad_load(h5filename)

## Examine your newly loaded object
print(rad)

## Utilize object's datasets and attributes in your own scripts
assert isinstance(rad, prf.SimpleRadiograph)

rad.image # required | Radiograph image (cropped and rotated, if desired) | pixel count
# rad.X # optional | X position of pixel centers (radiograph coordinate system*) | meters
# rad.Y # optional | Y position of pixel centers (radiograph coordinate system*) | meters
# rad.T # optional | Change-of-basis matrix (a.k.a. transition matrix) to move from x, y, z radiograph coordinate system* to x', y', z' global coordinate system of the target chamber. [x' y' z'] = T [x y z].

rad.object_type # required | Specification of the HDF5 object type | "radiograph" (always this value)
rad.radiograph_type # required | Specification of the HDF5 object type | "simple" (always this value)
rad.pradformat_version # required | HDF5 pradformat file format version followed | e.g. "0.1.0"

rad.scale_factor # required | Multiplier to convert pixel counts into particle counts | particles/pixel count
rad.pixel_width # required | Physical pixel width / bin width, for the first image axis | meters
# rad.pixel_width_ax2 # optional | Physical pixel width / bin width, for the second image axis (not needed if using square pixels) | meters
# rad.source_distance # optional | Approximate distance from the particle source to the plane of the radiograph | meters
# rad.ROI_distance # optional | Approximate distance from the center of the imaged region of interest to the plane of the radiograph | meters
# rad.spec_name # optional | Shortname for the particle species**
# rad.spec_mass # optional | Particle mass | kg
# rad.spec_charge # optional | Particle charge | Coulombs
# rad.spec_energy # optional | Particle energy | eV

# rad.label # optional | Short, identifying label for this file (with no spaces or crazy characters). This can be stamped onto plots, etc.
# rad.description # optional | Longer description of this file. This can be read by people trying to figure out where this file came from.
# rad.experiment_date # optional | Date of the experiment (or synthetic particle tracing), in the format "YYYY-MM-DD".
# rad.file_date # optional | Date the (future) file will be created, in the format "YYYY-MM-DD" | You don't need to set this, it will be set automatically
# rad.raw_data_filename # optional | Filename of the raw data file (e.g. CSV from MIT) from which this derivative file was created, if applicable.

##  Asterixed footnotes referenced above:
#
#  * The convention of this format is that the image lies in the z=0 plane of the radiograph coordinate system, and that the z-axis will point towards the particle source. The image may be stored already cropped and rotated by any angle within the x-y radiograph coordinate system, which is why X and Y are specified as arrays rather than vectors.
#
#  ** For best compatibility, consider using the PlasmaPy particle symbol conventions. https://docs.plasmapy.org/en/stable/api/plasmapy.particles.particle_symbol.html
#     For example, protons can be specified as just “p+”, and electrons by "e-". Any arbitrary isotope of Hydrogen can be specified “ H-I q+” where I is the mass number and q is the charge.
#
