#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:52:48 2019

@author: maxinemcfarlane
"""

from firebase_admin import db
import firebase_admin

#*** NEED TO FIGURE OUT AUTHORISE STEP ?? works in initdbase but not here ? *** 
default_app = firebase_admin.initialize_app()

ref = db.reference('/test/thisisahibstest')

print(ref.get())