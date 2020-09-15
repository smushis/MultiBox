# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultiBox.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from twitter import Twitter
from twitch import Twitch
from html_serv import htmlServ
from PyQt5 import QtCore, QtGui, QtWidgets

import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, app):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-image: url(img/steins.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(630, 170, 531, 261))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.Photo = QtWidgets.QLabel(self.centralwidget)
        self.Photo.setGeometry(QtCore.QRect(340, 190, 201, 201))
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap("img/Twitter/Kurisux200.png"))
        self.Photo.setObjectName("Photo")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(370, 410, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 160, 301, 271))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/twitter.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        self.app = app
        
    def switchIMG(self, state):
        if state == "Twitch":
            self.label.setPixmap(QtGui.QPixmap("img/twitch.png"))
        else:
            self.label.setPixmap(QtGui.QPixmap("img/twitter.png"))            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Results XXXXXXXXXXXXXXXXXXXXXXX"))
        self.username.setText(_translate("MainWindow", "TextLabel"))
        
    def launchTwitterThread(self):
        self.twitter_thread = Twitter(3, "Twitter Thread")
        self.twitter_thread.twitter_signal.connect(self.printTweet)
        self.twitter_thread.start()
        return self.twitter_thread
    
    def launchTwitchThread(self):
        self.twitch_thread = Twitch(3, "Twitch Thread")
        self.twitch_thread.twitch_signal.connect(self.printStreams)
        self.twitch_thread.start()
        return self.twitch_thread  
    
    def launchHTMLThread(self):
        self.HTML_thread = htmlServ(3, "HTML Thread", self.app)
        self.HTML_thread.start()
        return self.HTML_thread     

    def printTweet(self, data):
        self.switchIMG("Twitter")
        self.label1.setText(data["text"])
        self.label1.adjustSize()
        self.getImage(data["url"], data["username"], "Twitter")
        self.Photo.setPixmap(QtGui.QPixmap("img/Twitter/" + data["username"]))
        self.username.setText(data["username"])
        #self.Photo.setHidden(False)
        
    def printStreams(self,data):
        self.switchIMG("Twitch")
        self.label1.setText(data)
        self.label1.adjustSize()
        #self.Photo.setHidden(True)
        
    def getImage(self, url, username, web):
        Response = requests.get(url)
        if web == "Twitter":
            file = open("img/Twitter/" + username + ".png", "wb")
            file.write(Response.content)
            file.close()
        else:
            file = open("img/Twitch/" + username + ".png", "wb")
            file.write(Response.content)
            file.close()                
        
    
        

# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
