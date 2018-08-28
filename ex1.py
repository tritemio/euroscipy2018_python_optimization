import math

def OU_update1(*, x_prev, δt, τ, σ):
    N_norm = np.random.randn()
    relax = math.exp(-δt / τ)
    diffuse = σ * math.sqrt(1 - relax**2)
    return x_prev * relax + diffuse * N_norm