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
    
    API_Key = ""
    
    base_url = "http://api.openweathermap.org/data/2.5/onecall?"
    
    #List of city ID http://bulk.openweathermap.org/sample/city.list.json.gz
    city_lon = "4.411363" #Saint Etienne
    city_lat = "45.409149"
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
               
    def run(self):
        print("Starting " + self.name + "\n\r")
        self.readAPIKey()
        self.getWeatherData(self.API_Key)

    def readAPIKey(self):
        with open("Modules/Weather/key.txt", 'r') as file:
            key = file.read()
        #print(str(key))
        self.API_Key = str(key)
            
    def getWeatherData(self, API_Key):
       while True:     
            final_url = self.base_url + "appid=" + API_Key + "&lat=" + self.city_lat + "&lon=" + self.city_lon + "&exclude=minutely,hourly,alerts" +"&units=metric"
            try:
                weather_data = requests.get(final_url).json()
                weather_today_data = weather_data["current"]
                weather_week = weather_data["daily"]
                # print(weather_data)
            except:
                print("Problem during getting weather info")
                break
            # print(weather_today)
            ID_today = weather_today_data["weather"][0]["id"]
            weather_today = weather_today_data["weather"][0]["description"]
            url_icon_today = self.getWeatherIcon(ID_today)
            temp_today = "{:.1f}°C".format(weather_today_data["temp"])
            dico_today = self.createDict(url_icon_today, temp_today, weather_today)
            self.weather_signal.emit(dico_today)
            
            self.sendWeatherWeekly(weather_week)
                    
            sleep(600)
            
    def sendWeatherFromDay(self, data, day=1):
        weather = data[day]
        ID_tom = weather["weather"][0]["id"] 
        weather_tom = weather["weather"][0]["description"]
        url_icon_tom  = self.getWeatherIcon(ID_tom )
        temp_tom  = "{:.1f}°C".format(weather["temp"]["day"])            
        dico_tom = self.createDict(url_icon_tom, temp_tom, weather_tom, day)
        self.weather_signal.emit(dico_tom)
        
    def sendWeatherWeekly(self, data):
        for i in range(6):
            self.sendWeatherFromDay(data, i+1)
  
            
    def getWeatherIcon(self, ID):
        if ID == 800 :
            url = "http://openweathermap.org/img/wn/01d@4x.png"
        elif ID == 801:
            url = "http://openweathermap.org/img/wn/02d@4x.png"            
        elif ID == 802:
            url = "http://openweathermap.org/img/wn/03d@4x.png"    
        elif ID == (803|804):
            url = "http://openweathermap.org/img/wn/04d@4x.png"    
        elif (ID >= 300 & ID <= 321) | (ID >= 520 & ID <= 531):
            url = "http://openweathermap.org/img/wn/09d@4x.png"
        elif (ID >= 500 & ID <= 504):
            url = "http://openweathermap.org/img/wn/10d@4x.png"    
        elif (ID >= 200 & ID <= 232):
            url = "http://openweathermap.org/img/wn/11d@4x.png"    
        elif (ID == 511) | (ID >= 600 & ID <= 622):
            url = "http://openweathermap.org/img/wn/13d@4x.png"    
        elif (ID >= 701 & ID <= 781):
            url = "http://openweathermap.org/img/wn/50d@4x.png"
        else:
            print("Not identified ID")
            url = None
        return url
              
    def createDict(self, icon_url, temp, w_type, day="today"):
        dico = {}
        dico["icon_url"] = icon_url
        dico["type"] = w_type
        dico["temp"] = temp
        dico["day"] = day
    
        return dico
    

