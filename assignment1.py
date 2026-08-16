def encrypt(text, shift=3):
    result = ""
    for char in text:
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
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result
def main():             #MAIN PROGRAM 
    print("Caesar Cipher Program")
    plaintext = input("Enter plaintext:")
    encrypted = encrypt(plaintext)
    decrypted = decrypt(encrypted)
    print("\nRESULT")
    print("Encrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
if __name__ == "__main__":
    main()

    #1.Suppose you are given a line of text as a plaintext, find out the corresponding Caesar Cipher.
    #(i.e. character three to the right modulo 26). A → shift 3 → D,B → E,Z → C (wrap using %26).
    #Then perform the reverse operation to get original plaintext.