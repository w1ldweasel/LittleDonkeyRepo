# -*- coding: utf-8 -*-
"""

@author: Anieb
"""

def menu():
    
    print("************MAIN MENU**************")
    print("******Formula 1 Stats & Facts******")
    
    print()
    
choice = input("""
A: Formula 1 World Champions
B: Top Ten Pole Sitters
C: Constructors Champions
D: 
E: Quit

Please enter your choice: """)
        

        
if choice == "A" or choice =="a":
        print ("""  
               
           *** FORMULA 1 WORLD CHAMPIONS ***
          
                  7 World Titles 
                  Michael Schumacher 
                   
                  5 World Titles
                  Juan Manuel Fangio
                  Lewis Hamilton**
                  
                  4 World Titles
                  Alain Prost
                  Sebastian Vettel
                  
                  3 World Titles
                  Jack Brabham
                  Jackie Stewart
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
                  Nico Rosberg """)
           

        
elif choice == "B" or choice =="b":
        print("""
                 ****Top 10 Pole Sitters****
                  
                 1- Lewis Hamilton        83
                 2- Michael Schumacher    68
                 3- Aryton Senna          65
                 4- Sebastian Vettel      55
                 5- Jim Clark             33
                 5- Alain Prost           33
                 7- Nigel Mansell         32
                 8- Nico Rosberg          30
                 9- Juan Manuel Fangio    29
                10- Mika Hakkinen         26
                  
                  """)
elif choice == "C" or choice =="c":
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
elif choice=="D" or choice=="d":
        print("")
elif choice=="E" or choice=="e":
            exit
            
else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")


