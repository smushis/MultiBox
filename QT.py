# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:52:53 2020

@author: Barmando
"""

from TwitterGUI import Ui_MainWindow
import threading
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class MultiBox(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()            
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
    
    def run(self):
        print("Starting " + self.name + "\n\r")  
        self.MainWindow.show()
        sys.exit(self.app.exec_())        
        
    def printTweet(self, user, text):
        self.ui.label1.setText(user + "responded to you tweet! :" + text)
        self.ui.label1.adjustSize()
        
    def printFavTweet(self, user):
        if user == "Smushis":
            self.ui.label1.setText("You liked a tweet!")
            self.ui.label1.adjustSize()            
        else:    
            self.ui.label1.setText(user + "liked your tweet! :")
            self.ui.label1.adjustSize()
            