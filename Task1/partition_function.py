import numpy as np

# Constants
k_B = 1.38e-23  # Boltzmann constant (J/K)
T = 300         # Temperature in Kelvin
epsilon = 1e-20 # Energy level in Joules
mu = 5e-21      # Chemical potential in Joules

# Compute beta
beta = 1 / (k_B * T)

# Compute partition function terms
Z_00 = np.exp(-beta * (0 - 0 * mu))  # State (0,0)
Z_10 = np.exp(-beta * (0 - 1 * mu))  # State (1,0)
Z_01 = np.exp(-beta * (epsilon - 1 * mu))  # State (0,1)
Z_11 = np.exp(-beta * (epsilon - 2 * mu))  # State (1,1)

# Compute grand partition function
Z = Z_00 + Z_10 + Z_01 + Z_11

# Print results
print(f"Grand Partition Function Z: {Z:.5f}")

# Calculate probability of each state
P_00 = Z_00 / Z
P_10 = Z_10 / Z
P_01 = Z_01 / Z
P_11 = Z_11 / Z

print(f"Probability of state (0,0): {P_00:.5f}")
print(f"Probability of state (1,0): {P_10:.5f}")
print(f"Probability of state (0,1): {P_01:.5f}")
print(f"Probability of state (1,1): {P_11:.5f}")

# Calculate average occupation numbers
n1_avg = (0 * P_00) + (1 * P_10) + (0 * P_01) + (1 * P_11)
n2_avg = (0 * P_00) + (0 * P_10) + (1 * P_01) + (1 * P_11)

print(f"Average occupation number ⟨n1⟩: {n1_avg:.5f}")
print(f"Average occupation number ⟨n2⟩: {n2_avg:.5f}")

"""
Printed output;
k1/partition_function.py
Grand Partition Function Z: 5.64475
Probability of state (0,0): 0.17716
Probability of state (1,0): 0.59274
Probability of state (0,1): 0.05295
Probability of state (1,1): 0.17716
Average occupation number ⟨n1⟩: 0.76990

"""
