#!/usr/bin/env python3



"""
This file is a very simple file
It takes in a message from messageboard html with
the field storage and saves it to the database. All 
informaton is cleaned by the regulatory measures of 
the valid params in message board

Author:
Noah Garcia-Galan
"""

import csv
import json
import mysql.connector
from common_py_scripts import *

"""
Retrievs all messages from the sql database and store them in a json object
the json object is then dumped back to messageboard 

Parameters:
dbgconnection(connection object): A connection object for function to use
"""
def make_json(dbconnection):

     

    # create a dictionary
    data = {}


    try:

        #get connection
        mycursor = dbconnection.cursor()

        #create insert statement
       
        message_query = 'SELECT MesgID, Mesg, Username, TmStamp FROM Messages ORDER BY MesgID DESC;'
        mycursor.execute(message_query)
        

        #loop through items returned by the db
        for (MesgID, Mesg, Username, TmStamp) in mycursor:

            mesgObj = {}
            
            #convert time to string
            dt = TmStamp.strftime("%d-%b-%Y (%H:%M:%S)")

            #mesgObj = {"ID": %s, "User": %s, "Message": %s, "Date": %s}\
                    #%(MesgID, Mesg, Username, dt)


            #Create internal dictionary structure
            mesgObj["ID"]      = "%s"%(MesgID)
            mesgObj["User"]    = "%s"%(Username)
            mesgObj["Message"] = "%s"%(Mesg)
            mesgObj["Date"]    = "%s"%(dt)

            key = str(MesgID)
            data[key] = mesgObj
          




        dbconnection.commit()

    #if user could not be added
    #most likly from already existing
    except Exception as e:
        print(e, ' Unable to add you!\n','\nClick the back button to try again!\n')


 

    print (json.dumps(data))       


# Driver Code





if __name__=="__main__":
    print("Content-Type: text/html\n")              #REQUIRED!!!


    

    dbconnection = connectToDb(host="localhost", user="root", password="insert_password", \
                               database="SY306")


    make_json(dbconnection)
    dbconnection.close()

"""
#allows for messages to be posted 
        #by date order
        #for some reason ORDER BY was 
        #not working
        index = 0
        objlist = objlist[::-1]
        for key in keyholder:
            mesgObj = objlist[index]
            data[key] = mesgObj
            index+=1
          
"""