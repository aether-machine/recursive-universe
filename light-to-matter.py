import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants (tuned for black hole-like conditions)
alpha = 0.01  # Time-energy conversion factor (feedback coefficient)
beta = 0.005  # Matter decay rate (feedback loss rate)
tau = 0.02    # Light-to-matter conversion rate (matter creation)

# Define the system of equations: energy and matter dynamics
def system(t, y):
    E, M = y
    dE_dt = -tau * E  # Light converting to matter
    dM_dt = tau * E - beta * M  # Matter formation and decay (recursive)
    return [dE_dt, dM_dt]

# Initial conditions (at time t=0)
E0 = 1.0  # Initial energy (normalized)
M0 = 0.0  # Initial matter (start with no matter)
t_span = (0, 100)  # Time range for the simulation (in arbitrary units)
t_eval = np.linspace(*t_span, 500)  # Time points to evaluate

# Solve the system using the SciPy solver
sol = solve_ivp(system, t_span, [E0, M0], t_eval=t_eval)

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(sol.t, sol.y[0], label="Energy (E)", color="blue")
plt.plot(sol.t, sol.y[1], label="Matter (M)", color="red")
plt.xlabel("Time")
plt.ylabel("Proportions")
plt.title("Energy and Matter Recursive Dynamics")
plt.legend()
plt.grid(True)
plt.show()

