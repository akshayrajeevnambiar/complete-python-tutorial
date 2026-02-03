from collections import deque
from art import print_logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt (text: list, shift: int) -> str:
    shifted_alphabets = deque(alphabet)
    shifted_alphabets.rotate(shift)
        
    for i in range(len(text)):
        if text[i] != ' ':
            encrypted_char = shifted_alphabets[alphabet.index(text[i].lower())]
            text[i] = encrypted_char.upper() if text[i].isupper() else encrypted_char
    return ''.join(text)

def decrypt (text: list, shift: int) -> str:
    shifted_alphabets = deque(alphabet)
    shifted_alphabets.rotate(shift)
        
    for i in range(len(text)):
        if text[i] != ' ':
            encrypted_char = alphabet[shifted_alphabets.index(text[i].lower())]
            text[i] = encrypted_char.upper() if text[i].isupper() else encrypted_char
    return ''.join(text)

def caeser_logic():
    flag = ""
    while flag.lower() != "exit":
        flag = input("would you like to encrypt, decrypt or exit : ")
        if flag.lower() == "encrypt":
            print(encrypt(list(input("Enter the text you would like to encrypt: ")), int(input("Shift characters by : " ))))
        elif flag.lower() == "decrypt":
            print(decrypt(list(input("Enter the text you would like to encrypt: ")), int(input("Shift characters by : " ))))
        elif flag.lower() == "exit":
            print("exiting program")
        else:
            print("choice not valid please try again! ")

print_logo()
caeser_logic()