import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
alpha = 0.01  # Time-energy conversion factor
beta = 0.005  # Matter decay rate
tau = 0.02    # Light-to-matter conversion rate

# Differential equations: dE/dT and dM/dT
def system(t, y):
    E, M = y
    dE_dt = -tau * E  # Light converting to matter
    dM_dt = tau * E - beta * M  # Matter formation and decay
    return [dE_dt, dM_dt]

# Initial Conditions
E0 = 1.0  # Initial energy (normalized)
M0 = 0.0  # Initial matter
t_span = (0, 100)  # Time range
t_eval = np.linspace(*t_span, 500)  # Evaluation points

# Solve the system
sol = solve_ivp(system, t_span, [E0, M0], t_eval=t_eval)

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(sol.t, sol.y[0], label="Energy (E)", color="blue")
plt.plot(sol.t, sol.y[1], label="Matter (M)", color="red")
plt.xlabel("Time")
plt.ylabel("Proportions")
plt.title("Light-to-Matter Conversion in the Recursive Universe Model")
plt.legend()
plt.grid()
plt.show()
