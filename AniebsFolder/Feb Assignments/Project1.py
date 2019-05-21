#GUI interface
import tkinter as tk
from tkinter import Button, Label, Message

#import sys
#import random

import re

#smtplib imported to allow use of an email function
import smtplib
#config imported for user log in details for email function to work
import config
#sqlite imported to enable use of a database
import sqlite3 as lite


class StdRedirector(tk.Frame):
    def __init__(self, text_widget):
        self.text_space = text_widget 
        
class Application(tk.Frame):
    #__init__ is used to initialize the class defined previously
    def __init__(self, master=None):
        super().__init__(master)
        #self is a naming convention and the class attributes are given the 'self' prefix and class methods are given the name'self'
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.title("Formula 1")
        self.master.maxsize(800,800)

    def create_widgets(self):
       
        self.History = tk.Button(self)
        self.History["text"] = "What is Formula 1?"
        self.History["command"] = self.F1_History 
        self.History.pack(side="top")
        
        self.WC = tk.Button(self)
        self.WC["text"] = "Formula 1 World Champions"
        self.WC["command"] = self.F1_WorldChamp
        self.WC.pack(side="top")
        
        self.Facts = tk.Button(self)
        self.Facts["text"] = "Constructors Champions"
        self.Facts["command"] = self.Constructors
        self.Facts.pack(side="top")
        
        self.PP = tk.Button(self)
        self.PP["text"] = "Top Ten Pole Sitters"
        self.PP["command"] = self.F1_Pole
        self.PP.pack(side="top")
        
        self.Facts = tk.Button(self)
        self.Facts["text"] = "Fun Facts"
        self.Facts["command"] = self.Generate_Fact
        self.Facts.pack(side="top")
        
        self.Questions = tk.Button(self)
        self.Questions["text"] = "Questions?"
        self.Questions["command"] = self.Questions_F1
        self.Questions.pack(side="top")
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

      
    
    
    
    
    def F1_History(self):
        
        #this line of code allows SQLite to connect to the database ()  
        con = lite.connect('Formula1app.db')
        
        with con:
            #this line allows the cursor to have a connection and the second line allows it to excecute * = all from the selected table
            cur = con.cursor()
            cur.execute("SELECT * FROM f1History")
            #this line allows all of the data within the table mentioned above to be fetched
            rows = cur.fetchall()
            
            #this allows the information that has been fetched above to be printed
            for row in rows:
                 print (row)
#the code below is to allow the output from the database to be printed into the GUI window and not the python Console
                 data = row
                 m = Label(text=data)
                 m.pack()
                 #button = Button(text="Clear", command=m.destroy)
                 button = Button(text="Clear", command=m.destroy)
                 button.pack()

   
       
    def F1_WorldChamp(self):
            
        con = lite.connect('Formula1app.db')
        
        with con:
        
            cur = con.cursor()
            cur.execute("SELECT * FROM driverschampions")
        
            rows = cur.fetchall()
        
            for row in rows:
                print (row)
#the code below is to allow the output from the database to be printed into the GUI window and not the python Console
                data = row
                m = Label(text=data)
                m.pack()
                button = Button(text="Clear", command=m.destroy)
                button.pack()
            
            
    def F1_Pole(self):
           
        con = lite.connect('Formula1app.db')
        
        with con:
        
            cur = con.cursor()
            cur.execute("SELECT * FROM polepositions")
        
            rows = cur.fetchall()
        
            for row in rows:
                print (row) 
            #the code below is to allow the output from the database to be printed into the GUI window and not the python Console
                data = row
                m = Label(text=data)
                m.pack()
                button = Button(text="Clear", command=m.destroy)
                button.pack()
                 
    def Questions_F1(self):

            #while True:
                try:
                #the below code allows the user to input a question to ask the admin
                    question = input ("Please enter your Question here -->")
                    email = input ("Please enter your Email address here-->")
                    
                #input validation for inputting the email address correctly
                    m = re.match('[^@]+@[^@]+\.[^@]+',email)
                    if m:
                        print("your question has been submited please allow 24 hours for a reply")
                    else:
                        print("please input the email address in the correct format")
                        
                #the below code defines a variable called server using smtplib & gmail 
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                #the line below is used to initiate a secure SMTP connection 
                    server.starttls()
                #the line below will retrieve the login details of the email address and password the email will be sent from
                    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
#                message = "subject: {}\n\n{}" .format(self)
                #the message will be the question that was inputted earlier by the user and this will be pinged accross
                    message = email .format(self)
                    message1 = question .format(self)
#                    message3 = question, email
                    server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message, message1)
                    server.quit()
                #if it is successful the message below will print if not it will print an error message notifying the user the email failed to send.
                    print ("Email sent successfully")
                except:
                    print ("Email failed to send")
    

    def Constructors(self):
        
        
        con = lite.connect('Formula1app.db')
            
        with con:
            
                cur = con.cursor()
                cur.execute("SELECT * FROM ConstructorsChampions")
            
                rows = cur.fetchall()
            
                for row in rows:
                    print (row)
        #the code below is to allow the output from the database to be printed into the GUI window and not the python Console
        
                    data = row
                    m = Message(text=data)
                    m.pack()
                button = Button(text="Clear", command=m.destroy)
                button.pack()         
                    
                
    def Generate_Fact(self):
        
        con = lite.connect('Formula1app.db')
        
        with con:
        
            cur = con.cursor()
            cur.execute("SELECT * FROM Facts")
        
            rows = cur.fetchall()
            for row in rows:
                    print (row)
                    data = row
                #this code generates a random fact from 2 tuples above
                
#        fun_facts = random.choice(self.facts)
#        message = random.choice(self.comment)
#        fact = print("{} {}".format(fun_facts, message), file=sys.stderr)  
                    
#                    data = fact
                    data = row
                    m = Message(text=data)
                    m.pack()
            button = Button(text="Clear", command=m.destroy)
            button.pack() 
            
           

root = tk.Tk()
app = Application(master=root)
#below the code allows the app to remain open until the loop is broken
app.mainloop()