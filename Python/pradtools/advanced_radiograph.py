#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
advanced_radiograph.py: Read and write the HDF5 pradtools "Advanced Radiograph" file structure

WORK IN PROGRESS -- AKA DOES NOT WORK CURRENTLY OR CONFORM TO THE OFFICIAL SPEC

Created by Scott Feister on Tue Feb  2 20:33:42 2021
"""

import h5py

class Species(object):
    """
    Object for storing data about a single particle species.
    """
    def __init__(self, name=None, mass=None, charge=None):
        # Attributes.
        self.name = name # Shortname for the particle, e.g. "proton"
        self.mass = mass # Species mass per particle
        self.charge = charge # Species charge per particle
        self.units = "SI"

    def write(self, f, grp_name="species1"):
        spec = f.create_group(grp_name) # TODO: Iterate on species1, species2, species3, ...
        
        spec.attrs["units"] = self.units
        if not isinstance(self.name, type(None)):
            spec.attrs["name"] = self.name
        if not isinstance(self.mass, type(None)):
            spec.attrs["mass"] = self.mass
        if not isinstance(self.charge, type(None)):
            spec.attrs["charge"] = self.charge

class Sensitivity(object):
    """
    Object for storing data about image signal response to incident particles.
    """
    def __init__(self, species=None, energy=None, sensitivity=None):
        self.species = species # Should be a single species object
        self.energy = energy # Array of energies at which sensitivity is quantified
        self.energy_units = "eV"
        self.sensitivity = sensitivity # Array, same size of energies, of sensitivities
        self.sensitivity_units = "image signal per incident particle, at this energy"

    def write(self, f, grp_name="sensitivity1"):
        sens = f.create_group(grp_name) # TODO: Iterate on sensitivity1, sensitivity2, sensitivity3, ...
        
        if not isinstance(self.species, type(None)):
            self.species.write(sens)
        if not isinstance(self.energy, type(None)):
            sens.create_dataset("energy", data=self.energy)
        if not isinstance(self.energy_units, type(None)):
            sens.attrs["energy_units"] = self.energy_units        
        if not isinstance(self.sensitivity, type(None)):
            sens.create_dataset("sensitivity", data=self.sensitivity)
        if not isinstance(self.sensitivity_units, type(None)):
            sens.attrs["sensitivity_units"] = self.sensitivity_units           

class AdvancedRadiograph(object):
    """
    Object for storing data and attributes of a single radiograph created by multiple incident species and energies.
    """
    def __init__(self):
        # Attributes.
        self.layer_name = None
        self.image = None # 2D flux image
        self.image_units = "image signal"
        self.xmin = None
        self.xmax = None
        self.dx = None
        self.ymin = None
        self.ymax = None
        self.dy = None
        self.units = "SI" # assume SI units like meter, etc. for all quantities
        self.source_distance = None # Distance from the radiograph to the particle source
        self.ROI_distance = None # Distance from the radiograph to the imaged region of interest
        self.sensitivities = None # List of sensitivity objects
    
    def write(self, f, grp_name="layer1"):
        """ Write the radiograph within an open HDF5 file object or filename string f"""
        if isinstance(f, str): # if f is not an open file handle
            filename = f
            f = h5py.File(filename, "w") # Overwrites if file already exists!
        else:
            filename = None
        
        rad = f.create_group(grp_name) # TODO: Iterate on layer1, layer2, layer3, ...
        rad.attrs["type"] = "radiograph"
        rad.attrs["pradtools_version"] = "0.0.0" # TODO: Pull this stamp dynamically
        rad.attrs["pradtools_language"] = "Python"
        if not isinstance(self.layer_name, type(None)):
            rad.attrs["layer_name"] = self.layer_name
        if not isinstance(self.image, type(None)):
            rad.create_dataset("image", data=self.image)
            rad.attrs["image_description"] = "Radiograph image for which all other attributes noted here apply."
        if not isinstance(self.image_units, type(None)):
            rad.attrs["image_units"] = self.image_units
            rad.attrs["image_units_description"] = "Units for pixel values. Default is 'image signal'"
        if not isinstance(self.xmin, type(None)):
            rad.attrs["xmin"] = self.xmin
            rad.attrs["xmin_description"] = "Image horizontal axis minimum x-coordinate, for the pixel edge, in the radiograph plane."
        if not isinstance(self.xmax, type(None)):
            rad.attrs["xmax"] = self.xmax
            rad.attrs["xmax_description"] = "Image horizontal axis maximum x-coordinate, for the pixel edge, in the radiograph plane."
        if not isinstance(self.dx, type(None)):
            rad.attrs["dx"] = self.dx
            rad.attrs["dx_description"] = "Horizontal pixel size dx for the radiograph image."
        if not isinstance(self.ymin, type(None)):
            rad.attrs["ymin"] = self.ymin
            rad.attrs["ymin_description"] = "Image vertical axis minimum y-coordinate, for the pixel edge, in the radiograph plane."
        if not isinstance(self.ymax, type(None)):
            rad.attrs["ymax"] = self.ymax
            rad.attrs["ymax_description"] = "Image vertical axis maximum y-coordinate, for the pixel edge, in the radiograph plane."
        if not isinstance(self.dy, type(None)):
            rad.attrs["dy"] = self.dy
            rad.attrs["dy_description"] = "Vertical pixel size dy for the radiograph image."
        if not isinstance(self.units, type(None)):
            rad.attrs["units"] = self.units
            rad.attrs["units_description"] = "Units system used for all attribute values of this radiograph."
        if not isinstance(self.source_distance, type(None)):
            rad.attrs["source_distance"] = self.source_distance
            rad.attrs["source_distance_description"] = "Approximate distance from the particle source to the plane of the radiograph."
        if not isinstance(self.ROI_distance, type(None)):
            rad.attrs["ROI_distance"] = self.ROI_distance
            rad.attrs["ROI_distance_description"] = "Approximate distance from the center of the imaged region of interest to the plane of the radiograph."
        if not isinstance(self.sensitivities, type(None)):
            for s in self.sensitivities:
                s.write(rad)

        if filename: # Close the file if it wasn't input as an open file handle
            f.close()
            
if __name__ == "__main__":
    pass
