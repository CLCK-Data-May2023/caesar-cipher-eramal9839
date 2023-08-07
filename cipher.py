#Write a Python program that encrypts text given by the user. The program should 
#ask the user for a plain text sentence and print the encrypted text. The text 
#should be encrypted using a caesar cipher with a right shift of 5.


#ask user what they want to encrypt 
user_sentence = input("What do you want to encrypt? ")

#placeholder essentially for the variable 
encrypted_text = ""


for char in user_sentence:
    if char.isalpha():
        shift = 65 if char.isupper() else 97
        shifted_char = chr((ord(char) - shift + 5) % 26 + shift)
        encrypted_text += shifted_char
    else:
        encrypted_text += char

print("Encrypted text:", encrypted_text)






