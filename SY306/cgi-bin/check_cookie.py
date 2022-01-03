#!/usr/bin/env python3


"""
This file is used to check whether a user exists in the
database or if a new one needs to be created


Author:
Noah Garcia-Galan
"""

import csv
import json
import mysql.connector
import os
from common_py_scripts import *





"""
Checks if a cookie exists and redirects them if they do not,
returns and error screen if user does exist, will display and error message 
before redirecting the user

Parameters:
dbconnection(connection object): A connection object for function to use
usp(string): The combined username and password in cookie format
""" 
def check_cookie(dbconnection, usp):

    user = usp.split("-")[0]
    pswd = usp.split("-")[1]

    try:

        #get connection
        mycursor = dbconnection.cursor()

        #create insert statement
        message_query = 'SELECT Username, Pass FROM Users where Username=%s AND Pass=SHA2(%s, 256);'
        mycursor.execute(message_query,(user,pswd))

        amt = 0

        for obj in mycursor:
            amt+=1

        #if user exists then go to users only message board page
        if amt > 0:
   
            print("     <head>")
            print('         <meta http-equiv="refresh" content="0;url=../messageboard.html"/>')
            print("     </head>")

        #if no such user exists then notify and take back to login page
        else: 
            print("<head>")
            print('     <meta http-equiv="refresh" content="3;url=../loginpage.html"/>')
            print("</head>")
            print('<body onload="del_cookie();">')
            print("    <h1>User Does not Exist!!! Redirecting...</h1>")
            print("</body>")
            print()
            print('<script>')
            print(' function setCookie(cname, cvalue, exdays) {')
            print('     const d = new Date();')
            print('     d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));')
            print('     let expires = "expires=" + d.toGMTString();')
            print('     document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";')    
            print('     }')
            print(' function del_cookie(){')
            print('     setCookie("UserPass","",-1);')
            print(' }')
            print('</script>')





        dbconnection.commit()

    #if user could not be added
    #most likly from already existing
    except Exception as e:
        print(e)


 

  

# Driver Code









if __name__=="__main__":
    print("Content-Type: text/html\n")              #REQUIRED!!!


    

    dbconnection = connectToDb(host="localhost", user="root", password="insert_password", \
                               database="SY306")

    cookies=getCookies()
    check_cookie(dbconnection, cookies["UserPass"])
    dbconnection.close()
    
    
