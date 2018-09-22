import numpy as np


def KSA(key):
    key_length = len(key)
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % key_length]) % 256
        s[i], s[j] = s[j], s[i]  # swap
    return s


def PRAG(s, n):
    i = 0
    j = 0
    key = []
    while n > 0:
        n = n - 1
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]  # swap
        k = s[(s[i] + s[j]) % 256]
        key.append(k)
    return key


def preparing_key_array(s):
    return [ord(c) for c in s]


def main():
    key = 'attack'
    plaintext = 'Mission Accomplished'
    print('Key : ', key)
    print('plaintext : ', plaintext)
    key = preparing_key_array(key)
    s = KSA(key)
    key_stream = np.array(PRAG(s, len(plaintext)))
    print('Key stream is : ', key_stream)
    plaintext = np.array([ord(i) for i in plaintext])
    cipher = key_stream ^ plaintext  # XOR keystream and plaintext
    print('Ciphertext : ', cipher.astype(np.uint8).data.hex())


if __name__ == '__main__':
    main()
