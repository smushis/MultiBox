# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:45:04 2020

@author: Barmando
"""
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
import adafruit_dht
import board
from time import sleep

class DHT11(QtCore.QThread):
    DHT11_signal = pyqtSignal(str)
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
        self.dhtDevice = adafruit_dht.DHT11(board.D18)
        
    def run(self):
        while True:
            try:
                temp_c = self.dhtDevice.temperature
                self.DHT11_signal.emit("{:.1f}°C".format(temp_c))
                print("{:.1f}°C".format(temp_c))
            except RuntimeError as error:    
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                sleep(2)
                continue
            except Exception as error:
                self.dhtDevice.exit()
                raise error                
            sleep(2)