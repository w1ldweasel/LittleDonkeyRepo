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


def main():
    #find out the team in question from the user (2648)
    #*currently input in this program > FIND OUT HOW TO RECIEVE INPUT FROM MN UI?*
    teamreq = 'm'
    print('\n\n')
    print("Team ID\'s are as follows:")
    print("Barnsley => 2652")
    print("Birmingham => 2631")
    print("Blackburn => 2680")
    print("Brentford => 2644")
    print("Bristol City => 2650")
    print("Cardiff => 2637")
    print("Charlton => 2663")
    print("Derby => 2642")
    print("Fulham => 2639")
    print("Huddersfield => 2622")
    print("Hull => 2633")
    print("Leeds => 2653")
    print("Luton => 2695")
    print("Middlesbrough => 2648")
    print("Millwall => 2638")
    print("Nottingham => 2634")
    print("Preston => 2643")
    print("QPR => 2645")
    print("Reading => 2647")
    print("Sheffield Wed => 2651")
    print("Stoke => 2624")
    print("Swansea => 2618")
    print("West Brom => 2625")
    print("Wigan => 2679")

    while teamreq != 'Q':
        print('\n\n')
        print("Which EFL team do you want to know the next match result for? Please enter TeamID.")
        print("Enter 'Q' to quit.")
        teamreq = input("Enter Team ID or quit request here: ")
        
        if teamreq == 'Q' or teamreq == 'q':
            break
            exit()
        elif teamreq.isdigit():
            getdata(teamreq)        
        else:
            print('That\'s not the correct format, please enter an EFL team ID')
    
 
#get data from database
def getdata(teamid):
    db = firestore.Client()

    #to get all documents in a collection, do this
#    getdoc_ref = db.collection('footballtest')
#    docs = getdoc_ref.stream()
    #getdoc_ref.get > get is depricated for collection, but not document

#    for doc in docs:
#        print('{} => {}'.format(doc.id, doc.to_dict()))
        
    #to get a specific document in a collection, do this
    getdoc2_ref = db.collection('footballtest').document(teamid)
    doc = getdoc2_ref.get()
#    print('Team info: {} {}'.format(doc.id, doc.to_dict()))
    teamdata = doc.to_dict()
#    print(teamdata)
    if teamdata == None:
        print("That's not a recognised Team ID")
    else:
        predresult = teamdata.get("result")
        teamname = teamdata.get("team name")
    
        if predresult == "win":
            print('\n\n')
            print(teamname, " are predicted to win their next match.") 
        elif predresult == "draw":
            print('\n\n')
            print(teamname, " are predicted to draw their next match.")
        elif predresult == "lose":
            print('\n\n')
            print(teamname, " are predicted to lose their next match.") 
        else:
            print('\n\n')
            print("We have no data on ", teamname, " .")
 
# ADD MORE VARIABLES AND ADD WEIGHTING
      
    
    
if __name__ == "__main__":
  main()