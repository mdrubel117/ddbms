import hashlib

text = input("Enter message: ")

hash_value = hashlib.sha1(text.encode()).hexdigest()

print("SHA-1 Hash:", hash_value)
#8. Write a program to implement MD5 one way hash function.



