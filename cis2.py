from math import gcd
p = int(input("Enter The Value of p : "))
q = int(input("Enter The Value of q : "))
n = p*q
phi=(p-1)*(q-1)

e, d = 2, 2
while e < phi and gcd(e, phi) != 1:
    e += 1
while d < phi and (d*e) % phi != 1:
    d += 1

print(f"Public Key : ({e}, {n})")
print(f"Private Key : ({d}, {n})")

def encrypt(plain):
    return pow(plain, e, n)

def decrypt(cipher):
    return pow(cipher, d, n)

plain = int(input("Enter A Number : "))
cipher = encrypt(plain)
print(f"Cipher Text : {cipher}")
print(f"Plain Text : {decrypt(cipher)}")
