def encrypt(text, shift=3):
    result = ""
    while len(text) % 3 != 0:  # Add padding if length is not divisible by 3
        text += 'X'
    for i in range(0, len(text), 3):   # Process 3 characters at a time
        block = text[i:i+3]
        for char in block:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += char
    return result
def decrypt(text, shift=3):
    result = ""
    for i in range(0, len(text), 3):     # Process 3 characters at a time
        block = text[i:i+3]
        for char in block:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - 65 - shift) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                result += char
    return result
def main():        #MAIN PROGRAM 
    print("Polygram Substitution Cipher")
    plaintext = input("Enter plaintext: ")
    encrypted = encrypt(plaintext)
    decrypted = decrypt(encrypted)
    print("\nRESULT")
    print("Encrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
if __name__ == "__main__":
    main()


    #2. Find out the Polygram Substitution Cipher of a given plaintext
    #  (Consider the block size of 3).
    #  Then perform the reverse operation to get original plaintext.
    #HELLO→ HEL|LOX .Then HEL → ELH,LOX → OXL