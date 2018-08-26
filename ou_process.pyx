import numpy as np
cimport numpy as np
from libc.math cimport exp, sqrt

def OU_process_cy(int num_steps, *, double[:] N_norm, dt=0.1,
                x0=0, tau=1, sigma=2):
    cdef Py_ssize_t i
    cdef double relax, diffuse
    cdef double[:] x = np.empty(num_steps + 1)
    relax = exp(-dt / tau)
    diffuse = sigma * sqrt(1 - relax**2)

    x[0] = x0
    for i in range(num_steps):
        x[i+1] = x[i] * relax + diffuse * N_norm[i]
    return x
