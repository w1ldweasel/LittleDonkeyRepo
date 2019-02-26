# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:19:13 2019

@author: Max Ng
"""

from cryptography.fernet import Fernet
import base64

def main(): 

    print ("\n")
    print ("Choose an option 1, 2, 3, 4")
    print ("1 to generate a new key")
    print ("2 to encrypt a file")
    print ("3 to decrypt a file")
    print ("4 to encrypt input text")
    user_selection = input("Enter choice >")
    
    if user_selection == '1':
        generate_key()
    elif user_selection == '2':
        encrypt_file()
    elif user_selection == '3':
        decrypt_file()
    elif user_selection == '4':
        encrypt_text_input()
    else: print("No valid choice entered, closing.") 

def generate_key():
    keyfile_name = input("Enter name of file to save key >")
    f = open(keyfile_name, "wb")
    key = Fernet.generate_key()
    f.write(key)
    f.close()
     
def encrypt_file():
    keyfile = input("Enter key filename to retrieve key >") 
    source_file = input("Enter filename to encrypt contents, including extension >") 
    
    f = open(keyfile, "rb")
    key = f.read()
    f.close()
    
    f = open(source_file, "r")
    message = f.read()
    f.close()
    
    encoded_message = message.encode()
    cipher = Fernet(key)
    cipher_text = cipher.encrypt(encoded_message)
    #print (cipher_text) #Use to check the ciphertext
    
    f = open(source_file, "wb")
    f.write(cipher_text)
    f.close()


def decrypt_file():
    #Restore the original plaintext
    keyfile = input("Enter key filename to get the original encryption key >")
    source_file = input("Enter filename to decrypt contents, including extension >") 
    
    f = open(keyfile, "rb")
    key = f.read()
    f.close()
    
    f = open(source_file, "rb")
    cipher_text = f.read()
    
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(cipher_text)
    plaintext_message = decrypted_message.decode()
    #print (plaintext_message)
    
    f = open(source_file, "w")
    f.write(plaintext_message)
    f.close()
    
    
def encrypt_text_input():
    keyfile = input("Enter key filename >") 
    message = input("Enter plaintext >") 

    
    f = open(keyfile, "rb")
    key = f.read()
    f.close()
    
    encoded_message = message.encode()
    cipher = Fernet(key)
    cipher_text = cipher.encrypt(encoded_message)
    print (cipher_text) #Use to output the ciphertext
    
    #Test the decryption restores the original plaintext
    decrypted_message = cipher.decrypt(cipher_text)
    plaintext_message = decrypted_message.decode()
    print (plaintext_message)
    

def base64_encode():
    encoded_data = base64.b64encode("Base64 encode this text")
    print(encoded_data)
    
def base64_decode(encoded_text):
    decoded_data = base64.b64encode(encoded_text)
    print(decoded_data)

if __name__ == "__main__":
    main()
