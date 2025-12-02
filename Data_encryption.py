import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
#print(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars : {chars} ")
#print(f" {key} ")

#ENCRYPTION
plain_text = input("Enter the message to be encrypted: ")
cipher_text = ""

for letter in plain_text:
    index = key.index(letter)
    cipher_text += chars[index]

print(f"original message: {plain_text}")
print(f"encrypted  message: {cipher_text}")

#Decryption
plain_text = input("Enter the message to be decrypted: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]


print(f"encrypted  message: {cipher_text}")
print(f"original message: {plain_text}")



