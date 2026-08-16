from Crypto.Hash import SHA1
import secrets
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import DES3, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
A = RSA.generate(2048)          # Sender private key
A_pub = A.publickey()           # Sender public key
B = RSA.generate(2048)          # Receiver private key
B_pub = B.publickey()           # Receiver public key
m = input("Enter message: ").encode()   # Input message
h = SHA1.new(m)                 # SHA-1 hash
s = pkcs1_15.new(A).sign(h)     # RSA signature
data = s + m                    # Attach signature with message
k = DES3.adjust_key_parity(
    secrets.token_bytes(16))                               # Random 128-bit session key
c = DES3.new(k, DES3.MODE_ECB).encrypt(
    pad(data, 8)
)                               # Encrypt data using 3DES
ek = PKCS1_OAEP.new(B_pub).encrypt(k)   # Encrypt session key
print("\n--- ENCRYPTION ---")
print("Encrypted Key:", ek.hex())
print("Encrypted Data:", c.hex())
k = PKCS1_OAEP.new(B).decrypt(ek)       # Decrypt session key
data = unpad(
    DES3.new(k, DES3.MODE_ECB).decrypt(c), 8)                                       # Decrypt data
s = data[:256]                          # Separate signature
m = data[256:]                          # Separate message
try:
    pkcs1_15.new(A_pub).verify(
        SHA1.new(m), s)                                   # Verify signature
    print("\nOriginal Message:", m.decode())
    print("Authentication: Successful")
except ValueError:
    print("\nAuthentication: Failed")
# 12. PGP Services
# a. Authentication
# b. Confidentiality for transmitting data.