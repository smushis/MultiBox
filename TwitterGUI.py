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
from PIL import Image
from os import path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, app):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(550, 140, 721, 351))
        self.label1.setBaseSize(QtCore.QSize(531, 261))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label1.setFont(font)
        self.label1.setStyleSheet("")
        self.label1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label1.setWordWrap(True)
        self.label1.setObjectName("label1")
        self.Photo = QtWidgets.QLabel(self.centralwidget)
        self.Photo.setGeometry(QtCore.QRect(310, 180, 201, 201))
        self.Photo.setStyleSheet("")
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap("img/Twitter/Kurisux200.png"))
        self.Photo.setObjectName("Photo")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(330, 390, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 170, 291, 281))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/twitter.png"))
        self.label.setObjectName("label")
        self.cadreTweet = QtWidgets.QLabel(self.centralwidget)
        self.cadreTweet.setGeometry(QtCore.QRect(530, -150, 761, 921))
        self.cadreTweet.setText("")
        self.cadreTweet.setPixmap(QtGui.QPixmap("img/bkgnd.png"))
        self.cadreTweet.setObjectName("cadreTweet")
        self.cadreTweet.raise_()
        self.Photo.raise_()
        self.username.raise_()
        self.label1.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
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
        self.label1.setText(_translate("MainWindow", "Results XXXXXXXX d"))
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
        self.Photo.setPixmap(QtGui.QPixmap("img/Twitter/" + data["username"] + ".png"))
        self.username.setText(data["username"])
        #self.Photo.setHidden(False)
        
    def printStreams(self,data):
        self.switchIMG("Twitch")
        self.label1.setText(data["text"])
        self.label1.adjustSize()
        self.getImage(data["url"], data["username"], "Twitch")
        self.Photo.setPixmap(QtGui.QPixmap("img/Twitch/" + data["username"]+ "200x200.png"))
        self.username.setText(data["username"])
        #self.Photo.setHidden(True)
        
    def getImage(self, url, username, web):
        size = 200, 200
        Response = requests.get(url)
        if web == "Twitter":
            img_path = "img/Twitter/" + username + ".png"
            if path.exists(img_path) == False:
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
        else:
            img_path = "img/Twitch/" + username + ".png"
            if path.exists(img_path) == False:
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
            im = Image.open("img/Twitch/" + username + ".png")
            im = im.resize(size)
            im.save("img/Twitch/" + username + "200x200.png")                
        
    
        

# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
