import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lpmv  # Associated Legendre polynomials

# Constants
tau = 1e10  # Characteristic time constant (years)
Lambda_0 = 1e-52  # Initial cosmological constant
rho_0 = 1e-9  # Initial energy density
G = 6.67430e-11  # Gravitational constant
c = 3e8  # Speed of light
k_B = 1.380649e-23  # Boltzmann constant
ell = 2  # Orbital quantum number (fixed for simplicity)

# Time array (10 billion years simulation)
time_years = np.linspace(1, 10e10, 1000)

# Dynamic energy density decay
def dynamic_energy_density(t, rho_0, tau):
    return rho_0 * np.exp(-t / tau)

# Dynamic cosmological constant decay
def dynamic_cosmological_constant(t, Lambda_0, tau):
    return Lambda_0 * np.exp(-t / tau)

# Real-time computation of azimuthal quantum number (feedback loop)
def compute_azimuthal_m(t, max_m=5):
    # Normalize time between -1 and 1 for Legendre functions
    x = np.clip(2 * (t / np.max(time_years)) - 1, -1, 1)
    # Compute the associated Legendre function P_l^m(x) for a range of m values
    m_values = np.arange(0, max_m + 1)
    legendre_vals = np.array([lpmv(m, ell, x) for m in m_values])
    # Normalize to prevent runaway values
    return np.abs(legendre_vals).sum(axis=0) / (max_m + 1)

# Modulated entropy evolution using azimuthal quantum influence
def entropy_change(t, t_max, m_feedback):
    log_argument = 1 + m_feedback * (1 - t / t_max)
    log_argument = np.maximum(log_argument, 1e-10)  # Prevents negative or zero values
    return k_B * np.log(log_argument)

# Compute time-dependent variables
rho_t = dynamic_energy_density(time_years, rho_0, tau)
Lambda_t = dynamic_cosmological_constant(time_years, Lambda_0, tau)
m_t = compute_azimuthal_m(time_years)
entropy_t = entropy_change(time_years, 1e10, m_t)

# Plot results
fig, ax1 = plt.subplots()

ax1.set_xlabel('Time (years)')
ax1.set_ylabel('Energy Density (rho)', color='tab:blue')
ax1.plot(time_years, rho_t, color='tab:blue', label='Energy Density')

ax2 = ax1.twinx()
ax2.set_ylabel('Entropy & Cosmological Constant', color='tab:red')
ax2.plot(time_years, Lambda_t, color='tab:red', label='Cosmological Constant')
ax2.plot(time_years, entropy_t, color='tab:orange', label='Entropy Change')

plt.title('Azimuthal Quantum Feedback in Black Hole Time Dynamics')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig("quantum_feedback_blackhole.png")
plt.show()

