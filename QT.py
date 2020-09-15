# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:52:53 2020

@author: Barmando
"""

from TwitterGUI import Ui_MainWindow
import threading
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

QT_signal = pyqtSignal(str)

class MultiBox(QtCore.QThread):
    def __init__(self, name):
        QtCore.QThread.__init__(self, parent=None)
        self.name = name
    
    def run(self):
        print("Starting " + self.name + "\n\r") 
        
    def printTweet(self, user, text):
        # self.ui.label1.setText(user + "responded to you tweet! :" + text)
        # self.ui.label1.adjustSize()
        self.QT_signal.emit(user + "responded to you tweet! :" + text)
        
    def printFavTweet(self, user):
        # if user == "Smushis":
        #     self.ui.label1.setText("You liked a tweet!")
        #     self.ui.label1.adjustSize()            
        # else:    
        #     self.ui.label1.setText(user + "liked your tweet!")
        #     self.ui.label1.adjustSize()
        if user == "Smushis":
            self.QT_signal.emit("You liked a tweet!")

        else: 
            self.QT_signal.emit(user + "liked your tweet!")  
        # self.QT_signal.disconnect(a)