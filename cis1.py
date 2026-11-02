def caeser(plaintext, key):
    min = ord('a')
    size = 26

    result = ""
    for char in plaintext:
        char_code = ord(char)
        cipher = min + ((char_code - min + key) % size)
        result += chr(cipher)

    return result

def decrypt(ciphertext, key):
    return caeser(ciphertext, -key)

plain = input("Enter a Name: ")
key = int(input("Enter a Number: "))

cipher = caeser(plain, key)

print("Plaintext: ", plain)
print("Ciphertext", cipher)
print("Decrypttext", decrypt(cipher, key))


# rail fence
def encrypt(plain):
    even = ""
    odd = ""

    for i in range(len(plain)):
        if i % 2 == 0:
            even += plain[i]
        else :
            odd += plain[i]
    return even + odd

def decrypt(cipher):
    mid = (len(cipher) + 1) // 2
    even = cipher[:mid]
    odd = cipher[mid:]
    plain = ""

    for i in range(len(odd)):
        plain += even[i]
        plain += odd[i]

    if len(even) > len(odd):
        plain += even[-1]

    return plain

plain = input("Enter a name: ")
cipher = encrypt(plain)

print("Encryption: ", cipher)
print("Decryption: ", decrypt(cipher))


