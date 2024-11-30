"""
Timing Attack - Grafic de timp mediu
Pentru un atac de tip timing:

Generăm un grafic care arată timpul mediu necesar pentru fiecare cheie testată.
Evidențiem cheia corectă, care ar putea avea o deviație semnificativă.
"""
import matplotlib.pyplot as plt

# Date simulate
keys = ["Key1", "Key2", "Key3", "CorrectKey", "Key5"]
timing_results = [0.045, 0.046, 0.044, 0.060, 0.045]  # Cheia corectă are o valoare mai mare

# Crearea graficului
plt.figure(figsize=(10, 6))
plt.bar(keys, timing_results, color='skyblue')
plt.title("Rezultatele Timing Attack")
plt.xlabel("Chei testate")
plt.ylabel("Timp mediu (secunde)")
plt.axhline(y=max(timing_results), color='red', linestyle='--', label="Cheia corectă")
plt.legend()
plt.show()
