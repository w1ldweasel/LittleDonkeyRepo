#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:55:15 2019

@author: carnivor
"""

import sys
from  subprocess import call

print("   ____                       __  __                  ")
print("  / ___|__ _ _ __ _ __  ___  |  \/  | ___ _ __  _   _ ")
print(" | |   / _` | '__| '_ \/ __| | |\/| |/ _ \ '_ \| | | |")
print(" | |__| (_| | |  | | | \__ \ | |  | |  __/ | | | |_| |")
print("  \____\__,_|_|  |_| |_|___/ |_|  |_|\___|_| |_|\__,_|")
print("\n")
print("Press 1,2, 3 to run your choosen script or Q to exit")
print("\n")
print("1 : Hello World")
print("2 : Lotto Numbers")
print("3 : Christmas Countdown")
print()
print("q : Quit")

def choice():
    """
    Menu Choices
    """
    script_choice = input('Choice >')
    if script_choice == '1':
        call(["python", "HelloWorld.py"])
    elif script_choice == '2':
        call(["python", "gamenumbers.py"])
    elif script_choice == '3':
        call(["python", "xmascount.py"])
    elif script_choice.lower() == 'q':
        print("So you want to leave...")
        sys.exit("Bye Bye")
    else: print("You did not enter 1, 2, 3, or q, so try again")
    choice()

#main()
if __name__ == "__main__":
    choice()
