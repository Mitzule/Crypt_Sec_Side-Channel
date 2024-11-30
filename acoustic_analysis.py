import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import spectrogram

# Simulate acoustic data
def simulate_acoustic(key):
    length = 1000
    frequency = 300 if key == "correct_key" else 400
    time = np.linspace(0, 1, length)
    signal = np.sin(2 * np.pi * frequency * time) + np.random.normal(0, 0.5, length)
    return signal

keys = [
    b"mihai12345678901",  # Key 1: Incorrect key (simulating attacker guess)
    b"gabriela98765432",  # Key 2: Incorrect key (another attacker guess)
    b"remus12345678901",  # Correct Key: Used in encryption
    b"random_fake_key22"  # Key 3: Incorrect key
]

acoustic_signals = {key: simulate_acoustic(key) for key in keys}

# Spectrogram
for key, signal in acoustic_signals.items():
    f, t, Sxx = spectrogram(signal, fs=1000)
    plt.pcolormesh(t, f, 10 * np.log10(Sxx))
    plt.title(f"Spectrogram for Key: {key}")
    plt.ylabel("Frequency [Hz]")
    plt.xlabel("Time [s]")
    plt.colorbar(label="Intensity (dB)")
    plt.show()
