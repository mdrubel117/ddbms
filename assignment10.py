def rsa(p, q, e, message, block_size):
    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)
    # Calculate d
    d = pow(e, -1, phi)
    print("n =", n)
    print("phi =", phi)
    print("Public Key:", e, n)
    print("Private Key:", d, n)
    # Plaintext Blocks
    blocks = []
    for i in range(0, len(message), block_size):
        blocks.append(message[i:i + block_size])
    print("Plaintext Blocks:", blocks)
    # Encryption
    encrypted = []
    for block in blocks:
        c = pow(int(block), e, n)
        encrypted.append(c)
    print("Encrypted Blocks:", encrypted)
    # Decryption
    decrypted = []
    for block in encrypted:
        m = pow(block, d, n)
        decrypted.append(str(m).zfill(block_size))
    print("Decrypted Blocks:", decrypted)
    # Original Plaintext
    original = ""
    for block in decrypted:
        original += block
    print("Original Plaintext:", original)
# MAIN PROGRAM
def main():
    print("RSA Encryption and Decryption")
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))
    e = int(input("Enter e: "))
    message = input("Enter plaintext number: ")
    block_size = int(input("Enter block size: "))
    rsa(p, q, e, message, block_size)
if __name__ == "__main__":
    main()
    #if you ensure:
#p and q are different primes
#1 < e < φ(n)
#gcd(e, φ(n)) = 1
#plaintext is numeric
#every plaintext block is < n
#10. Encrypt the plaintext message using RSA algorithm. 
# Then perform the reverse operation to get original plaintext.