from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import sqlite3


import os

if os.path.exists("login.db"):
    con = sqlite3.connect("login.db")
    cur=con.cursor()
    pass

else:
    con = sqlite3.connect("login.db")
    cur=con.cursor()    
    cur.execute('CREATE TABLE IF NOT EXISTS login (username TEXT, password TEXT,email TEXT)')



class logincheck():
    def check(username,password):
        cur.execute("SELECT * FROM login WHERE username =? AND password =?",(username,password))
        name=bool(cur.fetchone())
        return name
        
def register(username,password,email):
    cur.execute('INSERT INTO login (username,password,email) VALUES(?,?,?)',(username,password,email))
    if(cur.rowcount>0):
        print ("Signup Done")
    else:
        print ("Signup Error")
    con.commit()
    return 1

