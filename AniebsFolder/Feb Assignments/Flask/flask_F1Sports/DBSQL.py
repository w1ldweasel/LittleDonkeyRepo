# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11


"""

import mysql.connector #this is imported to allow the connection to be established with the DB

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="admin",
      database="f1db"#this is to ensure the connection is created and pointing to this Database so when tables are created they are loaded to this DB
        
        )# this mydb instance will contain the host the username password and DB to establish the connection to the correct location

mycursor = mydb.cursor()# this is an object that communicates with the MYSQL server 

mycursor.execute("CREATE DATABASE f1db") #this is how the database is created followed with the name you wish to save the DB as

mycursor.execute("SHOW DATABASES")#this is the code to display the database

for db in mycursor: #this will display all of the DB's created in MYSQL
    print(db)

mycursor.execute("CREATE TABLE driver_wc (name VARCHAR(50), Championships VARCHAR(255))")#this allows us to make the table called drivers_WC with 2 variables name and championships these will act as collumns
mycursor.execute("SHOW TABLES")#this will display the tables within DB to check everything has been loaded correctly
for tb in mycursor:
    print(tb)#this will display all of the Tables's created in MYSQL for this DB
    
    
sqlFormula = "INSERT INTO accounts (Name, Championships) VALUES (%s, %s)" #this command will allow us to insert into the specific table and columns with placeholders %s this can be replaced by any value we want
driver_wc = [("Micheal Schumacher", 7),#tuple one will insert the two values as specified above into the correct columns.
            ("Juan Manuel Fangio", 5),
            ("Lewis Hamilton", 5),
            ("Alain Prost", 4),
            ("Sebastian Vettel", 4),
            ("Jack Brabham", 3),
            ("Jackie Stewart", 3),
            ("Niki Lauda", 3),
            ("Nelson Piquet", 3),
            ("Ayrton Senna", 3),
            ("ALberto Ascari", 2),
            ("Graham Hill", 2),
            ("Jim Clark", 2),
            ("Emerson Fittipaldi", 2),
            ("Mika Hakkinen", 2),
            ("Fernando Alonso", 2),]

mycursor.executemany(sqlFormula, driver_wc)#executemany will allow more than one record to be updated

mydb.commit()#this will push the update to the DB

mycursor.fetchall()#this is the code to display the database

for db in mycursor:
    print(db)
#
