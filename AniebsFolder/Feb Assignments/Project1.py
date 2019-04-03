import tkinter as tk
import sys
import random
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
          
       print ("""
               
Formula One is the highest class of single-seater auto racing sanctioned 
by the Fédération Internationale de l'Automobile and owned by the Formula One Group. 
The FIA Formula One World Championship has been one of the premier forms of racing 
                                         around the world since its inaugural season in 1950. 
Current champion: Lewis Hamilton 
Drivers: 20
Drivers' champion: Lewis Hamilton; (5th title)
Constructors' champion: Mercedes; (5th title)
Did you know: Formula One ranks 10th among professional sports leagues in the world by revenue (1,830 € million)               
        
        """)
       
    def F1_WorldChamp(self):
            
            print ("""  
                   
    FORMULA 1 WORLD CHAMPIONS
              
    7 World Titles 
    Michael Schumacher 
                       
    5 World Titles
    Juan Manuel Fangio
    Lewis Hamilton (Current World Champion)
                      
    4 World Titles
    Alain Prost
    Sebastian Vettel
                      
    3 World Titles
    Jack Brabham
    Jackie Stewart-
    Niki Lauda
    Nelson Piquet
    Ayrton Senna
                      
    2 World Titles
    Alberto Ascari
    Jim Clark
    Graham Hill
    Emerson Fittipaldi
    Mika Hakkinen
    Fernando Alonso
                      
    1 World Titles
    Nino Farina
    Mike Hawthorn
    Phil Hill
    John Surtees
    Denny Hulme
    Jochen Rindt
    James Hunt
    Mario Andretti
    Jody Scheckter
    Alan Jones
    Keke Rosberg
    Nigel Mansell
    Damon Hill
    Jaques Villeneuve
    Kimi Raikkonen
    Jenson Button
    Nico Rosberg 
    
    
    """)
            
    def F1_Pole(self):
            print("""
                  
        ****Top 10 Pole Sitters****
                  
        1- Lewis Hamilton        84
        2- Michael Schumacher    68
        3- Aryton Senna          65
        4- Sebastian Vettel      55
        5- Jim Clark             33
        5- Alain Prost           33
        7- Nigel Mansell         32
        8- Nico Rosberg          30
        9- Juan Manuel Fangio    29
        10- Mika Hakkinen        26
                  
                  """)
    def Questions_F1(self):
        
#        while True:
#            try:
                question = input ("Please enter your Question and your email address") 
                text_file = open("Q&A.txt", "a+")
                text_file.write("Question: %s, \n" %(question))
                text_file.close()
                print ('your question has been submitted please allow 24 hours for a reply')
#                break
#            except ValueError:
#                print ("That isn't the correct format please try again")
#                
    def Constructors(self):
          print("""
        
        *** FORMULA 1 CONSTRUCTORS WORLD CHAMPIONS ***
               CONSTRUCTOR | NUMBER OF TITLES
                FERRARI    |         16
                WILLIAMS   |         9
                McLAREN    |         8
                LOTUS      |         7
                MERCEDES   |         5
                RED BULL   |         4
                COOPER     |         2
                BRABHAM    |         2
                RENAULT    |         2
                VANWALL    |         1
                BRM        |         1
                MATRA      |         1
                TYRRELL    |         1
                BENETTON   |         1
                BRAWN      |         1
               
               
                  
            """)
           
    def Generate_Fact(self):
            fun_facts = random.choice(self.facts)
            message = random.choice(self.comment)
            print("{} {}".format(fun_facts, message), file=sys.stderr)
    
           

root = tk.Tk()
app = Application(master=root)
app.mainloop()