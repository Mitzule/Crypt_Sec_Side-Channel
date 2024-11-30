import matplotlib.pyplot as plt
import numpy as np
import random

# Simulate timing data
def simulate_timing(key):
    base_time = 0.05 if key == "correct_key" else 0.045
    return base_time + random.gauss(0, 0.005)

keys = [
    b"mihai12345678901",  # Key 1: Incorrect key (simulating attacker guess)
    b"gabriela987654321",  # Key 2: Incorrect key (another attacker guess)
    b"remus12345678901",  # Correct Key: Used in encryption
    b"random_fake_key22"  # Key 3: Incorrect key
]

timing_data = {key: [simulate_timing(key) for _ in range(100)] for key in keys}

# Plot histogram
plt.figure(figsize=(10, 6))
for key, timings in timing_data.items():
    plt.hist(timings, bins=20, alpha=0.7, label=f"Key: {key}")
plt.title("Timing Distribution for Keys")
plt.xlabel("Time (s)")
plt.ylabel("Frequency")
plt.legend()
plt.show()
