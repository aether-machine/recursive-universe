import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants (scaled for simplicity)
G = 1  # Gravitational constant (scaled)
c = 1  # Speed of light (scaled)
M = 1  # Black hole mass (scaled)

# Define the feedback function modeling energy recycling
def energy_feedback(t, y):
    curvature = y[0]  # Spacetime curvature near the event horizon
    energy_flow = y[1]  # Energy exchange (infall vs. radiation)
    
    # Curvature evolution: increases with energy infall, but regulated
    d_curvature_dt = G * M / (curvature + 1) - 0.1 * energy_flow  
    
    # Energy recycling: matter in → energy released via Hawking-like process
    d_energy_dt = -0.5 * np.tanh(curvature)  # Simulated radiation feedback
    
    return [d_curvature_dt, d_energy_dt]

# Initial conditions: starting curvature and energy flow
initial_conditions = [2.0, 0.1]  # Arbitrary units

time_span = (0, 50)  # Simulate for 50 time units
time_eval = np.linspace(0, 50, 500)  # Time steps

# Solve the system
solution = solve_ivp(energy_feedback, time_span, initial_conditions, t_eval=time_eval)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(solution.t, solution.y[0], label='Curvature', color='red')
plt.plot(solution.t, solution.y[1], label='Energy Recycling', color='blue')
plt.xlabel('Time')
plt.ylabel('Magnitude')
plt.legend()
plt.title('Black Holes as Energy Recyclers')
plt.show()
