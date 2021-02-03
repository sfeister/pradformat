#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
radiograph.py: Read and write the HDF5 pradtools "Radiograph" file structure

Created by Scott Feister on Tue Feb  2 20:33:42 2021
"""

import h5py

class species(object):
    """
    Object for storing data about a single particle species.
    """
    def __init__(self, spec_name="particle"):
        # Attributes.
        self.spec_name = spec_name # Shortname for the particle, e.g. "proton"
        self.spec_mass = None # Species mass per particle
        self.spec_charge = None # Species charge per particle

    def write(self, f):
        f.attr["spec_name"] = spec_name
        f.attr["spec_mass"] = spec_name
        f.attr["spec_charge"] = spec_name

class sensitivity(object):
    """
    Object for storing data about image signal response to incident particles.
    """
    def __init__(self, energy_units="MeV"):
        self.species = None # Should be a single species object
        self.energies = None # Array of energies at which sensitivity is quantified
        self.energy_units = energy_units
        self.sensitivity = None # Array, same size of energies, of sensitivities
        self.sensitivity_units = "image signal per incident particle, at this energy"

    def write(self, f):
        if self.species and self.species.spec_name:
            grp_name = self.species.spec_name
        else:
            grp_name = "default"
            
        sens = f.create_group(grp_name)
        
        if self.species:
            self.species.write(sens)
        if self.energies:
            sens.create_dataset("energies", data=self.energies)
        if self.energy_units:
            sens.attr["energy_units"] = self.energy_units        
        if self.sensitivity:
            sens.create_dataset("sensitivity", data=self.sensitivity)
        if self.sensitivity_units:
            sens.attr["sensitivity_units"] = self.sensitivity_units           

class radiograph(object):
    """
    Object for storing data and attributes of a single particle-radiograph.
    """
    def __init__(self):
        # Attributes.
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
    
    def write(self, f, grp_name="Layer1"):
        """ Write the radiograph within an open HDF5 file object or filename string f"""
        if isinstance(f, str): # if f is not an open file handle
            filename = f
            f = h5py.File(filename, "w-") # Fail if file already exists!
        else:
            filename = None
        
        rad = f.create_group(grp_name)
        rad.attr["type"] = "radiograph"
        rad.attr["pradtools_version"] = "0.0.0" # TODO: Pull this stamp dynamically
        rad.attr["pradtools_language"] = "Python"
        if self.image:
            rad.create_dataset("image", data=self.image)
            rad.attr["image_description"] = "Radiograph image for which all other attributes noted here apply."
        if self.image_units:
            rad.attr["image_units"] = self.image_units
            rad.attr["image_units_description"] = "Units for pixel values. Default is 'image signal'"
        if self.xmin:
            rad.attr["xmin"] = self.xmin
            rad.attr["xmin_description"] = "Image horizontal axis minimum x-coordinate, for the pixel edge, in the radiograph plane."
        if self.xmax:
            rad.attr["xmax"] = self.xmax
            rad.attr["xmax_description"] = "Image horizontal axis maximum x-coordinate, for the pixel edge, in the radiograph plane."
        if self.dx:
            rad.attr["dx"] = self.dx
            rad.attr["dx_description"] = "Horizontal pixel size dx for the radiograph image."
        if self.ymin:
            rad.attr["ymin"] = self.ymin
            rad.attr["ymin_description"] = "Image vertical axis minimum y-coordinate, for the pixel edge, in the radiograph plane."
        if self.ymax:
            rad.attr["ymax"] = self.ymax
            rad.attr["ymax_description"] = "Image vertical axis maximum y-coordinate, for the pixel edge, in the radiograph plane."
        if self.dy:
            rad.attr["dy"] = self.dy
            rad.attr["dy_description"] = "Vertical pixel size dy for the radiograph image."
        if self.units:
            rad.attr["units"] = self.units
            rad.attr["units_description"] = "Units system used for all attribute values of this radiograph."
        if self.source_distance:
            rad.attr["source_distance"] = self.source_distance
            rad.attr["source_distance_description"] = "Approximate distance from the particle source to the plane of the radiograph."
        if self.ROI_distance:
            rad.attr["ROI_distance"] = self.ROI_distance
            rad.attr["ROI_distance_description"] = "Approximate distance from the center of the imaged region of interest to the plane of the radiograph."
        if self.sensitivities:
            sens_grp = rad.create_group("sensitivities")
            for s in sensitivities:
                s.write(sens_grp)

        if filename: # Close the file if it wasn't input as an open file handle
            f.close()
            
if __name__ == "__main__":
    pass
