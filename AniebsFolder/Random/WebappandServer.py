# -*- coding: utf-8 -*-
"""
Created Jun 12

@author: Anieb
"""
#A Basic Web Server Gateway Interface (WSGI) server implements 
#the web server side of the WSGI interface for running Python web applications.


from wsgiref.simple_server import make_server #python package for WSGI 

#simple web app
#APP = flask.Flask(__name__)

#below is the web app function called web_app
def web_app(response):

    status = '200 OK' #The HTTP 200 OK success status response code indicates that the request has succeeded.
    headers = [('content-type', 'text/html; charset=utf-8')]#this is apart of the response to see what type of information it is whether its a html doc or a text doc
    response(status, headers)
    
    return [b'<strong>Hello World I just created my Web Server Gateway Interface (WSGI) </strong>']# this is to return information on the app

#    <html>
#        <head>
#            <title>Home Page - Anieb's Home Page</title>
#        </head>
#        <body>
#            <h1> Hello World I just created my first WSGI </h1>
#        </body>
#    </html>

with make_server('', 8000, web_app) as server:# ('' is the local host, 8000 is the port this will be hosted on, web_app this is added so the server knows what to display )
    print ("serving on port 8000...\nVisit http://127.0.0.1:8000\nTo stop the server enter 'control + C'")
    
    server.serve_forever()#this method will run the server until manually stopped
    
if __name__ == '__main__':
#    APP.debug=True
   web_app.run()