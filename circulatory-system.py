# Constants for high-feedback recirculation
alpha_feedback = 0.02  # High feedback constant
beta_feedback = 0.01  # Matter-to-energy recirculation

# Modified system with feedback loops
def recirculation_system(t, y):
    E, M = y
    # Feedback loop, energy is trapped and oscillates as matter decays
    dE_dt = -alpha_feedback * E + beta_feedback * M  # Energy feedback
    dM_dt = alpha_feedback * E - beta_feedback * M  # Matter to energy
    return [dE_dt, dM_dt]

# Initial conditions for recirculating system
E0_recirc = 1.0  # Initial energy
M0_recirc = 0.0  # Initial matter
t_span_recirc = (0, 100)  # Simulation time
t_eval_recirc = np.linspace(*t_span_recirc, 500)  # Time evaluation points

# Solve the system with recirculating feedback
sol_recirc = solve_ivp(recirculation_system, t_span_recirc, [E0_recirc, M0_recirc], t_eval=t_eval_recirc)

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(sol_recirc.t, sol_recirc.y[0], label="Energy (E)", color="blue")
plt.plot(sol_recirc.t, sol_recirc.y[1], label="Matter (M)", color="red")
plt.xlabel("Time")
plt.ylabel("Proportions")
plt.title("Recirculating Energy and Matter Feedback Loop")
plt.legend()
plt.grid(True)
plt.show()
