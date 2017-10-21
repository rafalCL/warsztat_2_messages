'''
Created on 20 paź 2017

@author: Edu
'''

from mysql.connector import connect

def connect_to_db(db_name):
    cnx = connect(user="root", password="", host="localhost", database=db_name)
    cnx.autocommit = True
    return cnx