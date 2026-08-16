from Crypto.Hash import SHA1
import secrets
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import DES3, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
A = RSA.generate(2048)          # Sender private key
A_pub = A.publickey()            # Sender public key
B = RSA.generate(2048)          # Receiver private key
B_pub = B.publickey()            # Receiver public key
m = input("Enter message: ").encode()   # Input message
k = DES3.adjust_key_parity(secrets.token_bytes(16))   # 128-bit session key,a. CONFIDENTIALITY
c = DES3.new(k, DES3.MODE_ECB).encrypt(pad(m, 8))     # 3DES encryption
ek = PKCS1_OAEP.new(B_pub).encrypt(k)                 # RSA encrypt session key
print("\n--- CONFIDENTIALITY ---")
print("Encrypted Key:", ek.hex())
print("Encrypted Data:", c.hex())
k = PKCS1_OAEP.new(B).decrypt(ek)                     # RSA decrypt session key
m = unpad(DES3.new(k, DES3.MODE_ECB).decrypt(c), 8)   # 3DES decryption
print("Original Message:", m.decode()) #b. AUTHENTICATION + CONFIDENTIALITY 
h = SHA1.new(m)                       # SHA-1 hash
s = pkcs1_15.new(A).sign(h)           # RSA signature
data = s + m                          # Signature + Message
k = DES3.adjust_key_parity(secrets.token_bytes(16))   # 128-bit session key
c = DES3.new(k, DES3.MODE_ECB).encrypt(pad(data, 8))  # 3DES encryption
ek = PKCS1_OAEP.new(B_pub).encrypt(k)                 # RSA encrypt session key
k = PKCS1_OAEP.new(B).decrypt(ek)                     # RSA decrypt session key
data = unpad(DES3.new(k, DES3.MODE_ECB).decrypt(c), 8)
s = data[:256]                         # Separate signature
m = data[256:]                         # Separate message
try:
    pkcs1_15.new(A_pub).verify(SHA1.new(m), s)         # Verify signature
    print("\nAuthentication: Successful")
except ValueError:
    print("\nAuthentication: Failed")
#14. Write a program to implement the following services of PGP. You have to follow all the steps mentioned in the algorithms.
#a. Confidentiality for storing data.
#b. Authentication and Confidentiality.