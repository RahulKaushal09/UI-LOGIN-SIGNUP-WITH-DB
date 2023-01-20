from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from loginpage import *
from database import *
import sys

USERNAME = "agnextmohali"
PASSWORD = "Agnext"

# class Login(QDialog):
#     def __init__(self):
#         super(Login,self).__init__()
#         loadUi("loginpage.ui",self)
#         self.Submitbutton_2.clicked.connect(self.Loginfunction)



#     def Loginfunction(self):
#         Username_input = self.Username_2.text()
#         Password_input = self.Password_2.text()
#         if USERNAME == str(Username_input) and PASSWORD == str(Password_input):
#             print("right")
#         else:
#             print("wrong")
        
            








# app = QtWidgets.QApplication(sys.argv)
# uilogin=Login()
# widget=QtWidgets.QStackedWidget()
# widget.addWidget(uilogin)
# widget.show()
# widget.setFixedHeight(1000)
# widget.setFixedWidth(1000)



def loginfunction(self):
    Username_input=ui.Username_2.text()
    Password_input=ui.Password_2.text()

    check=logincheck.check(Username_input,Password_input)
    # if USERNAME == str(Username_input) and PASSWORD == str(Password_input):
    if check:
        ui.loginpage.hide()
        ui.logged.show()
        
    else:
        ui.loginpage.hide()
        ui.failed.show()


def signup(self):
    ui.loginpage.hide()
    ui.signup.show()
    
    

def submit_reg():
    register_user=ui.username_signup.text()
    register_pass=ui.password_signup.text()
    register_email=ui.email_signup.text()
    check=register(register_user,register_pass,register_email)
    if check:
        ui.signup.hide()
        ui.logged.show()
    else:
        ui.signup.hide()
        ui.logged.hide()

app = QtWidgets.QApplication(sys.argv)
      
uilogin = QtWidgets.QWidget()
ui = Ui_uilogin()
ui.setupUi(uilogin)
uilogin.show()
ui.signup_button.clicked.connect(signup)
ui.Submitbutton_2.clicked.connect(loginfunction)
ui.submit_signup.clicked.connect(submit_reg)

sys.exit(app.exec_())


# if (Submit):
#     if USERNAME == Username and PASSWORD == Password:
#         logged()
#     else:
#         failed()
