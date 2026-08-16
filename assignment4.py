def encrypt(text, width1, width2):
    text = text.replace("","")       # First transposition
    while len(text) % width1 != 0:
        text += "X"
    result = ""
    for col in range(width1):
        for row in range(0, len(text), width1):
            result += text[row + col]
    print("\n1st Encryption:", result)
    text = result       # Second transposition
    while len(text) % width2 != 0:
        text += "X"
    result = ""
    for col in range(width2):
        for row in range(0, len(text), width2):
            result += text[row + col]
    return result
def decrypt(text, width1, width2):    # Reverse second transposition
    rows = len(text) // width2
    result = ""
    for row in range(rows):
        for col in range(width2):
            index = col * rows + row
            result += text[index]
    text = result     # Reverse first transposition
    rows = len(text) // width1
    result = ""
    for row in range(rows):
        for col in range(width1):
            index = col * rows + row
            result += text[index]
    return result.rstrip("X")
def main():   # MAIN PROGRAM
    print("Double Transposition Cipher Program")
    plaintext = input("Enter plaintext: ")
    width1 = int(input("Enter first width: "))
    width2 = int(input("Enter second width: "))
    encrypted = encrypt(plaintext, width1, width2)
    decrypted = decrypt(encrypted, width1, width2)
    words = plaintext.split()  # Restore spaces using original plaintext
    result = ""
    position = 0
    for word in words:
        result += decrypted[position:position + len(word)] + " "
        position += len(word)
    result = result.strip()
    print("\nRESULT")
    print("Encrypted Text:", encrypted)
    print("Decrypted Text:", result)
if __name__ == "__main__":
    main()
    #Find out corresponding double Transposition Cipher of the above plaintext. 
    # Then perform the reverse operation to get original plaintext.