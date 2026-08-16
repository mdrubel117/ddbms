from Crypto.Hash import SHA1
import secrets
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import DES3, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
A = RSA.generate(2048)        # Generate RSA key # Sender private key
A_pub = A.publickey()           # Sender public key
B = RSA.generate(2048)          # Receiver private key
B_pub = B.publickey()           # Receiver public key
m = input("Enter message: ").encode()  # Input message
h = SHA1.new(m)   # SHA-1 hash and RSA signature
s = pkcs1_15.new(A).sign(h)
data = s + m  # Attach signature with message
k = DES3.adjust_key_parity(secrets.token_bytes(16))   # Generate random 128-bit session key
c = DES3.new(k, DES3.MODE_ECB).encrypt(pad(data, 8))   # Encrypt data using 3DES
ek = PKCS1_OAEP.new(B_pub).encrypt(k)    # Encrypt session key using receiver public key
print("\n--- ENCRYPTION ---")
print("Encrypted Key:", ek.hex())
print("Encrypted Data:", c.hex())
k = PKCS1_OAEP.new(B).decrypt(ek)   # Decrypt session key using receiver private key
data = unpad(                              # Decrypt data using 3DES
    DES3.new(k, DES3.MODE_ECB).decrypt(c), 8)
s = data[:256]   # Separate signature and message
m = data[256:]
try:                     # Verify RSA signature using sender public key
    pkcs1_15.new(A_pub).verify(SHA1.new(m), s)
    print("\nOriginal Message:", m.decode())
    print("Authentication: Successful")
except ValueError:
    print("\nAuthentication: Failed")


    
    #13. Write a program to implement the following services of PGP. 
    # You have to follow all the steps mentionedin the algorithms.
    # a. Authentication.b. Confidentiality for storing data.

