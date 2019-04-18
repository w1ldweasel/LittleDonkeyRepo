#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:54:53 2019

@author: maxinemcfarlane
"""

import requests
import json

#get the info from REST API
def champoscores():
    url = 'https://apifootball.com/api/?action=get_countries&APIkey=e7f25b27b4e1d981d76e282bf840c90dee0f243862c5ff26ad5b0775612b0583'
    r = requests.get(url)
    print(r.content)
    json_scores = json.load(url)
    print(json_scores)
    
#trying out string formatting on the API call, may be easier for updating for weekly results
  #  sdate = '2019-03-15'
   # edate = '2019-03-17'
    
 #   url2 = ('https://apifootball.com/api/?action=get_events&from=%s&to=%s&league_id=63&APIkey=e7f25b27b4e1d981d76e282bf840c90dee0f243862c5ff26ad5b0775612b0583' %(sdate, edate)) 
  #  newr = requests.get(url2)
   # print(newr.content)
    
    
 #   pointcalc()
    
#do win / draw points calculation
#still to create hometeampts etc and figure out how that will work
#def pointcalc():
 #   if match_hometeam_score > match_awayteam_score:
  #      add 3 to hometeampts
   # elif match_hometeam_score < match_awayteam_score:
    #    add 3 to awayteampts
#    elif match_hometeam_score == match_awayteam_score:
 #       add 1 to hometeampts
  #      add 1 to awayteampts

#write to D/B


if __name__ == "__main__":
    champoscores()