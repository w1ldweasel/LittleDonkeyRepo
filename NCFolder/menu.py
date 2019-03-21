#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:55:15 2019
@author: carnivor
Now creates menu from folder items...

TO DO LIST
1, need remove menu.py from displaying in menu list

To get current scriptname -  os.path.basename(sys.argv[0])

"""

import time as t
import sys
import subprocess
import os
from os import listdir

def choice():
    FOLDER = os.getcwd()
    FILE_NAMES = [fn for fn in listdir(FOLDER) if fn.endswith(".py")]
    COUNT = -1
    for f in FILE_NAMES:
        COUNT = COUNT + 1
        print("[%s] " % COUNT + f)

    while True:
        ANS_FILE = input("Select script (or q to quit): ")
        if ANS_FILE.lower() == 'q':
            print("\n")
            print("So you want to leave...")
            t.sleep(1)
            quit("Bye Bye")
        elif int(ANS_FILE) > COUNT:
            print("\n")
            print("Wrong selection.")
            continue
        PATH = FOLDER + "/" + FILE_NAMES[int(ANS_FILE)]
        print("\n")
        print("Selected file: %s " % PATH)
        print("\n")
        runchoice(PATH)
        print("\n")
        choice()

def runchoice(PATH):
    subprocess.run(["python", PATH])

print("   ____                       __  __                  ")
print("  / ___|__ _ _ __ _ __  ___  |  \/  | ___ _ __  _   _ ")
print(" | |   / _` | '__| '_ \/ __| | |\/| |/ _ \ '_ \| | | |")
print(" | |__| (_| | |  | | | \__ \ | |  | |  __/ | | | |_| |")
print("  \____\__,_|_|  |_| |_|___/ |_|  |_|\___|_| |_|\__,_|")
print("\n")


#main()
if __name__ == "__main__":
    choice()
