#!/usr/bin/env python3

"""
This file allows a user to add a message to the
database. The message is the immediately displayed on
the message board.

Author:
Noah Garcia-Galan
"""

import sys
import json
import cgi
import csv
import html
import mysql.connector
from datetime import datetime
from common_py_scripts import *

"""
Checks if a user exists and adds them to the database if they do not,
returns and error screen if user does exist

Parameters:
dbconnection(connection object): A connection object for function to use
jsonobj(json object): json object holding username and message
"""
def insertMsgIntoDb(dbconnection, jsonobj):

    #load the json object
    myJson = json.loads(jsonobj)

    try:

        #get connection
        mycursor = dbconnection.cursor()

        #create insert statement
        #NEEDED --> INSERT INTO Messages(Mesg, Username) VALUES ("aa","aa");
        insertQuery = 'INSERT INTO Messages(Mesg, Username) VALUES (%s,%s)'

        #parameterized queries
        mycursor.execute(insertQuery,(myJson['Mesg'], myJson['Username']))
        dbconnection.commit()

    #if user could not be added
    #most likly from already existing
    except Exception as e:
        print(e, 'Unable to add message!\n','\nClick the back button to try again!\n')
    
    dbconnection.close()
  
       


if __name__=='__main__':
    
    print("Content-Type: text/html\n")              #REQUIRED!!!

    #get element and write to messages file
    form = cgi.FieldStorage()

    #get message and username of message
    #using cookie for username prevents direct access to
    #adding messages without being logged in 
    message = cleaner(html.escape(form['message'].value))
    user = getCookies()["UserPass"].split("-")[0]
    
    # driver code - read from client side - stringified object
    jobj = '{"Username":"%s", "Mesg":"%s"}'\
            %(user.strip(), message.strip())

    dbconnection = connectToDb(host="localhost", user="root", password="insert_password", \
                               database="SY306")

    insertMsgIntoDb(dbconnection=dbconnection, jsonobj=jobj)


    dbconnection.close()
    print(json.dumps({}))

    """
    MesgID int NOT NULL AUTO_INCREMENT,
    Mesg VARCHAR(255) NOT NULL,
    Username VARCHAR(255) NOT NULL,
    TmStamp DateTime NOT NULL,
    """


    
 
