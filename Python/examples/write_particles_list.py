# write_particles_list.py: A template for writing your own Particles List

import os
import numpy as np
from scipy.stats import uniform, norm
import pradformat as prf

## Construct Particles List object
plist = prf.ParticlesList()

## Create some test 1D arrays (R, theta, and phi in position and momentum space)
N = 1000 # Number of particles to generate
source_radius = 2.0e-6 # 2 micron for source radius (normal distribution standard deviation length)
R = norm.rvs(size=N, scale=source_radius) # Radius is in a normal distribution of standard deviation source_radius
theta = uniform.rvs(size=N, scale=np.pi) # theta is uniform from 0 to pi
phi = uniform.rvs(size=N, loc=-np.pi, scale=2*np.pi) # phi is uniform from -pi to pi

# Define particle momenta
pmag = 5.403e-21 # Magnitude of momentum for 100 MeV electron, in kg * m/s (I used Wolfram Alpha: https://www.wolframalpha.com/input/?i=100+MeV+electron+to+momentum)
half_angle = np.deg2rad(3.0) # Allow for a 3-degree half-angle conical divergence of particle emission
ptheta = uniform.rvs(size=N, scale=half_angle)
pphi = uniform.rvs(size=N, loc=-half_angle, scale=2*half_angle)

## Set datasets and attributes of the Particles List object
plist.x = R * np.sin(theta) * np.cos(phi) # required | x position of particle | meters
plist.y = R * np.sin(theta) * np.sin(phi) # required | y position of particle | meters
plist.z = R * np.cos(theta) # required | z position of particle | meters

plist.px = pmag * np.sin(ptheta) * np.cos(pphi) # required | momentum of particle, x-component | kg * m/s
plist.py = pmag * np.sin(ptheta) * np.sin(pphi) # required | momentum of particle, y-component | kg * m/s
plist.pz = pmag * np.cos(ptheta) # required | momentum of particle, z-component | kg * m/s

plist.charge = -1.602e-19 * np.ones(N) # required | particle charge | Coulombs
plist.mass = 9.109e-31 * np.ones(N) # required | particle mass | kg
plist.energy = 100.0e6 * np.ones(N) # optional | particle energy (can be derived from px,py,pz,mass) | eV
plist.spec_name = ["e-"]*N # optional | particle species name (e.g. "p+")*
plist.weight = 100 * np.ones(N) # optional | for pseudoparticles, number of real particles represented | real particles / pseudoparticle
plist.id = np.arange(N) # optional | unique particle ID (e.g. 4073)

# print(plist.object_type) # already-set | Specification of the HDF5 object type | "particles" (always this value)
# print(plist.particles_type) # already-set | Specification of the particles sub-type | "list" (always this value)
# print(plist.pradformat_version) # already-set | HDF5 pradformat file format version followed | e.g. "0.1.0"

plist.shuffled = 0 # optional | Whether the order of particles in this list has been randomly shuffled. 0 for false, 1 for true.
plist.label = "Ebeam_100MeV" # optional | Short, identifying label for this file (with no spaces or crazy characters). This can be stamped onto plots, etc.
plist.description = "100 MeV electron beam into a 3-degree half-angle cone, from a source with 2-micron standard-deviation length scale." # optional | Longer description of this file. This can be read by people trying to figure out where this file came from.
# print(plist.file_date) # automatically-set | Date the (future) file will be created, in the format "YYYY-MM-DD" | You don't need to set this, it will be set automatically
# plist.raw_data_filename = "/fs/EPOCH/mysim/sdf0013" # optional | Filename of the raw data file (e.g. simulation output) from which this derivative file was created, if applicable.

## Pretty print your newly-minted Particles List object
print(plist)

## Save to file
if not os.path.isdir("outs"):
    os.mkdir("outs")
h5filename = os.path.join('outs', 'myparticles.h5')
plist.save(h5filename)

##  Asterixed footnotes referenced above:
#
#  * For best compatibility, consider using the PlasmaPy particle symbol conventions. https://docs.plasmapy.org/en/stable/api/plasmapy.particles.particle_symbol.html
#     For example, protons can be specified as just "p+", and electrons by "e-". Any arbitrary isotope of Hydrogen can be specified "H-I q+"? where I is the mass number and q is the charge.
#