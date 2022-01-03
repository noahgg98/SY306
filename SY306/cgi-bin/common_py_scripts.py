#!/usr/bin/env python3


import csv
import json
import mysql.connector
import os
import re

"""
This is a file of all the commonlu used python functions

Author:
Noah Garcia-Galan
"""

"""
Takes an input string from serverside
and performs the same checks and cleaning
operations as client side. Instead of rejecting the
string it will remove the potentially harmful attributes.

REGEX used similar to client side cleansing

Parameters:
str2clean(string): A string to be cleaned and returned
"""
def cleaner(str2clean):

    #define allowed chars
    allowed = "abcdefghijklmnopqrstuvwxyz!?.@0123456789"
    allowed = list(allowed)

    #limit input size
    #turn string into list
    str2clean = str2clean[0:400]
    str2clean = list(str2clean)
    cleaned = list()

    for chr in str2clean:
        if chr.lower() in allowed or chr==" ":
            cleaned.append(chr)

    return "".join(cleaned)
    



"""
Checks if a user exists and adds them to the database if they do not,
returns and error screen if user does exist

Parameters:
dbconnection(connection object): A connection object for function to use
jsonobj(json object): json object holding username and password
user(string): string of username
psw(string): string of password
"""
def getCookies():

    if 'HTTP_COOKIE' in os.environ:

        #get cookie
        cookie_string = os.environ.get('HTTP_COOKIE')

        #parse the cookies received into a dictionary

        parseCookie   = cookie_string.split(';')
        cookies       = {}

        #split cookie to get user information
        for item in parseCookie:

            if len(item.strip()) == 0:
              continue

            split=item.split('=')
            cookies[split[0].strip()] = split[1].strip()

        return cookies

    else:
      return {}


"""
Connects to the sql database and returns a connection object
that can be used to preform operations later on

Parameters:
host(string): host trying to connect
user(string): username of database
password(string): password of database
database(string): database to connect to
"""
def connectToDb(host, user, password, database):
    
    try:

        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database)

        return(mydb)			# returns DBConnection object
    except Exception as e:

        print(e, "unable to connect to database check parameters")