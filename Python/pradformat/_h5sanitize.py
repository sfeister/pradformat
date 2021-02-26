#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_h5sanitize.py

Created by Scott Feister on Thu Feb  4 14:33:07 2021
"""

def _h5sanitize(attr_value):
    """Decodes bytestring HDF5 attribute values using UTF-8 format; passes unchanged attribute values of any other type
    This helps us support MATLAB-generated HDF5 files, which may save character vectors as fixed length HDF5 strings"""
    if isinstance(attr_value, bytes):
        return attr_value.decode('utf-8')
    else:
        return attr_value

if __name__ == "__main__":
    pass
