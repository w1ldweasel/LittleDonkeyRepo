# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:19:13 2019

@author: Max Ng
"""

from cryptography.fernet import Fernet
import base64

def main(): 
    generate_key()
    encrypt_text_input()

def generate_key():
    keyfile_name = input("Enter name of file to save key >")
    keyfile_name = keyfile_name + ".key"
    print(keyfile_name)
    f = open(keyfile_name, "wb")
    key = Fernet.generate_key()
    f.write(key)
    f.close()
     

def encrypt_text_input():
    message = input("Enter plaintext >") 
    keyfile = input("Enter key filename >") 
    keyfile = keyfile + ".key"
    
    f = open(keyfile, "rb")
    key = f.read()
    f.close()
    
    encoded_message = message.encode()
    cipher = Fernet(key)
    cipher_text = cipher.encrypt(encoded_message)
    print (cipher_text) #Use to output the ciphertext
    
    #Test the decryption restores the original plaintext
    """decrypted_message = cipher.decrypt(cipher_text)
    plaintext_message = decrypted_message.decode()
    print (plaintext_message)"""
    

def base64_encode():
    encoded_data = base64.b64encode("Base64 encode this text")
    print(encoded_data)
    
def base64_decode(encoded_text):
    decoded_data = base64.b64encode(encoded_text)
    print(decoded_data)

if __name__ == "__main__":
    main()
