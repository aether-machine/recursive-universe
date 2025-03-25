# Constants for a "black hole-like" region
gamma = 0.01  # Recirculation feedback strength
delta = 0.005  # Matter energy conversion efficiency

# Modified system for black hole-like conditions
def black_hole_system(t, y):
    E, M = y
    # Energy is recycled into matter, and matter decays back into energy
    dE_dt = -gamma * E  # Light gets trapped and converted to matter
    dM_dt = gamma * E - delta * M  # Matter decays back into energy
    return [dE_dt, dM_dt]

# Initial conditions for a black hole-like region
E0_bh = 1.0  # Initial energy (normalized)
M0_bh = 0.0  # No matter at the start
t_span_bh = (0, 100)  # Time range for simulation
t_eval_bh = np.linspace(*t_span_bh, 500)  # Time points

# Solve the system for the black hole-like region
sol_bh = solve_ivp(black_hole_system, t_span_bh, [E0_bh, M0_bh], t_eval=t_eval_bh)

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(sol_bh.t, sol_bh.y[0], label="Energy (E)", color="blue")
plt.plot(sol_bh.t, sol_bh.y[1], label="Matter (M)", color="red")
plt.xlabel("Time")
plt.ylabel("Proportions")
plt.title("Energy and Matter Feedback in a Black Hole-like Region")
plt.legend()
plt.grid(True)
plt.show()
