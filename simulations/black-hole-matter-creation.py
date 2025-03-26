import numpy as np
import matplotlib.pyplot as plt

# Constants (normalized for simplicity)
G = 1       # Gravitational constant (normalized)
c = 1       # Speed of light (normalized)
hbar = 1    # Reduced Planck's constant (normalized)

# Black hole properties (initial values)
M_initial = 10  # Initial mass of the black hole (arbitrary units)
r_s_initial = 2 * G * M_initial / c**2  # Schwarzschild radius

# Time evolution parameters
time_steps = 1000  # Number of simulation steps
dt = 0.01  # Time step size

# Arrays to store results
time = np.linspace(0, time_steps * dt, time_steps)
M_values = np.zeros(time_steps)
r_s_values = np.zeros(time_steps)
energy_radiation = np.zeros(time_steps)

# Initial conditions
M_values[0] = M_initial
r_s_values[0] = r_s_initial

# Hawking radiation function (energy loss over time)
def hawking_radiation(mass):
    return hbar * c**6 / (15360 * np.pi * G**2 * mass**2)  # Energy loss rate

# Simulation loop
for t in range(1, time_steps):
    M_prev = M_values[t - 1]
    dM = -hawking_radiation(M_prev) * dt  # Mass loss due to radiation

    M_new = max(M_prev + dM, 0)  # Ensure mass doesn't become negative
    r_s_new = 2 * G * M_new / c**2  # Recalculate Schwarzschild radius

    M_values[t] = M_new
    r_s_values[t] = r_s_new
    energy_radiation[t] = -dM / dt  # Track radiation output

# Plot results
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].plot(time, M_values, label="Black Hole Mass", color='blue')
ax[0].set_xlabel("Time (arbitrary units)")
ax[0].set_ylabel("Mass (normalized)")
ax[0].set_title("Black Hole Mass Evolution")
ax[0].legend()

ax[1].plot(time, energy_radiation, label="Hawking Radiation", color='red')
ax[1].set_xlabel("Time (arbitrary units)")
ax[1].set_ylabel("Radiation Energy Output (normalized)")
ax[1].set_title("Hawking Radiation Emission Over Time")
ax[1].legend()

plt.tight_layout()
plt.show()
