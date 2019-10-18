# -*- coding: utf-8 -*-
"""
Created on Sat Sep 5

"""


from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import mysql.connector # by importing this driver it allows the connection to be established to the MySQL database



#the code below establishes a connection with the MYSQL server
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Threat123",
      database="threatsolution"#this is to ensure the connection is created and pointing to this database
        
        )
mycursor = mydb.cursor()

app = Flask(__name__)

app.secret_key = "Flask123" #this is an encryption key for the secret key variable for the session created when the user logs in it prevents someone accessing from the client side

def login_required(f):# this to ensure the page that requires a log in will only be accessible if a logged in session is valid
    @wraps(f)
    def wrap(*args, **kwargs):#*args is used to pass a variable number of arguments to a function, **kwargs is used to pass a keyworded variable length argument list. **double star allows us to pass through keyword arguments
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('you need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/home')#@app.route is a decorator a way to extend the functionality of python in this case to route the 
def home():
    return render_template("home.html")#Instead of returning hardcode HTML from the function, a HTML file can be rendered by the render_template() function

@app.route('/admin', methods = ['POST', 'GET'])
@login_required#this decorator will ensure when a GET request is sent and there is no logged in session key it will redirect to the log in page and flash a message so the user can log in.
def admin():

    
    if request.method == "POST":  
        Characteristics = request.form['Characteristics']
        CharacteristicGuidance = request.form['CharacteristicGuidance']
        Threat = request.form['Threat']
        ThreatDescription = request.form['ThreatDescription']
        Requirement = request.form['Requirement']
        AssuranceRequirement = request.form['AssuranceRequirement']
        #the command below will allow us to insert into the specific table and columns with placeholders %s this can be replaced by any value we want
        mycursor.executemany("INSERT INTO threatlibrary (Characteristics, CharacteristicGuidance, Threat, ThreatDescription, Requirement, AssuranceRequirement) VALUES (%s, %s, %s, %s, %s, %s)", (Characteristics, CharacteristicGuidance, Threat, ThreatDescription, Requirement, AssuranceRequirement))
        mydb.connection.commit()#commit to the DB
        return redirect(url_for('admin'))
    
    return render_template("admin.html")


@app.route('/ThreatSolution', methods = ['GET', 'POST'])
def Threatsolution():
    
#this line allows the cursor to have a connection and the second line allows it to excecute * = all from the selected table
#    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM threatlibrary")
 #this line allows all of the data within the table mentioned above to be fetched
    threatlibrary = mycursor.fetchall()
    
#once the connection above is made and the information is retrived from the database table  below
#the return function will allow the render_template to direct the route to the specified URL this also alows us to
#assign a variable to the result retrieved from the databse.
    return render_template("ThreatSolution.html", data=threatlibrary)
   
    
@app.route('/login', methods = ['GET', 'POST']) #methods by default in flask are GET methods so when another method is required 
# it needs to be added into the methods POST will allow the end user to send a post request to this login end point in this case \login
def login():
    error = None #this is rendering an error message to send across to the login html page
    if request.method == 'POST':
        if request.form['username'] != 'pass' or request.form['password'] != 'pass':# this shows if the password and username don't match then it will display an error message
            error = 'invalid credentials. please try again.'
        else:
            session['logged_in'] = True # if the users credentials are correct the value true is a sign to confirm log in
            flash('you are now logged in')
            return redirect(url_for('admin')) #this is the page that the login page will redirect too
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():

    session.pop('logged_in', None)#when a get request is sent over to logout it will replace the logged in session from TRUE to NONE to close the session and delete the key
    flash('you are now logged out')
    return redirect(url_for('login'))#once the session is invalidated it will redirect to the following


if __name__ == '__name__':
    app.run(debug=True) 

app.run(port=8000)

