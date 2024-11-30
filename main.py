from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

""""
- Run the code, you will be asked in the console to enter the plain text
- After pressing enter you will be asked to enter the 3 keys needed 16 bits (16 letter/number input)
- After all the keys are entered the output will be the encrypted text and the decrypted text at the bottom
"""
def feistel_encrypt_round(plaintext, key, rounds=8, verbose=False):
    
    #decryption with given key
    assert len(key) == 16, "Key must be 16 bytes for AES-128"

    #split text
    half_length = len(plaintext) // 2
    left = plaintext[:half_length]
    right = plaintext[half_length:]

    for r in range(rounds):
        cipher = AES.new(key, AES.MODE_ECB)

        #xor between right(after encryption) and left
        right_encrypted = cipher.encrypt(pad(right, AES.block_size))[:len(left)]
        new_left = bytes(x ^ y for x, y in zip(left, right_encrypted))

        #swap for feistel
        left, right = right, new_left

    return left + right

def feistel_decrypt_round(ciphertext, key, rounds=8, verbose=False):
    
    #decryption with given key
    assert len(key) == 16, "Key must be 16 bytes for AES-128"

    #split text
    half_length = len(ciphertext) // 2
    left = ciphertext[:half_length]
    right = ciphertext[half_length:]

    for r in range(rounds):
        cipher = AES.new(key, AES.MODE_ECB)

        #xor between left(after encryption) and right
        left_encrypted = cipher.encrypt(pad(left, AES.block_size))[:len(right)]
        new_right = bytes(x ^ y for x, y in zip(right, left_encrypted))

        #swap for feistel
        right, left = left, new_right

    return left + right

def layered_feistel_encrypt(plaintext, key1, key2, key3, rounds=8, verbose=False):
    #encrypt with 1st - decrypt with 2nd - decrypt with 3rd
    encrypted_once = feistel_encrypt_round(plaintext, key1, rounds, verbose)
    decrypted_once = feistel_decrypt_round(encrypted_once, key2, rounds, verbose)
    final_encrypted = feistel_encrypt_round(decrypted_once, key3, rounds, verbose)

    return final_encrypted

def layered_feistel_decrypt(ciphertext, key1, key2, key3, rounds=8, verbose=False):
    
    #decrypt with 3rd - encrypt with 2nd - decrypt with 1st
    decrypted_once = feistel_decrypt_round(ciphertext, key3, rounds, verbose)
    encrypted_once = feistel_encrypt_round(decrypted_once, key2, rounds, verbose)
    final_decrypted = feistel_decrypt_round(encrypted_once, key1, rounds, verbose)

    return final_decrypted

if __name__ == "__main__":
    input_text = input("Enter the plaintext: ").encode()
    key1 = input("Enter a 16-byte (128-bit) key 1: ").encode()
    key2 = input("Enter a 16-byte (128-bit) key 2: ").encode()
    key3 = input("Enter a 16-byte (128-bit) key 3: ").encode()

    #check key length
    if len(key1) != 16:
        print("Invalid key 1 length. Generating a random 16-byte key.")
        key1 = get_random_bytes(16)
    if len(key2) != 16:
        print("Invalid key 2 length. Generating a random 16-byte key.")
        key2 = get_random_bytes(16)
    if len(key3) != 16:
        print("Invalid key 3 length. Generating a random 16-byte key.")
        key3 = get_random_bytes(16)


    if len(input_text) % 2 != 0:
        input_text += b" "

    #encryption process
    ciphertext = layered_feistel_encrypt(input_text, key1, key2, key3)
    print("\nCiphertext (hex):", ciphertext.hex())

    #decryption process
    decrypted_text = layered_feistel_decrypt(ciphertext, key1, key2, key3)
    print("\nDecrypted text:", decrypted_text.decode().strip())  #cut extra padding