# Installation

## Creating the environment (non-reproducible)

This creates the environment from scratch, using the most updated packages:

```
$ conda create -n py36_optimize python=3.6 cython line_profiler numba numexpr numpy ipykernel pandas nbconvert tqdm pyyaml joblib
$ conda activate py36_optimize
$ python -m ipykernel install --name py36_optimize --display-name "Python 3.6 (py36_optimize)"
$ pip install randomgen  # no conda package yet
```

> **NOTE**: This is will create an environment with the most updated packages available at installation time. Not for reproducibility.

## Cloning the environment (reproducible)

```
conda
```
