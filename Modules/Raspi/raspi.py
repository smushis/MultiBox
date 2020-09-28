# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:18:05 2020

@author: Barmando
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import psutil
from time import sleep

class RaspiInformation(QtCore.QThread):
    raspi_signal = pyqtSignal(dict)
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
               
    def run(self):
        print("Starting " + self.name + "\n\r")
        dico = {}
        while True:
            dico["ram"] = self.get_ram()
            dico["cpu"] = self.get_cpu_usage()
            dico["temp"] = self.get_temperature()
            self.raspi_signal.emit(dico)
            sleep(1)            
        
    def get_ram(self):
        try:
            return psutil.virtual_memory().percent
        except:
            print("oups")
            return 0
        
    def get_cpu_usage(self):
        try:
            return psutil.cpu_percent()
        except:
            return 0
         
    def get_temperature(self):
        try:
            return psutil.sensors_temperatures()["cpu_thermal"][0].current
        except Exception as E:
            print(E)
            return 0    