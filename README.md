## Tutorial "A tour of Python profiling and optimization"

*Tue August 28, 14:00,  A. Ingargiola*, **EuroScipy 2018**

To run on the cloud (no installation) use [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/tritemio/euroscipy2018_python_optimization/master?filepath=Optimizing%20Python%20code.ipynb)

> **WARNING** During the EuroScipy 2018 Tutorial a local installation is preferable.


# Requirements

You will need: 

```
python=3.6 cython line_profiler numba numexpr numpy ipykernel pandas joblib matplotlib seaborn
```

available through PyPI or conda/conda-forge. You will also need:

```
randomgen
```

currently only available from PyPI.


# Installation

## Cloning (reproducible)

Linux and macOS users can use the following command:

```
conda env create -f environment.yml
```

to create the `py36_optimize` environment for this tutorial. The `yml` file is:

- `environment_macos.yml` for macOS
- `binder/environment.yml` for Linux

## From scratch (non-reproducible)

This creates the environment from scratch, using the most updated packages (non-reproducible):

```
$ conda create -n py36_optimize python=3.6 cython line_profiler numba numexpr numpy ipykernel pandas joblib matplotlib seaborn
$ conda activate py36_optimize
$ pip install randomgen  # no conda package yet
```

## Installing the IPython kernel

After installing the environment you need make it available to Jupyter:

```
$ conda activate py36_optimize
$ python -m ipykernel install --name py36_optimize --display-name "Python 3.6 (py36_optimize)"
```
