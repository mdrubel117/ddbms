import hashlib

text = input("Enter message: ")

hash_value = hashlib.md5(text.encode()).hexdigest()

print("MD5 Hash:", hash_value)
#8. Write a program to implement MD5 one way hash function.



