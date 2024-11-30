"""
Timing Attack - Implementare practică
Putem simula un atac de timing folosind cod Python. Ideea este să generăm timpi de execuție artificial variați pe baza unor chei greșite și să măsurăm timpul necesar pentru fiecare. De exemplu:

Generăm un set de chei posibile.
Pentru fiecare cheie, rulăm criptarea/decriptarea de mai multe ori.
Calculăm timpul mediu pentru fiecare cheie și găsim cea care produce cele mai consistente rezultate.
"""
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def simulate_encryption(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, AES.block_size))

def timing_attack(ciphertext, possible_keys):
    timing_results = {}
    for key in possible_keys:
        start = time.time()
        try:
            simulate_encryption(ciphertext, key)
        except:
            pass
        end = time.time()
        timing_results[key] = end - start
    # Sort the keys by timing
    best_key = min(timing_results, key=timing_results.get)
    return best_key, timing_results

# Exemplu de rulare
ciphertext = b"SampleText"
possible_keys = [b"testkey1testkey", b"testkey2testkey", b"actualkey123456"]
best_key, timings = timing_attack(ciphertext, possible_keys)
print(f"Key found: {best_key}, Timing results: {timings}")
