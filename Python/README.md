# pradtools (Particle Radiography Tools) - Python Package

**pradtools** is a set of cross-platform tools related to particle radiography. It especially leans on reading and writing from a set of common HDF5 formats for data at various stages along the real/synthetic particle radiography pipeline.

This  code was written by Scott Feister for broader use by the High Energy Density Physics Community.

## Setup

### Dependencies
This module requires **Python 3.7+**. Installation requires **git**.

**OS X users:** Prior to installing dependencies, ensure an adequate Python installation by following [this guide](https://matplotlib.org/faq/installing_faq.html#osx-notes). The Python that ships with OS X may not work well with some required dependencies.

* [`numpy`](http://www.numpy.org/)
* [`scipy`](https://www.scipy.org/)
* [`matplotlib`](https://matplotlib.org/)
* [`h5py`](https://www.h5py.org/)

The dependencies may be installed according to the directions on 
their webpages, or with any Python
package manager that supports them. For example, one could use `pip` to install
them as
 ```bash
pip install numpy scipy matplotlib h5py
```

**NOTE**: If you are on a cluster where you do not have write permissions to the python installation directory, you may need to add "--user" to your pip and setup calls here and below. E.g.
```bash
pip install --user numpy scipy matplotlib h5py
```

As an alternate to pip, one could also use [Anaconda Python](https://anaconda.org/anaconda/python) to
install the dependencies
```bash
conda install numpy scipy matplotlib h5py
```

### Installation
After installing the required packages, we may install **pradtools**.

One way to install **pradtools** is via
```bash
pip install "git+https://github.com/phyzicist/pradtools.git#egg=pkg&subdirectory=Python"
```

To update **pradtools** at a later date
```bash
pip install --upgrade "git+https://github.com/phyzicist/pradtools.git#egg=pkg&subdirectory=Python"
```

An alternative way to install **pradtools** is via
```bash
git clone https://github.com/phyzicist/pradtools.git
cd pradtools/Python
python setup.py install
```

## Usage
You will need to read through the source code for descriptions of the functions of this package. There is unfortunately no formal documentation.

### General usage
```python
import pradtools as pr
```

## Uninstalling

To uninstall **pradtools**
```shell
pip uninstall pradtools
```