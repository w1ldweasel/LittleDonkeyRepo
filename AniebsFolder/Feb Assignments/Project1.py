import tkinter as tk
import sys
import random
import smtplib
import config
import sqlite3 as lite
#import Tkinter
#from tkinter import * 


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.title("Formula 1")
        self.master.maxsize(400,400)

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
          
        con = lite.connect('Formula1app.db')
        
        with con:
        
            cur = con.cursor()
            cur.execute("SELECT * FROM f1History")
        
            rows = cur.fetchall()
        
            for row in rows:
                print (row)      
            
       
    def F1_WorldChamp(self):
            
        con = lite.connect('Formula1app.db')
        
        with con:
        
            cur = con.cursor()
            cur.execute("SELECT * FROM driverschampions")
        
            rows = cur.fetchall()
        
            for row in rows:
                print (row)      
            
            
    def F1_Pole(self):
           
        con = lite.connect('Formula1app.db')
        
        with con:
        
            cur = con.cursor()
            cur.execute("SELECT * FROM polepositions")
        
            rows = cur.fetchall()
        
            for row in rows:
                print (row)      
            
                 
    def Questions_F1(self):
    

            try:
                question = input ("Please enter your Question and your email address") 
                text_file = open("Q&A.txt", "a+")
                text_file.write("Question: %s, \n" %(question))
                text_file.close()
                print ('your question has been submitted please allow 24 hours for a reply')
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(config.EMAIL_ADDRESS, config.PASSWORD)
                message = "subject: {}\n\n{}" .format(self)
                server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
                server.quit()
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
            
         
    def Generate_Fact(self):
            fun_facts = random.choice(self.facts)
            message = random.choice(self.comment)
            print("{} {}".format(fun_facts, message), file=sys.stderr)
    
           

root = tk.Tk()
app = Application(master=root)
app.mainloop()