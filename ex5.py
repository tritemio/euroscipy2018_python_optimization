@numba.jit
def OU_process_nb(num_steps, *, N_norm, δt=0.1, x0=0., τ=1., σ=2.):
    relax = math.exp(-δt / τ)
    diffuse = σ * math.sqrt(1 - relax**2)

    x = np.empty(num_steps + 1)
    x[0] = x0
    for i in range(num_steps):
        x[i+1] = x[i] * relax + diffuse * N_norm[i]
    return x