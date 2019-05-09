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

    #to get all documents in a collection, do this
    getdoc_ref = db.collection(u'footballtest')
    docs = getdoc_ref.stream()
    #getdoc_ref.get > get is depricated

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
        
    #to get a specific document in a collection, do this
    getdoc2_ref = db.collection(u'footballtest').document(u'Hull City')

    doc = getdoc2_ref.get()
    print(u'Team info: {} {}'.format(doc.id, doc.to_dict()))
    
    procdata()
 

#process the data
#average score, how many wins/draws, trends
def procdata():
    

    
    
    
#write processed data to database
#THIS WILL WRITE TO A NEW COLLECTION OR MAYBE SAME DOCUMENT. 1 DOC PER TEAM? NOT DECIDED
#*** TO BE UPDATED ***
#def writedata():
#
#    db = firestore.Client()
#    doc_ref = db.collection(u'test').document(u'thisisafinaltest')
#    doc_ref.update({
#        u'testname': u'Max4',
#        u'testteam': u'Man City',
#        u'points': 80
#    })
#    print("this has worked")
    
    
if __name__ == "__main__":
  getdata()