# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:33:41 2019

@author: Admin
"""
import base64
import time

def main(): 
    decoded_file = 'decoded_file.txt'
    base64_decode('back_to_80s.txt', decoded_file)
    print('\n')
    f = open(decoded_file, 'r')
    for lines in f:
        new_line = lines.replace(' it', ' GIT')
        print(new_line)
        time.sleep(0.77)
    f.close()

def base64_decode(source_file, decoded_file):

    f = open(source_file, "r")
    input_file = f.read()
    f.close()
    f = open(decoded_file, "w")
    decoded_output= base64.b64decode(input_file) 
    decoded_file = f.write(decoded_output.decode())#decode the byte outbut from Base64 decoding
    f.close()

if __name__ == "__main__":
    main()
