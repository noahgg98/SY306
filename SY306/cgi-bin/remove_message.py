#!/usr/bin/env python3

"""
This file interfaces with messageboard.html
to remove a message based on message text and
message id. Will only remove one message at a time


Author:
Noah Garcia-Galan
"""

import csv
import cgi
import json
import mysql.connector
from common_py_scripts import *

"""
Removes a message from the database
so that it is no longer displayed

Parameters:
dbconnection(connection object): A connection object for function to use
message(string): string of the message to be deleted
username(string): string of the username associated with the message
"""
def remove_mesg(dbconnection, message, username, uid):

     


    try:

        #get connection
        mycursor = dbconnection.cursor()

        #create insert statement
        if username == "Admin":
            message_query = "DELETE FROM Messages WHERE Mesg='%s' and MesgID = '%d';"\
            %(message, uid)
        else:
            message_query = "DELETE FROM Messages WHERE Mesg='%s' and Username='%s' and MesgID = '%d';"\
            %(message, username, uid)

        #execute the statement
        mycursor.execute(message_query)
        dbconnection.commit()

    #if user could not be added
    #most likly from already existing
    except Exception as e:
        print(e, ' Unable to remove message!\n','\nClick the back button to try again!\n')


# Driver Code
if __name__=="__main__":
    print("Content-Type: text/html\n")              #REQUIRED!!!

    form    = cgi.FieldStorage()
    message = form['message'].value
    uid = int(form['id'].value)

    user = getCookies()["UserPass"].split("-")[0]

    

    dbconnection = connectToDb(host="localhost", user="root", password="insert_password", \
                               database="SY306")


    remove_mesg(dbconnection, message=message, username=user, uid=uid)
    dbconnection.close()
    print (json.dumps({}))  