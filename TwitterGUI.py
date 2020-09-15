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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, app):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1550, 1002)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/twitter.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 1, 1, 1)
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button1.setFont(font)
        self.Button1.setObjectName("Button1")
        self.gridLayout.addWidget(self.Button1, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1550, 26))
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
            print("Twitch img")
            self.label.setPixmap(QtGui.QPixmap("img/twitch.png"))
        else:
            print("Twitter img")
            self.label.setPixmap(QtGui.QPixmap("img/twitter.png"))            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Results"))
        self.Button1.setText(_translate("MainWindow", "TWEETOS"))
        
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
        self.label1.setText(data)
        self.label1.adjustSize()
        
    def printStreams(self,data):
        self.switchIMG("Twitch")
        self.label1.setText(data)
        self.label1.adjustSize()
                
        
    
        

# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
