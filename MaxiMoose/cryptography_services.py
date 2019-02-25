# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:19:13 2019

@author: Max Ng
"""

from cryptography.fernet import Fernet
import base64

def main(): 
    generate_key()
    encrypt_text()

def generate_key():
    f = open("keyfile.txt", "wb")
    key = Fernet.generate_key()
    f.write(key)
     

def encrypt_text():
    f = open("keyfile.txt", "rb")
    key = f.read()
    print (key)
    message = 'plaintext blah'
    encoded_message = message.encode()
    cipher = Fernet(key)
    cipher_text = cipher.encrypt(encoded_message)
    print (cipher_text)
    
    #Test the decryption
    plaintext_message = cipher.decrypt(cipher_text)
    print (plaintext_message)
    

def base64_encode():
    encoded_data = base64.b64encode("Base64 encode this text")
    print(encoded_data)
    
def base64_decode(encoded_text):
    decoded_data = base64.b64encode(encoded_text)
    print(decoded_data)

if __name__ == "__main__":
    main()
