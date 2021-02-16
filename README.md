# pradformat (Proton Radiography File Format Tools)

**pradformat** is a set of cross-platform tools related to particle radiography. It especially leans on reading and writing from a set of common HDF5 file formats (with common contents) for data at various stages along the real/synthetic particle radiography pipeline.

The Python code, MATLAB code, and shared HDF5 file structures of this package were written by Scott Feister of California State University Channel Islands for broader use by the High Energy Density Physics Community.

For simplicity, the MATLAB and Python readers in this package read the entire objects into RAM (as far as I know). This will not work for large HDF5 files, and perhaps could be improved with further future readers. If you run into memory issues, I suggest reading the same files using the native HDF5 readers for MATLAB and Python (and thus avoid loading the entire datasets into RAM).

Compression of the datasets within the HDF5 files is performed in the Python writers, but not in the MATLAB writers. Compression can dramatically reduce file size. Both Python and MATLAB readers can read compressed or uncompressed datasets.