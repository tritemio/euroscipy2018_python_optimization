# To build the cython extensions use:
# python setup.py build_ext --inplace
#

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        'ou_process',
        ['ou_process.pyx'],
        include_dirs=[np.get_include()],
        # Uncomment the following line for profiling
        define_macros=[('CYTHON_TRACE', '1')],
    )
]

setup(
    name="Cyton functions to simulate an OU process",
    ext_modules=cythonize(
        extensions,
        # Uncomment the following line for profiling
        compiler_directives={'linetrace': True, 'binding': True},
    ),
)
