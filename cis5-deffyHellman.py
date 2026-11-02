def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

p = int(input("Enter prime number: "))
g = int(input("Enter primitive root: "))
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

if not is_prime(p) or not 1 < g < p or a <= 0 or b <= 0:
    print("Invalid Input")
else:
    A = pow(g, a, p)
    B = pow(g, b, p)

    KA = pow(B, a, p)
    KB = pow(A, b, p)

    print("Alice's Public Key:", A)
    print("Bob's Public Key:", B)
    print("Alice's Shared Secret:", KA)
    print("Bob's Shared Secret:", KB)

    if KA == KB:
        print("Key Exchange Successful!")
    else:
        print("Key Exchange Failed!")
