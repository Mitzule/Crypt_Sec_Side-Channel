"""
https://imgur.com/a/XhuTB1H
"""
import numpy as np
import matplotlib.pyplot as plt

# Date simulate (timpi în secunde)
keys = ["Key1", "Key2", "CorrectKey", "Key4"]
timing_data = {
    "Key1": [0.045, 0.046, 0.047, 0.045],
    "Key2": [0.043, 0.044, 0.045, 0.044],
    "CorrectKey": [0.060, 0.062, 0.061, 0.063],
    "Key4": [0.046, 0.045, 0.047, 0.046],
}

# Calcul timp mediu și deviație standard
average_times = {key: np.mean(times) for key, times in timing_data.items()}
std_devs = {key: np.std(times) for key, times in timing_data.items()}

# Grafic
plt.figure(figsize=(10, 6))
plt.bar(average_times.keys(), average_times.values(), yerr=std_devs.values(), capsize=5, color='skyblue')
plt.title("Timp mediu și deviație standard pentru fiecare cheie")
plt.ylabel("Timp mediu (secunde)")
plt.xlabel("Cheie")
plt.axhline(y=max(average_times.values()), color='red', linestyle='--', label="Timp maxim (cheia corectă)")
plt.legend()
plt.show()
