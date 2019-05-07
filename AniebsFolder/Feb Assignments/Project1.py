#GUI interface
import tkinter as tk
from tkinter import Button, Label, Message

import sys
import random
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
        self.master.maxsize(650,650)

    def create_widgets(self):
        self.facts = ('The standard F1 car comprises of about 80,000 components. Each car needs to be built with 100% accuracy ─ obviously!', 'The minimum weight permissible of an F1 car is 1,500 lb including the driver.', 'The F1 driver loses approximately 8lb during a race. To help them hydrate, F1 cockpits have drinking bottles installed.', 'During a race, F1 drivers experience up to 5G under braking and 3G under acceleration. As a result, F1 drivers need to develop their neck muscles in order to endure G-forces.', 'There are around 500 rules and regulations that teams have to follow – on top of international sporting codes.', 'Temperatures in the cockpit can reach around 50 degrees celsius on race day.', 'A Formula 1 car’s engine can only last, on average, about seven races. Passenger car engines usually last around ten years.', 'A DRIVER CAN SURVIVE THE IMPACT OF 100 MPH TO STANDSTILL IN 2 SECONDS', 'The winner of the first World Championship in 1950 was Italian Giuseppe Farina in his Alfa Romeo', 'During a race, a driver loses up to 4kg (8.8 lbs) of weight from sweating in the heat of the cockpit. All cockpits have a water tank for drivers, which they drink from via a pipe.')
        self.comment = ('Amazing right?', 'What an Interesting fact!')  
       
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
    

            try:
                #the below code allows the user to input a question to ask the admin
                question = input ("Please enter your Question and your email address") 
#                text_file = open("Q&A.txt", "a+")
#                text_file.write("Question: %s, \n" %(question))
#                text_file.close()
                print ('your question has been submitted please allow 24 hours for a reply')
                #the below code defines a variable called server using smtplib & gmail 
                server = smtplib.SMTP('smtp.gmail.com', 587)
                #the line below is used to initiate a secure SMTP connection 
                server.starttls()
                #the line below will retrieve the login details of the email address and password the email will be sent from
                server.login(config.EMAIL_ADDRESS, config.PASSWORD)
#                message = "subject: {}\n\n{}" .format(self)
                #the message will be the question that was inputted earlier by the user and this will be pinged accross
                message = question .format(self)
                server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
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
                #this code generates a random fact from 2 tuples above
                fun_facts = random.choice(self.facts)
                message = random.choice(self.comment)
                print("{} {}".format(fun_facts, message), file=sys.stderr)                
            
           

root = tk.Tk()
app = Application(master=root)
#below the code allows the app to remain open until the loop is broken
app.mainloop()