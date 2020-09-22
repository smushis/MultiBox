# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:33:08 2020

@author: Barmando
"""

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from time import sleep

class Weather(QtCore.QThread):
    weather_signal = pyqtSignal(dict)
    
    API_Key = "de0ab0351733baf5bbca5bf3f0c86072"
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    #List of city ID http://bulk.openweathermap.org/sample/city.list.json.gz
    city_id = "2980291" #Saint Etienne
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
               
    def run(self):
        self.getWeatherData(self.API_Key, self.city_id)
            
    def getWeatherData(self, API_Key, city_id):
       while True:     
            final_url = self.base_url + "appid=" + API_Key + "&id=" + city_id + "&units=metric"
            try:
                weather_data = requests.get(final_url).json()
            except:
                print("Problem during getting weather info")
                break
            if len(weather_data['weather']) > 1:
                weather = weather_data["weather"][0]["main"]
            else:
                weather = weather_data["weather"]["main"]
            url_icon = self.getWeatherIcon(weather)
            temp = weather_data["weather"]["main"]["temp"]
            dico = self.createDict(url_icon, temp, weather)
            self.weather_signal.emit(dico)
            sleep(60)
            
    def getWeatherIcon(self, w):
        weather = w.lower()
        if weather == "clear sky":
            url = "http://openweathermap.org/img/wn/01d@2x.png"
        elif weather == "few clouds":
            url = "http://openweathermap.org/img/wn/02d@2x.png"            
        elif weather == "scattered clouds":
            url = "http://openweathermap.org/img/wn/03d@2x.png"    
        elif weather == "broken clouds":
            url = "http://openweathermap.org/img/wn/04d@2x.png"    
        elif weather == "shower rain":
            url = "http://openweathermap.org/img/wn/09d@2x.png"
        elif weather == "rain":
            url = "http://openweathermap.org/img/wn/10d@2x.png"    
        elif weather == "thunderstorm":
            url = "http://openweathermap.org/img/wn/11d@2x.png"    
        elif weather == "snow":
            url = "http://openweathermap.org/img/wn/13d@2x.png"    
        elif weather == "mist":
            url = "http://openweathermap.org/img/wn/50d@2x.png"  
        return url
              
    def createDict(self, icon_url, temp, w_type):
        dico = {}
        dico["icon_url"] = icon_url
        dico["type"] = w_type
        dico["temp"] = temp
        return dico
    

