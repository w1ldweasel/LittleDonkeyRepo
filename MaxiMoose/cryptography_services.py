# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:19:13 2019

@author: Max Ng
"""

from cryptography.fernet import Fernet
import base64
from os import path


def main(): 
    
    print ("\n")
    print ("Choose an option 1, 2")
    print ("1 for encryption")
    print ("2 to Base64 encode a file" )
    print ("3 to Base64 decode a file" )
    user_selection = input("Enter choice >")
    if user_selection == '1':
        fernet_encryption()
    elif user_selection == '2':
        base64_encode()
    elif user_selection == '3':
        base64_decode()
    else: print("No valid choice entered, closing.") 
    
def fernet_encryption(): 
    print ("\n")
    print ("Choose an option 1, 2, 3, 4")
    print ("1 to generate a new key")
    print ("2 to encrypt a file")
    print ("3 to decrypt a file")
    #print ("4 to encrypt input text")
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
    valid_files = True
    if path.exists(keyfile):
        invalid_keyfile = ""
    else:
        invalid_keyfile = "The key file name is invalid"
        valid_files = False
   
    if path.exists(source_file):
        invalid_sourcefile = ""
    else:
        invalid_sourcefile = "The input file name is invalid"
        valid_files = False
        
    if valid_files == False:
        print (invalid_keyfile, invalid_sourcefile)
    else:
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
    print ("\n")
    print ("Cipher text: ")
    print (cipher_text) #Use to output the ciphertext
    
    #Test the decryption restores the original plaintext
    decrypted_message = cipher.decrypt(cipher_text)
    plaintext_message = decrypted_message.decode()
    print ("\n")
    print ("Original plaintext: ")
    print (plaintext_message)
    

def base64_encode():
    source_file = input("Enter filename to encode >") 
    encoded_file = input("Enter filename to save encoded file as >") 
    f = open(source_file, "r")
    input_file = f.read()
    f.close()
    f = open(encoded_file, "wb")
    encoded_output= base64.b64encode(input_file.encode()) 
    encoded_file = f.write(encoded_output)
    f.close()

    
def base64_decode():
    source_file = input("Enter filename to decode >") 
    decoded_file = input("Enter filename to save decoded file as >") 
    f = open(source_file, "rb")
    input_file = f.read()
    f.close()
    f = open(decoded_file, "w")
    decoded_output= base64.b64decode(input_file) 
    base64decoded_file = f.write(decoded_output.decode())#decode the byte outbut from Base64 decoding
    f.close()

if __name__ == "__main__":
    main()
