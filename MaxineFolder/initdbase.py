#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:43:44 2019

@author: maxinemcfarlane
"""

#*** figure out how this works ***
#*** add comments so can easily change program to init any databases ***

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {'football-data-python-project': project_id,})
    
db = firestore.client()

    