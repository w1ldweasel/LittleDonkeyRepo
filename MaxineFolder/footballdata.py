#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:38:25 2019

@author: maxinemcfarlane
"""

import json
import urllib.request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import firestore


#function to set up API call and get data
#*** LOOK AT CHANGING THIS FROM URLLIB.REQUEST TO REQUESTS (BETTER FOR API)*** 
def main():
    sdate = '2019-03-15'
    edate = '2019-03-17'
    
    footieurl = ('https://apifootball.com/api/?action=get_events&from=%s&to=%s&league_id=63&APIkey=e7f25b27b4e1d981d76e282bf840c90dee0f243862c5ff26ad5b0775612b0583' %(sdate, edate))
    
    webUrl = urllib.request.urlopen(footieurl)
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Error getting football information.")


#function to parse and process data
def printResults(data):
    theJSON = json.loads(data)
    
    # * if the value occurs once, do theis
    if "match_hometeam_name" in theJSON:
        print (theJSON["match_hometeam_name"])
    else:
        print ('???')
     
    # * if there are multiple occurences of the value (i.e. a range), do this
    for i in theJSON:
        print (i["match_hometeam_name"])
        
        
#write data to database
def writedata():
#*** NEED TO FIGURE OUT INITIALIZE / AUTHORISE STEP ***
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {'football-data-python-project': project_id,})
    
    db = firestore.Client()
    doc_ref = db.collection(u'test').document(u'thisisatest')
    doc_ref.set({
        u'testname': u'Max',
        u'testteam': u'Hibs',
        u'points': 80
    })
        
                
        
if __name__ == "__main__":
  main()