import matplotlib.pyplot as plt
import numpy as np

# Simulate EM signals
def simulate_em_signal(length, key):
    frequency = 5 if key == "correct_key" else 10
    noise = np.random.normal(0, 0.5, length)
    return np.sin(np.linspace(0, frequency * 2 * np.pi, length)) + noise

keys = [
    b"mihai12345678901",  # Key 1: Incorrect key (simulating attacker guess)
    b"gabriela987654321",  # Key 2: Incorrect key (another attacker guess)
    b"remus12345678901",  # Correct Key: Used in encryption
    b"random_fake_key22"  # Key 3: Incorrect key
]

em_signals = {key: simulate_em_signal(500, key) for key in keys}

# Plot time-domain signals
plt.figure(figsize=(10, 6))
for key, signal in em_signals.items():
    plt.plot(signal, label=f"Key: {key}")
plt.title("Electromagnetic Signals for Keys")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
