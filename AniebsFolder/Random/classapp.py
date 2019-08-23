# -*- coding: utf-8 -*-
"""
Created  Jun 13

@author: Anieb
"""
#Class Based WSGI Application

from wsgiref.simple_server import make_server

class WebApp:
    
    def __init__(self, environment, response):
        self.environment = environment
        self.response = response
    
    def __iter__(self):
        status = '200 OK'
        response_headers = [('content-type', 'text/html')]
        self.response(status, response_headers)

        yield b"<strong>Hello world i just built my first class based WSGI </strong>"

with make_server('', 8000, WebApp) as server:
    print ("serving on port 8000...\nVisit http://127.0.0.1:8000\nTo Kill the server enter 'control + C'")
    
    server.serve_forever()