"""
Analiză Power Analysis - Corelația consumului
Dacă simulăm consumul de putere, putem genera un grafic care arată variațiile în funcție de cheia folosită:

Generăm o serie de valori de consum (sintetice sau reale).
Calculăm corelația între date și cheia corectă.
"""
import numpy as np

# Date sintetice de consum
keys = ["Key1", "Key2", "CorrectKey", "Key4", "Key5"]
power_consumption = [0.2, 0.25, 0.35, 0.21, 0.22]  # Cheia corectă are un consum specific

# Crearea graficului
plt.figure(figsize=(10, 6))
plt.plot(keys, power_consumption, marker='o', color='orange')
plt.title("Analiza Consumului de Putere")
plt.xlabel("Chei testate")
plt.ylabel("Consum (unități arbitrare)")
plt.grid(True)
plt.show()
