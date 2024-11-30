# Simulare timpi
import random
correct_key_times = [random.gauss(0.06, 0.005) for _ in range(100)]
wrong_key_times = [random.gauss(0.045, 0.005) for _ in range(100)]

# Grafic
plt.figure(figsize=(10, 6))
plt.hist(correct_key_times, bins=20, alpha=0.7, label="Cheia corectă", color='green')
plt.hist(wrong_key_times, bins=20, alpha=0.7, label="Chei greșite", color='blue')
plt.title("Distribuția timpilor pentru Timing Attack")
plt.xlabel("Timp (secunde)")
plt.ylabel("Frecvență")
plt.legend()
plt.show()
