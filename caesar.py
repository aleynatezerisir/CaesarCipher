# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 02:12:07 2021

@author: Kullanıcı
"""

import string

alphabet = string.ascii_lowercase 

def encrypt():
    
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to encrypt: ").strip()
    print()
    key = int(input("Enter key to encrypt: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c


    print("Your encrypted message is:\n")
    print(decrypted_message)
def decrypt():
    
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("Your decrypted message is:\n")
    print(decrypted_message)
encrypt()
decrypt()