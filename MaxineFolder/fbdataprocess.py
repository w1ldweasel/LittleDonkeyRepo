#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:52:48 2019

@author: maxinemcfarlane
"""

from firebase_admin import db
import firebase_admin
import os

#*** NEED TO FIGURE OUT AUTHORISE STEP *** 
default_app = firebase_admin.initialize_app()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/maxinemcfarlane/Downloads/APIkey1.json"

ref = db.reference('/test/thisisahibstest')

print(ref.get())