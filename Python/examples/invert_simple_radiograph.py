# invert_simple_radiograph.py: Example of how we can transfer properties from a SimpleRadiograph onto a SimpleInversion

import os
import numpy as np
import pradformat as prf

## Load object from pradformat file
h5filename = os.path.join('outs', 'myradiograph.h5')
rad = prf.prad_load(h5filename)

## Examine your newly loaded object
print(rad)

## Utilize object's datasets and attributes in your own scripts
assert isinstance(rad, prf.SimpleRadiograph)

# Create a SimpleInversion object, copying over many matching properties from the SimpleRadiograph as a template
siv = prf.SimpleInversion(template=rad)
siv.label = "Inverted_" + siv.label
siv.description = "Inverted: " + siv.description
print(siv)