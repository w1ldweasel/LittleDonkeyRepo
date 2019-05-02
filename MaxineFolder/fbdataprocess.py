#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:52:48 2019

@author: maxinemcfarlane
"""

from google.cloud import firestore
import os

#default_app = firebase_admin.initialize_app()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="APIkey1.json"

#get data from database
def getdata():
    db = firestore.Client()

    test_ref = db.collection(u'test')
    docs = test_ref.get()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    

#process data
#average score, how many wins/draws
#*** TO BE UPDATED ***

    
    
    
#write data to database
#THIS WILL WRITE TO A NEW COLLECTION
#*** TO BE UPDATED ***
def writedata():

    db = firestore.Client()
    doc_ref = db.collection(u'test').document(u'thisisafinaltest')
    doc_ref.set({
        u'testname': u'Max4',
        u'testteam': u'Man City',
        u'points': 80
    })
    print("this has worked")
    
    
if __name__ == "__main__":
    getdata()