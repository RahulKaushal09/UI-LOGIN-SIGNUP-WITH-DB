from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import sqlite3


# app = Flask(__name__)
# # change to name of your database; add path if necessary
# db_name = 'login.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# # this variable, db, will be used for all SQLAlchemy commands
# db = SQLAlchemy(app)

import os

if os.path.exists("login.db"):
    con = sqlite3.connect("login.db")
    cur=con.cursor()
    pass

else:
    con = sqlite3.connect("login.db")
    cur=con.cursor()    
    cur.execute('CREATE TABLE IF NOT EXISTS login (username TEXT, password TEXT,email TEXT)')

# log = input("1 to signup , 2 to login")



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


# signup('rahul','rahul123','rahul@gmail.com')
# if log =="1":
#     username=str(input("enter username"))
#     password=str(input("enter password"))
#     cur.execute('INSERT INTO login (username,password) VALUES(?,?)',(username,password))
#     if(cur.rowcount>0):
#         print ("Signup Done")
#     else:
#         print ("Signup Error")
#     con.commit()
# elif log =="2":
#     username=input("enter username")
#     password=input("enter password")
#     cur.execute("SELECT * FROM login WHERE username =? AND password =?",(username,password))
#     # if(cur.fetchone()):


    
# else:
#     log=input("please enter 1 or 2 ")














# @app.route('/')
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text


# if __name__ == '__main__':
#     app.run(debug=True)


# class creatinguser(db.Model):

#     id = db.Column( db.Interger , primary_key=true )
#     username = db.column(db.String(80) , unique=true,nullable=False)
#     email = db.column(db.string(120), unique=true,nullable=False)

#     def __init__(self,username,email):
#         self.username = username
#         self.email = email
    
#     def __repr__(self):
#         return 'user{}'.format(username)

# admin = creatinguser(user_admin,user_admin@gmail.com)
