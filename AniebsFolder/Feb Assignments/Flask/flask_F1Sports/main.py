# -*- coding: utf-8 -*-
"""
Created on Sat Sep 5

"""


from flask import Flask, render_template
import mysql.connector # by importing this driver it allows the connection to be established to the MySQL database

#the code below establishes a connection with the MYSQL server
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Admin",
      database="f1db"#this is to ensure the connection is created and pointing to this database
        
        )

app = Flask(__name__)

		

@app.route('/index')#@app.route is a decorator a way to extend the functionality of python in this case to route the 
def index():
    return render_template("index.html") #Instead of returning hardcode HTML from the function, a HTML file can be rendered by the render_template() function

@app.route('/WhatIsFormula1')
def home():
    return render_template("home.html")

@app.route('/WorldChamps')
def about():
#this line allows the cursor to have a connection and the second line allows it to excecute * = all from the selected table
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM driver_wc")
 #this line allows all of the data within the table mentioned above to be fetched
    myresult = mycursor.fetchall()
#once the connection above is made and the information is retrived from the database table  below
#the return function will allow the render_template to direct the route to the specified URL this also alows us to
#assign a variable to the result retrieved from the databse.
    return render_template("about.html", data=myresult)

@app.route('/admin')
def admin():
    return render_template("admin.html")
#    if request.form['password'] == 'password' and request.form['username'] == 'admin':
#        session['logged_in'] = True
#    else:
#        flash('wrong password!')
#    return render_template("index.html")


if __name__ == '__name__':
    app.run(debug=True) 

app.run(port=8000)

