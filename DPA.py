"""
Simulare DPA (Differential Power Analysis)
Scop: Analizăm corelația între consumul de putere simulat și părți ale cheii.

Generăm consumuri pentru mai multe texte brute.
Identificăm corelațiile care indică cheia corectă.
"""
from scipy.stats import pearsonr

def generate_power_samples(plaintexts, key):
    """Generează date sintetice de consum de putere."""
    power_samples = []
    for pt in plaintexts:
        power_samples.append(simulate_power_analysis(pt, key))
    return power_samples

# Date sintetice
plaintexts = [b"Test data %d" % i for i in range(1, 11)]
correct_key = b"realkey123456789"
wrong_key = b"fakekey098765432"

# Generăm consumuri de putere
power_correct = generate_power_samples(plaintexts, correct_key)
power_wrong = generate_power_samples(plaintexts, wrong_key)

# Corelație
correlation_correct, _ = pearsonr(range(len(power_correct)), power_correct)
correlation_wrong, _ = pearsonr(range(len(power_wrong)), power_wrong)

# Grafic
plt.figure(figsize=(10, 6))
plt.plot(power_correct, label=f"Cheie corectă (corelație: {correlation_correct:.2f})", color="green")
plt.plot(power_wrong, label=f"Cheie greșită (corelație: {correlation_wrong:.2f})", color="red")
plt.title("Simulare Differential Power Analysis (DPA)")
plt.xlabel("Operații")
plt.ylabel("Consumul de putere (simulat)")
plt.legend()
plt.show()
