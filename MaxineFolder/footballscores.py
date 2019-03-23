#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:54:53 2019

@author: maxinemcfarlane
"""

import requests

#get the info from REST API
def premscores():
    url = 'https://apifootball.com/api/?action=get_countries&APIkey=e7f25b27b4e1d981d76e282bf840c90dee0f243862c5ff26ad5b0775612b0583'
    r = requests.get(url)
    print(r.content)
    
#trying out string formatting on the API call, may be easier for updating for weekly results
    sdate = '2016-10-30'
    edate = '2016-11-01'
    
    url2 = ('https://apifootball.com/api/?action=get_events&from=%s&to=%s&league_id=63&APIkey=e7f25b27b4e1d981d76e282bf840c90dee0f243862c5ff26ad5b0775612b0583' %(sdate, edate)) 
    newr = requests.get(url2)
    print(newr.content)
    
#do win / draw points calculation



#write to D/B


if __name__ == "__main__":
    premscores()