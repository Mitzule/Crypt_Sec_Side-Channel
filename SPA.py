"""
Simulare SPA (Simple Power Analysis)
Scop: Simulăm consumul de putere al algoritmului de criptare AES pe baza activității bit cu bit.

Cod pentru Simulare SPA
Simulăm consumul de putere al fiecărui bit din textul cifrat.
Calculăm suma biturilor setate pentru fiecare operațiune AES (aceasta corespunde activității tranzistorilor).
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import numpy as np
import matplotlib.pyplot as plt

def hamming_weight(byte_array):
    """Calculează greutatea Hamming (numărul de biți setați)."""
    return sum(bin(byte).count('1') for byte in byte_array)

def simulate_power_analysis(plaintext, key):
    """Simulează consumul de putere pe baza greutății Hamming."""
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    power_consumption = hamming_weight(ciphertext)  # Consumul de putere estimat
    return power_consumption

# Date sintetice
plaintexts = [b"Test data 1", b"Test data 2", b"Test data 3"]
key = b"testkeytestkey12"  # Cheie de 128 biți

power_data = [simulate_power_analysis(pt, key) for pt in plaintexts]

# Crearea graficului
plt.figure(figsize=(10, 6))
plt.bar(range(len(power_data)), power_data, color='purple')
plt.title("Simulare Simple Power Analysis (SPA)")
plt.xlabel("Operații de criptare")
plt.ylabel("Consumul de putere (greutatea Hamming)")
plt.show()
