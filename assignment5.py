def encrypt(text, key):  #5. One Time Pad Cipher
    result = ""
    for i in range(len(text)):
        result += chr((ord(text[i].upper()) - 65 + ord(key[i]) - 65) % 26 + 65)
    return result
def decrypt(text, key, original):
    result = ""
    for i in range(len(text)):
        result += chr((ord(text[i]) - 65 - (ord(key[i]) - 65)) % 26 + 65)
    if original.islower():
        result = result.lower()
    return result
def main():        #MAIN PROGRAM
    print("One Time Pad Cipher Program")
    plaintext = input("Enter plaintext: ")
    file = open("key.txt", "r")
    key = file.read().strip().upper()
    file.close()
    if len(key) < len(plaintext):
        print("Key is too short!")
        return
    key = key[:len(plaintext)]
    encrypted = encrypt(plaintext, key)
    decrypted = decrypt(encrypted, key, plaintext)
    print("\nRESULT")
    print("Encrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
if __name__ == "__main__":
    main()
    #5. You are supplied a file of large nonrepeating set of truly random key letter. 
    # Your job is to encrypt the plaintext using ONE TIME PAD technique.
    #  Then perform the reverse operation to get original plaintext.