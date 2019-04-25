#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:52:48 2019

@author: maxinemcfarlane
"""

from google.cloud import firestore
import os

#*** NEED TO FIGURE OUT AUTHORISE STEP *** 
#default_app = firebase_admin.initialize_app()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/maxinemcfarlane/Downloads/APIkey1.json"

db = firestore.Client()

test_ref = db.collection(u'test')
docs = test_ref.get()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))