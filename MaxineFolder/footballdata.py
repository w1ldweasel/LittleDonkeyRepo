#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:38:25 2019

@author: maxinemcfarlane
"""

import json
import urllib.request
from google.cloud import firestore
import os
import config


#function to set up API call and get data
#*** LOOK AT CHANGING THIS FROM URLLIB.REQUEST TO REQUESTS (BETTER FOR API)*** 
def main():
    
    sdate = '2019-03-15'
    edate = '2019-03-17'
    key = config.footballkey
    
    footieurl = ('https://apifootball.com/api/?action=get_events&from=%s&to=%s&league_id=63&APIkey=%s' %(sdate, edate, key))
  
    webUrl = urllib.request.urlopen(footieurl)
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Error getting football information.")


#function to parse and process data
def printResults(data):
    theJSON = json.loads(data)
    
    # * if the value occurs once, do this
    if "match_hometeam_name" in theJSON:
        print (theJSON["match_hometeam_name"])
    else:
        print ('???')
     
    # * if there are multiple occurences of the value (i.e. a range), do this
    for i in theJSON:
        print (i["match_hometeam_name"])
        
        
    writedata()
        
        
#write data to database
def writedata():
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="APIkey1.json"
    
    db = firestore.Client()
    doc_ref = db.collection(u'test').document(u'testingmultipleentries')
    doc_ref.set({
        u'testname': u'Klopp',
        u'testteam': u'Liverpool',
        u'points': 50
#        u'testname': u'Pep',
#        u'testteam': u'Man City',
#        u'points': 55,
#        u'testname': u'Silva',
#        u'testteam': u'Everton',
#        u'points': 30
    })
    print("this has worked")
        
                
        
if __name__ == "__main__":
  main()