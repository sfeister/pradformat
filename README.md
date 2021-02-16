# pradformat (Proton Radiography File Format Tools)

**pradformat** is a set of cross-platform tools related to particle radiography. It especially leans on reading and writing from a set of common HDF5 file formats (with common contents) for data at various stages along the real/synthetic particle radiography pipeline.

The Python code, MATLAB code, and shared HDF5 file structures of this package were written by Scott Feister of California State University Channel Islands for broader use by the High Energy Density Physics Community.

## File Formats (see specifications document)
The file formats defined by the pradformat specification are defined in the **"FormatSpec.xlsx"** document, which is in the main folder of this repository. Please download this and examine it now. Keep the document handy as a reference while using the readers/writers.

## Installation
To install the MATLAB readers/writers, navigate into the Releases section -- you will download and install the toolbox. (Not yet created! Don't try this yet.)

To install the Python readers/writers, navigate into the "Python" directory of this repository and follow the setup instructions in the README.

## Usage
Please look through the examples in this repository, under "Python/examples/" and "MATLAB/examples/".

It's a bit tricky to add your sensitivities to the Advanced Radiograph, so please see example4 especially before trying that one out.

## Limitations
For simplicity, the MATLAB and Python readers in this package read the entire objects into memory (as far as I know). This will not work for large HDF5 files, and perhaps could be improved with further future readers. If you run into memory issues, I suggest reading the same files using the native HDF5 readers for MATLAB and Python (and thus avoid loading the entire datasets into RAM).

Compression of the datasets within the HDF5 files is performed in the Python writers, but not in the MATLAB writers. Compression can dramatically reduce file size. Both Python and MATLAB readers can read compressed or uncompressed datasets.

Currently, MATLAB is entirely missing readers/writers for Particles List and Advanced Radiograph.