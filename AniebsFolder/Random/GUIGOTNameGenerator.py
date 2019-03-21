# -*- coding: utf-8 -*-
"""

@author: Anieb
"""
import tkinter as tk
import sys, random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.title("GAME OF THRONES NAME GENERATOR")
        self.master.maxsize(350,200)

    def create_widgets(self):
        #created two tuples of names one containing the first name and one containing the last
        #so that when the code is running a random name it selects two at random from the two lists below
        self.first = ('Eddard', 'Robert', 'Jaime', 'Catelyn', 'Cersei', 'Daenerys', 'Jorah', 'Viserys', 'Jon', 'Sansa', 'Arya', 'Robb', 'Theon', 'Bran', 'Joffrey', 'Sandor', 'Tyrion', 'Khal', 'Petyr', 'Davos', 'Samwell', 'Stannis', 'Jeor')
        self.last = ('Stark', 'Baratheon', 'Lannister', 'Targaryen', 'Mormont', 'Snow', 'Greyjoy', 'Clegane', 'Lannister', 'Drogo', 'Baelish', 'Bolton', 'Sparrow')
        #code below allows the button to be created to run the generator
        self.rand_name = tk.Button(self)
        self.rand_name["text"] = "GENERATE YOUR GAME OF THRONES NAME\n(click me)"
        self.rand_name["command"] = self.Generate_Name
        self.rand_name.pack(side="top")
        #code below allows the button to be created to quit
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    def Generate_Name(self):
        first_name = random.choice(self.first)
        last_name = random.choice(self.last)
        print("{} {}".format(first_name, last_name), file=sys.stderr)

root = tk.Tk()
app = Application(master=root)
app.mainloop()

"""Just testing out basic GUI code and infused it with a game of thrones generator just before the last season starts
Whats your Game of Thrones name?"""