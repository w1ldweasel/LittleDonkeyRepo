#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:54:53 2019

@author: maxinemcfarlane
"""

import urllib.request

#scrape info from BBC sport
def premscores():
    webUrl = urllib.request.urlopen("https://www.bbc.co.uk/sport/football/premier-league/scores-fixtures/2019-03?filter=results")
    data = webUrl.read()
    print(data)


#do win / draw points calculation



#write to D/B


if __name__ == "__main__":
    premscores()