#!/usr/bin/env python3

"""
This file is used to add a new user to the 
database. It interfaces with the signup.html
form fields to clean and insert the data

Author:
Noah Garcia-Galan
"""

import cgi
import html
import mysql.connector
import json
import time
from common_py_scripts import *


"""
Checks if a user exists and adds them to the database if they do not,
returns and error screen if user does exist

Parameters:
dbconnection(connection object): A connection object for function to use
jsonobj(json object): json object holding username and password
user(string): string of username
psw(string): string of password
"""
def add_user(dbconnection, jsonobj, user, psw):

    myJson = json.loads(jsonobj)
    exist = False

    try:

        #get connection
        checker  = dbconnection.cursor()
        mycursor = dbconnection.cursor()

        #get all user items from db
        userQuery = 'SELECT * FROM Users;'
        checker.execute(userQuery)

        #loop through and see if user already exists
        for ( unm, name, pswd, permission) in checker:
            if (unm == user):
                exist = True

        #show error screen if user exists
        if exist:
            print("User Already Exist!!")
            show_error_screen()
            
        else:
            #create insert statement
            insertQuery = 'INSERT INTO Users(Username, NameReal, Pass) VALUES (%s, %s, SHA2(%s,256))'

            mycursor.execute(insertQuery, (myJson['Username'], myJson['NameReal'], myJson['Pass']))
            print("<head>")
            print('     <meta http-equiv="refresh" content="3;url=../loginpage.html"/>')
            print("</head>")
            print("<h1> ACCOUNT CREATED ! </h1>")
            print("<br><br><a href='../loginpage.html'>Go to Login Page</a>")
            dbconnection.commit()

    #if user could not be added
    #most likly from already existing
    except Exception as e:
        print('Unable to add you!\n','\nClick the back button to try again!\n')
        show_error_screen()

"""
setups the initial screen to be shown
"""
def show_screen():
    print("Content-Type: text/html\n")				#REQUIRED!!!
    print('<!doctype html><title>Hello There!</title>')
    print('<head> <script type="text/javascript" src="../common_scripts.js"></script></head>')
    print('<body onload="to_add_user();">')
    print("</body>")


        
    print ("</html>")

"""
show an error message and redirect user if bad input occurs
"""
def show_error_screen():
    
    print("<!doctype html>")
    print("<title>Hello There!</title><body>")
    print("<head>")
    print('     <meta http-equiv="refresh" content="3;url=../signup.html"/>')
    print("</head>")
    print("<br><br><a href='../signup.html'>Go Back!</a>")
    print ("</body></html>")


if __name__=="__main__":
    show_screen()
    #create form field
    form = cgi.FieldStorage()


    #grab needed information from form
    #should already be clean but just in case clean again
    name     = cleaner(html.escape(form['name'].value))
    user     = cleaner(html.escape(form['user'].value))
    password = cleaner(html.escape(form['pass'].value))


    # driver code - read from client side - stringified object
    jobj = '{"Username":"%s", "NameReal":"%s", "Pass":"%s"}'\
            %(user, name, password)

    dbconnection = connectToDb(host="localhost", user="root", password="insert_password", \
                               database="SY306")

    add_user(dbconnection=dbconnection, jsonobj=jobj, user=user, psw=password)

    dbconnection.close()