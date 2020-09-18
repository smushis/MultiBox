# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:59:11 2020

@author: Barmando
"""


import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class htmlServ(QtCore.QThread):
    host  = "0.0.0.0"
    port = 22220
    
    def __init__(self, threadID, name, app):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
        self.app = app
        
    def run(self):
        print("Starting " + self.name + "\n\r")
        self.app.run(host=self.host, port=self.port)
    