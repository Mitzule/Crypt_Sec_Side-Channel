import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

# Simulate power consumption based on Hamming weight
def hamming_weight(byte_array):
    return sum(bin(byte).count('1') for byte in byte_array)

def simulate_power(plaintext, key):
    power = hamming_weight(key) * 0.1 + np.random.normal(0, 0.02)
    return power

# Example data
plaintexts = [b"Test data %d" % i for i in range(10)]
keys = [
    b"mihai12345678901",  # Key 1: Incorrect key (simulating attacker guess)
    b"gabriela987654321",  # Key 2: Incorrect key (another attacker guess)
    b"remus12345678901",  # Correct Key: Used in encryption
    b"random_fake_key22"  # Key 3: Incorrect key
]


# Generate power data
power_data = {key: [simulate_power(pt, key) for pt in plaintexts] for key in keys}

# Plot
plt.figure(figsize=(10, 6))
for key, powers in power_data.items():
    plt.plot(powers, label=f"Key: {key}")
plt.title("Power Consumption for Different Keys")
plt.xlabel("Operation")
plt.ylabel("Power (arbitrary units)")
plt.legend()
plt.grid(True)
plt.show()

# Correlation
for key, powers in power_data.items():
    correlation, _ = pearsonr(range(len(powers)), powers)
    print(f"Key: {key}, Correlation with operations: {correlation:.2f}")
