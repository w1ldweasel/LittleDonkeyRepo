# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:19:13 2019

@author: Max Ng
"""

from cryptography.fernet import Fernet

def main(): 
    generate_key()

def generate_key():
    f = open("keyfile.txt", "w")
    key = Fernet.generate_key()
    f.write(str(key) + "\r\n")
     

if __name__ == "__main__":
    main()
