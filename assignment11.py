def diffie_hellman(p, g, a, b):
    # Alice public key
    A = pow(g, a, p)
    # Bob public key
    B = pow(g, b, p)
    # Shared secret key
    key1 = pow(B, a, p)
    key2 = pow(A, b, p)
    print("Alice Public Key:", A)
    print("Bob Public Key:", B)
    print("Alice Shared Key:", key1)
    print("Bob Shared Key:", key2)
# MAIN PROGRAM
def main():
    print("Diffie-Hellman Key Exchange")
    p = int(input("Enter prime number p: "))
    g = int(input("Enter primitive root g: "))
    a = int(input("Enter Alice private key: "))
    b = int(input("Enter Bob private key: "))
    diffie_hellman(p, g, a, b)
if __name__ == "__main__":
    main()

#p = prime number
#g = primitive root of p
#a = Alice's private key, 1 < a < p
#b = Bob's private key, 1 < b < p
#Shared keys must be equal
# 11.Write a program to implement Diffie-Hellman Key Exchange.

