import numpy as np
import matplotlib.pyplot as plt

dtau = 0.001  # Set dimensionless time increments
dx = 0.05     # Set dimensionless length increments
Tmax = 0.95   # Set maximum dimensionless temperature
M = 21        # Counter for length discretization

# Calculate parameters
dx_x = 1.0 / (M - 1)
ratio = dtau / (dx**2)
const = 1.0 - 2.0 * ratio

# Set up arrays for solution
T = np.zeros(M)
T[0] = 1.0
T[-1] = 1.0

# Set up array for storing solutions at different time steps
T_sol = np.zeros((400, M))
T_sol[:, 0] = 1.0
T_sol[:, -1] = 1.0

# Set counters to zero
i = 0
tau = 0.0

# While loop to iterate until mid-point temperature reaches Tmax
while T[10] < Tmax:
    i += 1
    tau += dtau

    # Calculate new temperatures
    Tnew = np.zeros(M)
    for j in range(1, M - 1):
        Tnew[j] = ratio * (T[j - 1] + T[j + 1]) + const * T[j]

    # Update temperatures
    T[:] = Tnew[:]
    T_sol[i, :] = T[:]

print("Tau and T_final =", tau, T_sol[i])

# Set up array for spatial values of x to plot
x = np.linspace(0, 1, M)

# Plot the solutions
plt.plot(x, T_sol[50, :], label='Tau = 0.5')
plt.plot(x, T_sol[100, :], label='Tau = 0.1')
plt.plot(x, T_sol[150, :], label='Tau = 0.15')
plt.plot(x, T_sol[250, :], label='Tau = 0.25')
plt.plot(x, T_sol[i, :], label='Tau = final time')
plt.title('Normalized Slab Temperatures')
plt.xlabel('Normalized Length')
plt.ylabel('Normalized Temperature')
plt.legend()
plt.grid()
plt.show()

