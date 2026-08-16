def encrypt(text, width):
    result = ""
    text = text.replace("", "")    # Remove spaces
    while len(text) % width != 0:     # Add padding if needed
        text += "X"
    for col in range(width):     # Read column by column
        for row in range(0, len(text), width):
            result += text[row + col]
    return result
def decrypt(text, width):
    result = ""
    rows = len(text) // width
    for row in range(rows):      # Read column by column and reconstruct rows
        for col in range(width):
            index = col * rows + row
            result += text[index]
    return result.rstrip("X")
def main():     #MAIN PROGRAM
    print(" Transposition Cipher Program ")
    plaintext = input("Enter plaintext: ")
    width = int(input("Enter width: "))
    encrypted = encrypt(plaintext, width)
    decrypted = decrypt(encrypted, width)
    print("\nRESULT")
    print("Encrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
if __name__ == "__main__":
    main()


    #3. Consider the plaintext “DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLY UNIVERSITY OF RAJSHAHI BANGLADESH”.
    # find out the corresponding Transposition Cipher (Take width as input).
    #  Then perform the reverse operation to get original plaintext.
    #Plaintext: HELLO WORLD
    #HELLOWORLD
    #Width: 3
    #HEL
    #LOW
    #ORL
    #DXX



