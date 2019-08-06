#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:38:25 2019

@author: maxinemcfarlane
"""

import json
import requests
from google.cloud import firestore
import os
import config


#function to set up API call and get data
def main():
    
    sdate = '2019-03-15'
    edate = '2019-03-17'
    key = config.footballkey
    
    footieapi = ('https://apifootball.com/api/?action=get_events&from=%s&to=%s&league_id=63&APIkey=%s' %(sdate, edate, key))
  
    r = requests.get(footieapi)
    if (r.status_code == 200):
        data = r.text
        printResults(data)
    else:
        print("Error getting football information.")


#function to parse and process data
def printResults(data):
    theJSON = json.loads(data)
    
    #if the value occurs once, do this
    if "match_hometeam_name" in theJSON:
        print (theJSON["match_hometeam_name"])
    else:
        print ('???')
     
    #if there are multiple occurences of the value (i.e. a range), do this
    for i in theJSON:
        print (i["match_hometeam_name"])
        hometeamname = (i["match_hometeam_name"]) 
        hometeamscore = (i["match_hometeam_score"])
        if (i["match_hometeam_score"]) > (i["match_awayteam_score"]):
            homeresult = "win"
        elif (i["match_hometeam_score"]) < (i["match_awayteam_score"]):
            homeresult = "lose"
        elif (i["match_hometeam_score"]) == (i["match_awayteam_score"]):
            homeresult = "draw"
        writedata(hometeamname, hometeamscore, homeresult)
        
    for i in theJSON:
        print (i["match_awayteam_name"])
        awayteamname = (i["match_awayteam_name"]) 
        awayteamscore = (i["match_awayteam_score"])
        if (i["match_awayteam_score"]) > (i["match_hometeam_score"]):
            awayresult = "win"
        elif (i["match_awayteam_score"]) < (i["match_hometeam_score"]):
            awayresult = "lose"
        elif (i["match_awayteam_score"]) == (i["match_hometeam_score"]):
            awayresult = "draw"
        writedata(awayteamname, awayteamscore, awayresult)

        
#write data to database
def writedata(team, score, result):
       
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="APIkey1.json"
    
    db = firestore.Client()
    doc_ref = db.collection('footballtest').document(team)
    
    #***NEED TO CHANGE THIS TO .UPDATE AFTER FIRST RUN, AS SET OVERWRITES DATA***
    doc_ref.set({
        'goals': score,
        'result': result
    })
    print("this has worked")
        
                
        
if __name__ == "__main__":
  main()