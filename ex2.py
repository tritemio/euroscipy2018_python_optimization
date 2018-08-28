def OU_update2(*, x_prev, δt, τ, σ, N_norm):
    relax = math.exp(-δt / τ)
    diffuse = σ * math.sqrt(1 - relax**2)
    return x_prev * relax + diffuse * N_norm

def OU_process1(num_steps, *, δt=0.1, x0=0, τ=1, σ=2, OU_update=OU_update2):
    N_norm = np.random.randn(num_steps)
    x = [x0]
    for i in range(num_steps):
        x.append(OU_update(x_prev=x[-1], δt=δt, σ=σ, τ=τ, N_norm=N_norm[i])) 
    return x