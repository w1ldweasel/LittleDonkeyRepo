# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11


"""
import mysql.connector #this is imported to allow the connection to be established with the DB

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Threat123",
      database="threatsolution")#this is to ensure the connection is created and pointing to this Database so when tables are created they are loaded to this DB
# this mydb instance will contain the host the username password and DB to establish the connection to the correct location

mycursor = mydb.cursor()# this is an object that communicates with the MYSQL server 

mycursor.execute("CREATE DATABASE threatsolution") #this is how the database is created followed with the name you wish to save the DB as

mycursor.execute("SHOW DATABASES")#this is the code to display the database

for db in mycursor: #this will display all of the DB's created in MYSQL
    print(db)

mycursor.execute("CREATE TABLE threatlibrary (Characteristics VARCHAR(50), CharacteristicGuidance VARCHAR(255), Threat VARCHAR(255), ThreatDescription VARCHAR(255), Requirement VARCHAR(255), AssuranceRequirement VARCHAR(255))")#this allows us to make the table called drivers_WC with 2 variables name and championships these will act as collumns
mycursor.execute("SHOW TABLES")#this will display the tables within DB to check everything has been loaded correctly
for tb in mycursor:
    print(tb)#this will display all of the Tables's created in MYSQL for this DB
    
    
sqlFormula = """INSERT INTO threatlibrary (Characteristics, CharacteristicGuidance, Threat, ThreatDescription, Requirement, AssuranceRequirement) VALUES (%s, %s, %s, %s, %s, %s)""" #this command will allow us to insert into the specific table and columns with placeholders %s this can be replaced by any value we want
threatlibrary = [("The system is a mobile application", "a mobile device which can be removed from LBG premises", "staff may missuse systems to exfiltrate data from the bank", "the application may allow a legitimate user to exfiltrate data from LBG. for examplea mobile application that allows LBG content to be downloaded onto a smartphone harddrive.", "data should be classified in lline with LBG classification policy", "Evidence may be provided to support the operation of data loss prevention controls e.g. screenshots")]#tuple one will insert the two values as specified above into the correct columns.
                
mycursor.executemany(sqlFormula, threatlibrary)#executemany will allow more than one record to be updated

mydb.commit()#this will push the update to the DB

mycursor.fetchall()#this is the code to display the database

for db in mycursor:
    print(db)

