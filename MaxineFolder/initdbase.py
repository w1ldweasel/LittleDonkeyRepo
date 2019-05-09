#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:43:44 2019

@author: maxinemcfarlane
"""

#*** figure out how this works ***
#*** add comments so can easily change program to init any databases ***

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


#cred = credentials.Certificate("/Users/maxinemcfarlane/Downloads/APIkey1.json")
#default_app = firebase_admin.initialize_app(cred)

    
db = firestore.client()

doc_ref = db.collection('test').document('thisisahibstest')
doc_ref.set({
        'testname': 'Max',
        'testteam': 'Hibs',
        'points': 200
})
print ('this has worked')
    