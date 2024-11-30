"""
https://imgur.com/a/4sHFgx9
"""
from scipy.stats import pearsonr

# Simulare date (Hamming Weight și consum)
hamming_weights = [5, 7, 6, 8, 5, 6, 7, 5]  # HW pentru fiecare operație
power_consumption = [0.2, 0.25, 0.23, 0.28, 0.19, 0.22, 0.24, 0.21]  # Consumul simulat

# Calcul corelație
correlation, _ = pearsonr(hamming_weights, power_consumption)

# Grafic
plt.figure(figsize=(10, 6))
plt.scatter(hamming_weights, power_consumption, color='orange')
plt.title(f"Corelația între Hamming Weight și consum: {correlation:.2f}")
plt.xlabel("Hamming Weight")
plt.ylabel("Consum (unități arbitrare)")
plt.grid(True)
plt.show()
