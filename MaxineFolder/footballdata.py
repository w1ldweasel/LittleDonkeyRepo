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
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/maxinemcfarlane/Downloads/APIkey1.json"
    
    db = firestore.Client()
    doc_ref = db.collection(u'test').document(u'thisisafinaltest')
    doc_ref.set({
        u'testname': u'Max4',
        u'testteam': u'Man City',
        u'points': 80
    })
    print("this has worked")
        
                
        
if __name__ == "__main__":
  main()