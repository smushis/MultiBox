# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignGUI2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from Modules.Twitter.twitter import Twitter
from Modules.Twitch.twitch import Twitch
from Modules.Listener.html_serv import htmlServ
from Modules.Spotify.spotify import Spotify
from Modules.Weather.weather import Weather
from Modules.Youtube.youtube import Youtube
from Modules.Raspi.raspi import RaspiInformation
from Modules.GUI.clock import AnalogClock
from Modules.GameTracker.tracker import GameTracker

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, Qt, QPoint
from PyQt5.QtWidgets import QVBoxLayout, QLabel 
from PyQt5.QtGui import QColor, QPainter, QPolygon
import requests
import io
import psutil
from PIL import Image
from PIL import ImageCms
from os import path
from time import sleep
import os
from datetime import date
from datetime import timedelta
from pynput.keyboard import Listener
from pynput.keyboard import Key

from constants import TEMP_ON

if TEMP_ON:
    from Modules.Temperature.Temperature import DHT11  

class Ui_MainWindow(object): 
    
    hourHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -40)
    ])

    minuteHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -70)
    ])

    hourColor = QColor(127, 0, 127)
    minuteColor = QColor(0, 127, 127, 191)
    
    def setupUi(self, MainWindow, app):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.data_1 = QtWidgets.QLabel(self.centralwidget)
        self.data_1.setGeometry(QtCore.QRect(980, 40, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_1.setFont(font)
        self.data_1.setWordWrap(True)
        self.data_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.data_1.setObjectName("data_1")
        self.Twitch_Title = QtWidgets.QLabel(self.centralwidget)
        self.Twitch_Title.setGeometry(QtCore.QRect(980, 110, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Twitch_Title.setFont(font)
        self.Twitch_Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Twitch_Title.setWordWrap(True)
        self.Twitch_Title.setObjectName("Twitch_Title")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(0, 0, 1451, 721))
        self.BG.setText("")
        self.BG.setPixmap(QtGui.QPixmap("img/TwitchBG.png"))
        self.BG.setObjectName("BG")
        self.media = QtWidgets.QLabel(self.centralwidget)
        self.media.setGeometry(QtCore.QRect(490, 190, 331, 291))
        self.media.setStyleSheet("border: 10px double blue;")
        self.media.setText("")
        self.media.setAlignment(QtCore.Qt.AlignCenter)
        self.media.setObjectName("media")
        self.img_album = QtWidgets.QLabel(self.centralwidget)
        self.img_album.setGeometry(QtCore.QRect(40, 540, 151, 151))
        self.img_album.setText("")
        self.img_album.setPixmap(QtGui.QPixmap("img/kurisux150.png"))
        self.img_album.setObjectName("img_album")
        self.titleMusic = QtWidgets.QLabel(self.centralwidget)
        self.titleMusic.setGeometry(QtCore.QRect(260, 568, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)        
        self.titleMusic.setFont(font)
        self.titleMusic.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.titleMusic.setWordWrap(True)
        self.titleMusic.setObjectName("titleMusic")
        self.artistMusic = QtWidgets.QLabel(self.centralwidget)
        self.artistMusic.setGeometry(QtCore.QRect(260, 610, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.artistMusic.setFont(font)
        self.artistMusic.setWordWrap(True)
        self.artistMusic.setObjectName("artistMusic")
        self.cadreAlbum = QtWidgets.QLabel(self.centralwidget)
        self.cadreAlbum.setGeometry(QtCore.QRect(10, 500, 191, 211))
        self.cadreAlbum.setText("")
        self.cadreAlbum.setPixmap(QtGui.QPixmap("img/spot.png"))
        self.cadreAlbum.setObjectName("cadreAlbum")
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(30, 230, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.temp.setFont(font)
        self.temp.setAlignment(QtCore.Qt.AlignCenter)
        self.temp.setObjectName("temp")
        self.humi = QtWidgets.QLabel(self.centralwidget)
        self.humi.setGeometry(QtCore.QRect(20, 270, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.humi.setFont(font)
        self.humi.setAlignment(QtCore.Qt.AlignCenter)
        self.humi.setObjectName("humi")
        self.IconWeather_1 = QtWidgets.QLabel(self.centralwidget)
        self.IconWeather_1.setGeometry(QtCore.QRect(20, 60, 91, 81))
        self.IconWeather_1.setText("")
        self.IconWeather_1.setPixmap(QtGui.QPixmap("img/10d@4x.png"))
        self.IconWeather_1.setAlignment(QtCore.Qt.AlignCenter)
        self.IconWeather_1.setObjectName("IconWeather_1")
        self.tempExte = QtWidgets.QLabel(self.centralwidget)
        self.tempExte.setGeometry(QtCore.QRect(10, 130, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempExte.setFont(font)
        self.tempExte.setAlignment(QtCore.Qt.AlignCenter)
        self.tempExte.setObjectName("tempExte")
        self.weatherBG = QtWidgets.QLabel(self.centralwidget)
        self.weatherBG.setGeometry(QtCore.QRect(0, 40, 871, 161))
        self.weatherBG.setText("")
        self.weatherBG.setPixmap(QtGui.QPixmap("img/GUI2/Weather_bg.png"))
        self.weatherBG.setObjectName("weatherBG")
        self.homeBG = QtWidgets.QLabel(self.centralwidget)
        self.homeBG.setGeometry(QtCore.QRect(0, 200, 151, 131))
        self.homeBG.setText("")
        self.homeBG.setPixmap(QtGui.QPixmap("img/GUI2/home_temp_bg.png"))
        self.homeBG.setObjectName("homeBG")
        self.notfis = QtWidgets.QLabel(self.centralwidget)
        self.notfis.setGeometry(QtCore.QRect(850, 10, 451, 701))
        self.notfis.setText("")
        self.notfis.setPixmap(QtGui.QPixmap("img/GUI2/Notifs.png"))
        self.notfis.setObjectName("notfis")
        self.cadreNotifs_1 = QtWidgets.QLabel(self.centralwidget)
        self.cadreNotifs_1.setGeometry(QtCore.QRect(854, 20, 415, 170))
        self.cadreNotifs_1.setText("")
        self.cadreNotifs_1.setPixmap(QtGui.QPixmap("img/GUI2/tweet_like.png"))
        self.cadreNotifs_1.setObjectName("cadreNotifs_1")
        self.cadreNotifs_2 = QtWidgets.QLabel(self.centralwidget)
        self.cadreNotifs_2.setGeometry(QtCore.QRect(854, 192, 415, 170))
        self.cadreNotifs_2.setText("")
        self.cadreNotifs_2.setPixmap(QtGui.QPixmap("img/GUI2/tweet_like.png"))
        self.cadreNotifs_2.setObjectName("cadreNotifs_2")
        self.cadreNotifs_3 = QtWidgets.QLabel(self.centralwidget)
        self.cadreNotifs_3.setGeometry(QtCore.QRect(854, 361, 415, 170))
        self.cadreNotifs_3.setText("")
        self.cadreNotifs_3.setPixmap(QtGui.QPixmap("img/GUI2/tweet_like.png"))
        self.cadreNotifs_3.setObjectName("cadreNotifs_3")
        self.cadreNotifs_4 = QtWidgets.QLabel(self.centralwidget)
        self.cadreNotifs_4.setGeometry(QtCore.QRect(854, 530, 415, 170))
        self.cadreNotifs_4.setText("")
        self.cadreNotifs_4.setPixmap(QtGui.QPixmap("img/GUI2/tweet_like.png"))
        self.cadreNotifs_4.setObjectName("cadreNotifs_4")
        self.buttonIMG_1 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonIMG_1.setGeometry(QtCore.QRect(1200, 130, 44, 44))
        self.buttonIMG_1.setStyleSheet("background-image: url(:/bg/img.png); background-color: rgba(255, 255, 255, 0);")
        self.buttonIMG_1.setText("")
        self.buttonIMG_1.setObjectName("buttonIMG_1")
        self.date_1 = QtWidgets.QLabel(self.centralwidget)
        self.date_1.setGeometry(QtCore.QRect(17, -5, 111, 61))
        self.clock = AnalogClock(self.centralwidget)
        self.clock.setGeometry(QtCore.QRect(540, 206, 18, 180))
        self.clock.setObjectName("clock")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.date_1.setFont(font)
        self.date_1.setObjectName("date_1")
        self.date_2 = QtWidgets.QLabel(self.centralwidget)
        self.date_2.setGeometry(QtCore.QRect(135, -5, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.date_2.setFont(font)
        self.date_2.setObjectName("date_2")
        self.date_3 = QtWidgets.QLabel(self.centralwidget)
        self.date_3.setGeometry(QtCore.QRect(255, -5, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.date_3.setFont(font)
        self.date_3.setObjectName("date_3")
        self.date_4 = QtWidgets.QLabel(self.centralwidget)
        self.date_4.setGeometry(QtCore.QRect(376, -5, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.date_4.setFont(font)
        self.date_4.setObjectName("date_4")
        self.date_5 = QtWidgets.QLabel(self.centralwidget)
        self.date_5.setGeometry(QtCore.QRect(495, -5, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.date_5.setFont(font)
        self.date_5.setObjectName("date_5")
        self.date_6 = QtWidgets.QLabel(self.centralwidget)
        self.date_6.setGeometry(QtCore.QRect(615, -5, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.date_6.setFont(font)
        self.date_6.setObjectName("date_6")
        self.date_7 = QtWidgets.QLabel(self.centralwidget)
        self.date_7.setGeometry(QtCore.QRect(737, -5, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.date_7.setFont(font)
        self.date_7.setObjectName("date_7")
        self.tempExte_2 = QtWidgets.QLabel(self.centralwidget)
        self.tempExte_2.setGeometry(QtCore.QRect(130, 130, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempExte_2.setFont(font)
        self.tempExte_2.setAlignment(QtCore.Qt.AlignCenter)
        self.tempExte_2.setObjectName("tempExte_2")
        self.IconWeather_2 = QtWidgets.QLabel(self.centralwidget)
        self.IconWeather_2.setGeometry(QtCore.QRect(140, 60, 91, 81))
        self.IconWeather_2.setText("")
        self.IconWeather_2.setPixmap(QtGui.QPixmap("img/10d@4x.png"))
        self.IconWeather_2.setAlignment(QtCore.Qt.AlignCenter)
        self.IconWeather_2.setObjectName("IconWeather_2")
        self.tempExte_3 = QtWidgets.QLabel(self.centralwidget)
        self.tempExte_3.setGeometry(QtCore.QRect(250, 130, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempExte_3.setFont(font)
        self.tempExte_3.setAlignment(QtCore.Qt.AlignCenter)
        self.tempExte_3.setObjectName("tempExte_3")
        self.IconWeather_3 = QtWidgets.QLabel(self.centralwidget)
        self.IconWeather_3.setGeometry(QtCore.QRect(260, 60, 91, 81))
        self.IconWeather_3.setText("")
        self.IconWeather_3.setPixmap(QtGui.QPixmap("img/10d@4x.png"))
        self.IconWeather_3.setAlignment(QtCore.Qt.AlignCenter)
        self.IconWeather_3.setObjectName("IconWeather_3")
        self.tempExte_4 = QtWidgets.QLabel(self.centralwidget)
        self.tempExte_4.setGeometry(QtCore.QRect(370, 130, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempExte_4.setFont(font)
        self.tempExte_4.setAlignment(QtCore.Qt.AlignCenter)
        self.tempExte_4.setObjectName("tempExte_4")
        self.IconWeather_4 = QtWidgets.QLabel(self.centralwidget)
        self.IconWeather_4.setGeometry(QtCore.QRect(380, 60, 91, 81))
        self.IconWeather_4.setText("")
        self.IconWeather_4.setPixmap(QtGui.QPixmap("img/10d@4x.png"))
        self.IconWeather_4.setAlignment(QtCore.Qt.AlignCenter)
        self.IconWeather_4.setObjectName("IconWeather_4")
        self.tempExte_5 = QtWidgets.QLabel(self.centralwidget)
        self.tempExte_5.setGeometry(QtCore.QRect(490, 130, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempExte_5.setFont(font)
        self.tempExte_5.setAlignment(QtCore.Qt.AlignCenter)
        self.tempExte_5.setObjectName("tempExte_5")
        self.IconWeather_5 = QtWidgets.QLabel(self.centralwidget)
        self.IconWeather_5.setGeometry(QtCore.QRect(500, 60, 91, 81))
        self.IconWeather_5.setText("")
        self.IconWeather_5.setPixmap(QtGui.QPixmap("img/10d@4x.png"))
        self.IconWeather_5.setAlignment(QtCore.Qt.AlignCenter)
        self.IconWeather_5.setObjectName("IconWeather_5")
        self.tempExte_7 = QtWidgets.QLabel(self.centralwidget)
        self.tempExte_7.setGeometry(QtCore.QRect(610, 130, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempExte_7.setFont(font)
        self.tempExte_7.setAlignment(QtCore.Qt.AlignCenter)
        self.tempExte_7.setObjectName("tempExte_7")
        self.IconWeather_7 = QtWidgets.QLabel(self.centralwidget)
        self.IconWeather_7.setGeometry(QtCore.QRect(620, 60, 91, 81))
        self.IconWeather_7.setText("")
        self.IconWeather_7.setPixmap(QtGui.QPixmap("img/10d@4x.png"))
        self.IconWeather_7.setAlignment(QtCore.Qt.AlignCenter)
        self.IconWeather_7.setObjectName("IconWeather_7")
        self.tempExte_9 = QtWidgets.QLabel(self.centralwidget)
        self.tempExte_9.setGeometry(QtCore.QRect(730, 130, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempExte_9.setFont(font)
        self.tempExte_9.setAlignment(QtCore.Qt.AlignCenter)
        self.tempExte_9.setObjectName("tempExte_9")
        self.IconWeather_9 = QtWidgets.QLabel(self.centralwidget)
        self.IconWeather_9.setGeometry(QtCore.QRect(740, 60, 91, 81))
        self.IconWeather_9.setText("")
        self.IconWeather_9.setPixmap(QtGui.QPixmap("img/10d@4x.png"))
        self.IconWeather_9.setAlignment(QtCore.Qt.AlignCenter)
        self.IconWeather_9.setObjectName("IconWeather_9")
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(150, 210, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.date.setFont(font)
        self.date.setObjectName("label")
        self.cadreMusic = QtWidgets.QLabel(self.centralwidget)
        self.cadreMusic.setGeometry(QtCore.QRect(190, 520, 411, 151))
        self.cadreMusic.setText("")
        self.cadreMusic.setPixmap(QtGui.QPixmap("img/GUI2/music.png"))
        self.cadreMusic.setObjectName("cadreMusic")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(160, 270, 121, 51))
        self.lcdNumber.setStyleSheet("")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setObjectName("lcdNumber")
        self.spot_play = QtWidgets.QPushButton(self.centralwidget)
        self.spot_play.setGeometry(QtCore.QRect(310, 660, 52, 52))
        self.spot_play.setObjectName("spot_play")
        self.spot_play.setStyleSheet("background-color: rgba(255, 255, 255, 0); background-image: url(img/GUI2/play.png);")
        self.spot_forward = QtWidgets.QPushButton(self.centralwidget)
        self.spot_forward.setGeometry(QtCore.QRect(400, 660, 52, 52))
        self.spot_forward.setObjectName("spot_forward")
        self.spot_forward.setStyleSheet("background-color: rgba(255, 255, 255, 0); background-image: url(img/GUI2/forward.png);")
        self.spot_back = QtWidgets.QPushButton(self.centralwidget)
        self.spot_back.setGeometry(QtCore.QRect(220, 660, 52, 52))
        self.spot_back.setObjectName("spot_back")
        self.spot_back.setStyleSheet("background-color: rgba(255, 255, 255, 0); background-image: url(img/GUI2/backward.png);")
        self.img_PP_1 = QtWidgets.QLabel(self.centralwidget)
        self.img_PP_1.setGeometry(QtCore.QRect(890, 65, 91, 101))
        self.img_PP_1.setText("")
        self.img_PP_1.setPixmap(QtGui.QPixmap("img/GUI2/kurisux100.png"))
        self.img_PP_1.setObjectName("img_PP_1")
        self.buttonIMG_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonIMG_2.setGeometry(QtCore.QRect(1200, 305, 44, 44))
        self.buttonIMG_2.setStyleSheet("background-image: url(:/bg/img.png); background-color: rgba(255, 255, 255, 0);")
        self.buttonIMG_2.setText("")
        self.buttonIMG_2.setObjectName("buttonIMG_2")
        self.data_2 = QtWidgets.QLabel(self.centralwidget)
        self.data_2.setGeometry(QtCore.QRect(980, 210, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_2.setFont(font)
        self.data_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.data_2.setWordWrap(True)
        self.data_2.setObjectName("data_2")
        self.img_PP_2 = QtWidgets.QLabel(self.centralwidget)
        self.img_PP_2.setGeometry(QtCore.QRect(890, 240, 91, 101))
        self.img_PP_2.setText("")
        self.img_PP_2.setPixmap(QtGui.QPixmap("img/GUI2/kurisux100.png"))
        self.img_PP_2.setObjectName("img_PP_2")
        self.Twitch_Title_2 = QtWidgets.QLabel(self.centralwidget)
        self.Twitch_Title_2.setGeometry(QtCore.QRect(980, 280, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Twitch_Title_2.setFont(font)
        self.Twitch_Title_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Twitch_Title_2.setWordWrap(True)
        self.Twitch_Title_2.setObjectName("Twitch_Title_2")
        self.buttonIMG_3 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonIMG_3.setGeometry(QtCore.QRect(1200, 475, 44, 44))
        self.buttonIMG_3.setStyleSheet("background-image: url(:/bg/img.png); background-color: rgba(255, 255, 255, 0);")
        self.buttonIMG_3.setText("")
        self.buttonIMG_3.setObjectName("buttonIMG_3")
        self.data_3 = QtWidgets.QLabel(self.centralwidget)
        self.data_3.setGeometry(QtCore.QRect(980, 380, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_3.setFont(font)
        self.data_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.data_3.setWordWrap(True)
        self.data_3.setObjectName("data_3")
        self.img_PP_3 = QtWidgets.QLabel(self.centralwidget)
        self.img_PP_3.setGeometry(QtCore.QRect(890, 410, 91, 101))
        self.img_PP_3.setText("")
        self.img_PP_3.setPixmap(QtGui.QPixmap("img/GUI2/kurisux100.png"))
        self.img_PP_3.setObjectName("img_PP_3")
        self.Twitch_Title_3 = QtWidgets.QLabel(self.centralwidget)
        self.Twitch_Title_3.setGeometry(QtCore.QRect(980, 450, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Twitch_Title_3.setFont(font)
        self.Twitch_Title_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Twitch_Title_3.setWordWrap(True)
        self.Twitch_Title_3.setObjectName("Twitch_Title_3")
        self.buttonIMG_4 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonIMG_4.setGeometry(QtCore.QRect(1200, 640, 44, 44))
        self.buttonIMG_4.setStyleSheet("background-image: url(:/bg/img.png); background-color: rgba(255, 255, 255, 0);")
        self.buttonIMG_4.setText("")
        self.buttonIMG_4.setObjectName("buttonIMG_4")
        self.data_4 = QtWidgets.QLabel(self.centralwidget)
        self.data_4.setGeometry(QtCore.QRect(980, 550, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_4.setFont(font)
        self.data_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.data_4.setWordWrap(True)
        self.data_4.setObjectName("data_4")
        self.img_PP_4= QtWidgets.QLabel(self.centralwidget)
        self.img_PP_4.setGeometry(QtCore.QRect(890, 575, 91, 101))
        self.img_PP_4.setText("")
        self.img_PP_4.setPixmap(QtGui.QPixmap("img/GUI2/kurisux100.png"))
        self.img_PP_4.setObjectName("img_PP_4")
        self.Twitch_Title_4 = QtWidgets.QLabel(self.centralwidget)
        self.Twitch_Title_4.setGeometry(QtCore.QRect(980, 620, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Twitch_Title_4.setFont(font)
        self.Twitch_Title_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Twitch_Title_4.setWordWrap(True)
        self.Twitch_Title_4.setObjectName("Twitch_Title_4")
        self.raspi_temp = QtWidgets.QLabel(self.centralwidget)
        self.raspi_temp.setGeometry(QtCore.QRect(0, 450, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.raspi_temp.setFont(font)
        self.raspi_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.raspi_temp.setObjectName("raspi_temp")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 350, 171, 41))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.516717 rgba(102, 46, 166, 211), stop:1 rgba(255, 255, 255, 255));")
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 400, 171, 41))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.516717 rgba(102, 46, 166, 211), stop:1 rgba(255, 255, 255, 255));")
        self.raspi_ram_2 = QtWidgets.QLabel(self.centralwidget)
        self.raspi_ram_2.setGeometry(QtCore.QRect(4, 350, 181, 41))
        self.raspi_ram_2.setAlignment(QtCore.Qt.AlignCenter)
        self.raspi_ram_2.setObjectName("raspi_ram_2")
        self.raspi_cpu_2 = QtWidgets.QLabel(self.centralwidget)
        self.raspi_cpu_2.setGeometry(QtCore.QRect(10, 400, 171, 41))
        self.raspi_cpu_2.setAlignment(QtCore.Qt.AlignCenter)
        self.raspi_cpu_2.setObjectName("raspi_cpu_2") 
        self.cadreDataRaspi = QtWidgets.QLabel(self.centralwidget)
        self.cadreDataRaspi.setGeometry(QtCore.QRect(-5, 340, 280, 161))
        self.cadreDataRaspi.setText("")
        self.cadreDataRaspi.setPixmap(QtGui.QPixmap("img/GUI2/data_raspi.png"))
        self.cadreDataRaspi.setObjectName("cadreDataRaspi")
        self.cadreClock = QtWidgets.QLabel(self.centralwidget)
        self.cadreClock.setGeometry(QtCore.QRect(160, 250, 171, 91))
        self.cadreClock.setText("")
        self.cadreClock.setPixmap(QtGui.QPixmap("img/GUI2/clock.png"))
        self.cadreClock.setObjectName("cadreClock") 
        self.stats = QtWidgets.QLabel(self.centralwidget)
        self.stats.setGeometry(QtCore.QRect(520, 510, 311, 211))
        self.stats.setText("")
        self.stats.setPixmap(QtGui.QPixmap("img/GUI2/spotify_stats.png"))
        self.stats.setObjectName("stats")
        self.stat_song = QtWidgets.QLabel(self.centralwidget)
        self.stat_song.setGeometry(QtCore.QRect(680, 580, 140, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stat_song.setFont(font)
        self.stat_song.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.stat_song.setObjectName("stat_song") 
        self.stats_artist = QtWidgets.QLabel(self.centralwidget)
        self.stats_artist.setGeometry(QtCore.QRect(530, 580, 131, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stats_artist.setFont(font)
        self.stats_artist.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.stats_artist.setObjectName("stats_artist") 
        self.rank_rl_1 = QtWidgets.QLabel(self.centralwidget)
        self.rank_rl_1.setGeometry(QtCore.QRect(384, 390, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rank_rl_1.setFont(font)
        self.rank_rl_1.setObjectName("rank_rl_1")
        self.cadreRL = QtWidgets.QLabel(self.centralwidget)
        self.cadreRL.setGeometry(QtCore.QRect(270, 340, 211, 171))
        self.cadreRL.setText("")
        self.cadreRL.setPixmap(QtGui.QPixmap("img/GUI2/RL_ranks.png"))
        self.cadreRL.setObjectName("cadreRL")
        self.rl_3v3 = QtWidgets.QLabel(self.centralwidget)
        self.rl_3v3.setGeometry(QtCore.QRect(280, 360, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.rl_3v3.setFont(font)
        self.rl_3v3.setObjectName("rl_3v3")
        self.rl_2v2 = QtWidgets.QLabel(self.centralwidget)
        self.rl_2v2.setGeometry(QtCore.QRect(280, 430, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.rl_2v2.setFont(font)
        self.rl_2v2.setObjectName("rl_2v2")
        self.rl_rank_img_1 = QtWidgets.QLabel(self.centralwidget)
        self.rl_rank_img_1.setGeometry(QtCore.QRect(380, 350, 61, 51))
        self.rl_rank_img_1.setText("")
        self.rl_rank_img_1.setPixmap(QtGui.QPixmap("img/GUI2/RL/diamond3.png"))
        self.rl_rank_img_1.setObjectName("rl_rank_img_1")
        self.rl_rank_img_2 = QtWidgets.QLabel(self.centralwidget)
        self.rl_rank_img_2.setGeometry(QtCore.QRect(380, 430, 61, 51))
        self.rl_rank_img_2.setText("")
        self.rl_rank_img_2.setPixmap(QtGui.QPixmap("img/GUI2/RL/diamond3.png"))
        self.rl_rank_img_2.setObjectName("rl_rank_img_2")
        self.rank_rl_2 = QtWidgets.QLabel(self.centralwidget)
        self.rank_rl_2.setGeometry(QtCore.QRect(385, 470, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rank_rl_2.setFont(font)
        self.rank_rl_2.setObjectName("rank_rl_2")
        self.raspi_cpu_img = QtWidgets.QLabel(self.centralwidget)
        self.raspi_cpu_img.setGeometry(QtCore.QRect(200, 399, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.raspi_cpu_img.setFont(font)
        self.raspi_cpu_img.setText("")
        self.raspi_cpu_img.setPixmap(QtGui.QPixmap("img/GUI2/cpu.png"))
        self.raspi_cpu_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.raspi_cpu_img.setObjectName("raspi_cpu_img")
        self.raspi_ram_img = QtWidgets.QLabel(self.centralwidget)
        self.raspi_ram_img.setGeometry(QtCore.QRect(200, 346, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.raspi_ram_img.setFont(font)
        self.raspi_ram_img.setText("")
        self.raspi_ram_img.setPixmap(QtGui.QPixmap("img/GUI2/ram.png"))
        self.raspi_ram_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.raspi_ram_img.setObjectName("raspi_ram_img")        
        self.BG.raise_()
        self.cadreClock.raise_()
        self.notfis.raise_()
        self.stats.raise_()       
        self.cadreMusic.raise_()
        self.homeBG.raise_()
        self.weatherBG.raise_()
        self.img_album.raise_()
        self.titleMusic.raise_()
        self.artistMusic.raise_()
        self.cadreAlbum.raise_()
        self.temp.raise_()
        self.humi.raise_()
        self.IconWeather_1.raise_()
        self.tempExte.raise_()
        self.media.raise_()
        self.cadreNotifs_1.raise_()
        self.cadreDataRaspi.raise_()
        self.cadreNotifs_2.raise_()
        self.cadreNotifs_4.raise_()
        self.cadreNotifs_3.raise_() 
        self.data_1.raise_()
        self.Twitch_Title.raise_()
        self.date_1.raise_()
        self.date_2.raise_()
        self.date_3.raise_()
        self.date_4.raise_()
        self.date_5.raise_()
        self.date_6.raise_()
        self.date_7.raise_()
        self.tempExte_2.raise_()
        self.IconWeather_2.raise_()
        self.tempExte_3.raise_()
        self.IconWeather_3.raise_()
        self.tempExte_4.raise_()
        self.IconWeather_4.raise_()
        self.tempExte_5.raise_()
        self.IconWeather_5.raise_()
        self.tempExte_7.raise_()
        self.IconWeather_7.raise_()
        self.tempExte_9.raise_()
        self.IconWeather_9.raise_()
        self.date.raise_()
        self.lcdNumber.raise_()
        self.spot_play.raise_()
        self.spot_forward.raise_()
        self.spot_back.raise_()
        self.buttonIMG_1.raise_()
        self.img_PP_1.raise_()
        self.buttonIMG_2.raise_()
        self.data_2.raise_()
        self.img_PP_2.raise_()
        self.Twitch_Title_2.raise_()
        self.buttonIMG_3.raise_()
        self.data_3.raise_()
        self.img_PP_3.raise_()
        self.Twitch_Title_3.raise_()
        self.buttonIMG_4.raise_()
        self.data_4.raise_()
        self.img_PP_4.raise_()
        self.Twitch_Title_4.raise_()
        self.raspi_temp.raise_()  
        self.progressBar.raise_()
        self.progressBar_2.raise_()
        self.raspi_ram_2.raise_()
        self.raspi_cpu_2.raise_()
        self.stats_artist.raise_()
        self.stat_song.raise_()
        self.clock.raise_()
        self.cadreRL.raise_()
        self.rl_3v3.raise_()
        self.rl_2v2.raise_()
        self.rl_rank_img_1.raise_()
        self.rl_rank_img_2.raise_()
        self.rank_rl_1.raise_()
        self.rank_rl_2.raise_()
        self.raspi_ram_img.raise_()
        self.raspi_cpu_img.raise_()        
        MainWindow.setCentralWidget    
        MainWindow.setCentralWidget(self.centralwidget)
        self.media.setBuddy(self.media)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.app = app
        self.media.setHidden(True)
        # self.clock.setHidden(True)
        self.path = os.getcwd()
        
        if TEMP_ON:
            self.temp.setVisible(True)
            self.humi.setVisible(True)
            self.homeBG.setVisible(True)
        else:
            self.temp.setHidden(True)
            self.humi.setHidden(True)
            self.homeBG.setHidden(True)
               
        # creating a timer object 
        timer = QTimer(self.centralwidget) 
  
        # adding action to timer 
        timer.timeout.connect(self.showTime) 
  
        # update the timer every second 
        timer.start(1000)
        
        self.notifs = []
        
        self.buttonIMG_1.setHidden(True)
        self.buttonIMG_2.setHidden(True)
        self.buttonIMG_3.setHidden(True)
        self.buttonIMG_4.setHidden(True)        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.data_1.setText(_translate("MainWindow", "Text"))
        self.Twitch_Title.setText(_translate("MainWindow", "Twitch Title"))
        self.titleMusic.setText(_translate("MainWindow", "TextLabel"))
        self.artistMusic.setText(_translate("MainWindow", "TextLabel"))
        self.temp.setText(_translate("MainWindow", "24.0°C"))
        self.humi.setText(_translate("MainWindow", "85%"))
        self.tempExte.setText(_translate("MainWindow", "24.0°C"))
        self.date_1.setText(_translate("MainWindow", "24/09"))
        self.date_2.setText(_translate("MainWindow", "24/09"))
        self.date_3.setText(_translate("MainWindow", "24/09"))
        self.date_4.setText(_translate("MainWindow", "24/09"))
        self.date_5.setText(_translate("MainWindow", "24/09"))
        self.date_6.setText(_translate("MainWindow", "24/09"))
        self.date_7.setText(_translate("MainWindow", "24/09"))
        self.tempExte_2.setText(_translate("MainWindow", "24.0°C"))
        self.tempExte_3.setText(_translate("MainWindow", "24.0°C"))
        self.tempExte_4.setText(_translate("MainWindow", "24.0°C"))
        self.tempExte_5.setText(_translate("MainWindow", "24.0°C"))
        self.tempExte_7.setText(_translate("MainWindow", "24.0°C"))
        self.tempExte_9.setText(_translate("MainWindow", "24.0°C"))
        self.date.setText(_translate("MainWindow", "Dimanche 27 Septembre"))
        self.data_2.setText(_translate("MainWindow", "Text"))
        self.Twitch_Title_2.setText(_translate("MainWindow", "Twitch Title"))
        self.data_3.setText(_translate("MainWindow", "Text"))
        self.Twitch_Title_3.setText(_translate("MainWindow", "Twitch Title"))
        self.data_4.setText(_translate("MainWindow", "Text"))
        self.Twitch_Title_4.setText(_translate("MainWindow", "Twitch Title"))
        self.raspi_temp.setText(_translate("MainWindow", "0°C"))
        self.raspi_ram_2.setText(_translate("MainWindow", "TextLabel"))
        self.raspi_cpu_2.setText(_translate("MainWindow", "TextLabel"))        
        self.stats_artist.setText(_translate("MainWindow", "1) AYAYA "))
        self.stat_song.setText(_translate("MainWindow", "1) AYA l\'abum"))
        self.rank_rl_1.setText(_translate("MainWindow", "1085 "))
        self.rl_3v3.setText(_translate("MainWindow", "3V3"))
        self.rl_2v2.setText(_translate("MainWindow", "2V2"))
        self.rank_rl_2.setText(_translate("MainWindow", "1085 "))
        
    def launchTwitterThread(self):
        self.twitter_thread = Twitter(1, "Twitter Thread")
        self.twitter_thread.twitter_signal.connect(self.newNotifications)
        self.buttonIMG_1.clicked.connect(self.showMedia)
        self.buttonIMG_2.clicked.connect(self.showMedia)
        self.buttonIMG_3.clicked.connect(self.showMedia)
        self.buttonIMG_4.clicked.connect(self.showMedia)
        self.twitter_thread.start()
        return self.twitter_thread
    
    def launchTwitchThread(self):
        self.twitch_thread = Twitch(2, "Twitch Thread")
        self.twitch_thread.twitch_signal.connect(self.newNotifications)
        self.twitch_thread.start()
        return self.twitch_thread  
    
    def launchHTMLThread(self):
        self.HTML_thread = htmlServ(3, "HTML Thread", self.app)
        self.HTML_thread.start()
        return self.HTML_thread   
    
    def launchSpotifyThread(self):
        self.spotify_thread = Spotify(4, "Spotify Thread", self.app)
        self.spotify_thread.Spotify_signal.connect(self.showMusic)
        self.spotify_thread.idle_spoti_signal.connect(self.HideMusic)
        self.spotify_thread.play_pause_signal.connect(self.switchSpotButton)
        self.spotify_thread.stat_signal.connect(self.updateStats)
        self.spot_back.clicked.connect(self.spotify_thread.prevTrack)
        self.spot_play.clicked.connect(self.spotify_thread.play_pause)
        self.spot_forward.clicked.connect(self.spotify_thread.nextTrack)
        self.spotify_thread.start()
        self.listener_thread = Listener(on_press=self.on_press, on_release=None)
        # This is a daemon=True thread, use .join() to prevent code from exiting  
        self.listener_thread.start()        
        return self.spotify_thread

    def launchTemperatureThread(self):       
        self.temp_thread = DHT11(6, "Temperature Thread")
        self.temp_thread.DHT11_signal.connect(self.showTempHouse)
        self.temp_thread.start()
        return self.temp_thread     

    def launchWeatherThread(self):       
        self.weather_thread = Weather(7, "Weather Thread")
        self.weather_thread.weather_signal.connect(self.showWeather)
        self.weather_thread.start()
        return self.weather_thread 

    def launchYoutubeThread(self):       
        self.youtube_thread = Youtube(8, "Youtube Thread")
        self.youtube_thread.yt_signal.connect(self.newNotifications)
        self.youtube_thread.start()
        return self.youtube_thread 

    def launchRaspiThread(self):       
        self.raspi_thread = RaspiInformation(9, "Raspi Thread")
        self.raspi_thread.raspi_signal.connect(self.printGraphRaspi)
        self.raspi_thread.start()
        return self.raspi_thread
    
    def launchGameTrackerThread(self):       
        self.game_thread = GameTracker(10, "Rocket League Thread")
        self.game_thread.game_signal.connect(self.printGame)
        self.game_thread.start()
        return self.game_thread  
    
    def showMedia(self):
        if self.media.isVisible:
            self.media.setHidden(True)
        else:
            self.media.setVisible(True)

    def switchSpotButton(self, state):
        if state:
            self.spot_play.setStyleSheet("background-color: rgba(255, 255, 255, 0); background-image: url(img/GUI2/pause.png);")          
        else:
            self.spot_play.setStyleSheet("background-color: rgba(255, 255, 255, 0); background-image: url(img/GUI2/play.png);")            

    def printTweet(self, data, label, Photo, title, cadre, button):
        title.setHidden(True)
        text = data.get("text", "Error while printing tweet")
        label.setText(text)
        label.adjustSize()
        self.getImage(data["url"], data["username"], "Twitter", 90)
        im = Image.open("img/Twitter/" + data["username"]+ ".png")
        im_conv = self.convert_to_srgb(im)
        im_conv.save("img/Twitter/" + data["username"] + ".png")
        Photo.setPixmap(QtGui.QPixmap("img/Twitter/" + data["username"] + ".png"))
        if data["media"] != None:
            self.getImage(data["media"]["link"], data["media"]["id"], "Twitter_Media", 275)
            self.media.setPixmap(QtGui.QPixmap("img/Twitter_Media/" + data["media"]["id"] + ".png"))
            button.setVisible(True)
        print(data["events"])
        if data["events"] == "Mention":
            cadre.setPixmap(QtGui.QPixmap("img/GUI2/tweet_mentions.png"))
        elif data["events"] == "rt":
            cadre.setPixmap(QtGui.QPixmap("img/GUI2/tweet_RT.png")) 
        elif data["events"] == "fav":
            cadre.setPixmap(QtGui.QPixmap("img/GUI2/tweet_like.png"))
        elif data["events"] == "dm":
            print("DM received but not yet showed")
            
    def printStreams(self, data, label, Photo, title, cadre):
        self.media.setHidden(True)
        label.setText(data["text"])     
        label.adjustSize()
        self.getImage(data["url"], data["username"], "Twitch", 90)
        Photo.setPixmap(QtGui.QPixmap("img/Twitch/" + data["username"]+ ".png"))
        title.setVisible(True)
        title.setText(data["title"])      
        title.adjustSize()
        cadre.setPixmap(QtGui.QPixmap("img/GUI2/twitch_border.png"))
        
    def printYoutube(self, data, label, Photo, title, cadre):
        label.setText("New video from " + data["username"])
        label.adjustSize()
        self.getImage(data["url"], data["user_id"], "Youtube", 90)
        Photo.setPixmap(QtGui.QPixmap("img/Youtube/" + data["user_id"]+ ".png"))
        title.setVisible(True)
        title.setText(data["title"])      
        title.adjustSize()        
        cadre.setPixmap(QtGui.QPixmap("img/GUI2/youtube.png"))
        
    def showMusic(self, data):
        self.titleMusic.setText(data["track"])
        self.titleMusic.adjustSize()
        self.artistMusic.setText(data["artist"])
        self.artistMusic.adjustSize()
        self.getImage(data["img_album"], data["album"], "Spotify", 150)
        self.img_album.setPixmap(QtGui.QPixmap("img/Spotify/" + data["album"]+ ".png"))
        
    def HideMusic(self, state=False):
        if state:
            self.cadreMusic.setHidden(True)
            self.titleMusic.setHidden(True)
            self.artistMusic.setHidden(True)
            self.cadreAlbum.setHidden(True)
            self.img_album.setHidden(True)
        elif not(state):
            self.cadreMusic.setVisible(True)
            self.titleMusic.setVisible(True)
            self.artistMusic.setVisible(True)
            self.cadreAlbum.setVisible(True)
            self.img_album.setVisible(True)  
            
    def on_press(self, key): #only working on windows
        if key == Key.media_play_pause:
            # play pause media key was pressed
            self.spotify_thread.play_pause()
        if key == Key.media_next:
            # next key was pressed
            self.spotify_thread.nextTrack()
        if key == Key.media_previous:
            # previous key was pressed 
            self.spotify_thread.prevtrack()

    def on_release(key):
        pass            
            
    def getImage(self, url, name, media_type, size=None):
        try:
            img_path = "img/" + media_type + "/" + name + ".png"
            if not(path.isdir("img/" + media_type)):
                os.mkdir("img/" + media_type)
            if path.exists(img_path) == False:
                Response = requests.get(url)
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
                if size != None:
                    self.reduceImageSize(size, img_path)        
        except OSError as Os:
            print("Problem during conversion of image")
            print(str(Os))
        except Exception as error:
            print("Error when getting image")
            print(error)
            
    def convert_to_srgb(self, img):
        '''Convert PIL image to sRGB color space (if possible)'''
        icc = img.info.get('icc_profile', '')
        if icc:
            io_handle = io.BytesIO(icc)     # virtual file
            src_profile = ImageCms.ImageCmsProfile(io_handle)
            dst_profile = ImageCms.createProfile('sRGB')
            img = ImageCms.profileToProfile(img, src_profile, dst_profile)
        return img
    
    def reduceImageSize(self, base, img_path):
        basewidth = base
        img = Image.open(img_path)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(img_path)
        
    def showTempHouse(self, temp):
        self.temp.setText(temp["Temp"])
        self.humi.setText(temp["Humi"])
        
    def showWeather(self, weather):
        date_ = date.today()
        if weather["day"] == "today":
            self.tempExte.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_1.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            self.date_1.setText(date_.strftime("%d/%m"))
        elif weather["day"] == 1:
            self.tempExte_2.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_2.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            date_day2 = date_ + timedelta(days=1)
            self.date_2.setText(date_day2.strftime("%d/%m"))
        elif weather["day"] == 2:
            self.tempExte_3.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_3.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            date_day3 = date_ + timedelta(days=2)
            self.date_3.setText(date_day3.strftime("%d/%m"))
        elif weather["day"] == 3:
            self.tempExte_4.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_4.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            date_day4 = date_ + timedelta(days=3)
            self.date_4.setText(date_day4.strftime("%d/%m"))
        elif weather["day"] == 4:
            self.tempExte_5.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_5.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            date_day5 = date_ + timedelta(days=4)
            self.date_5.setText(date_day5.strftime("%d/%m"))
        elif weather["day"] == 5:
            self.tempExte_7.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_7.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            date_day6 = date_ + timedelta(days=5)
            self.date_6.setText(date_day6.strftime("%d/%m"))
        elif weather["day"] == 6:
            self.tempExte_9.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_9.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            date_day7 = date_ + timedelta(days=6)
            self.date_7.setText(date_day7.strftime("%d/%m"))
            
    # method called by timer 
    def showTime(self): 
        # getting current time 
        current_time = QTime.currentTime() 
        # converting QTime object to string 
        label_time = current_time.toString('hh:mm') 
        # showing it to the label 
        self.lcdNumber.display(label_time)
        day = date.today().weekday()
        if day == 0:
            day_txt = "Monday"
        elif day == 1:
            day_txt = "Tuesday"
        elif day == 2:
            day_txt = "Wednesday"
        elif day == 3:
            day_txt = "Thursday"
        elif day == 4:
            day_txt = "Friday"
        elif day == 5:
            day_txt = "Saturday"
        elif day == 6:
            day_txt = "Sunday"
        else:
            day_txt = ""            
        self.date.setText(day_txt + ", " + date.today().strftime("%B %d"))
        # self.paintEvent()
      
    def newNotifications(self, data):
        if len(self.notifs) == 4:
            self.notifs.remove(self.notifs[0])
        if data in self.notifs:
            print("already get notification")
        else:
            self.notifs.append(data)
            self.updateNotifs()
            print("Notification added")
        
    def updateNotifs(self):
        for i in range(len(self.notifs)):
            if i == 0:
                img = self.img_PP_1
                text = self.data_1
                cadre = self.cadreNotifs_1
                twitchTitle = self.Twitch_Title
                button = self.buttonIMG_1
            elif i == 1:
                img = self.img_PP_2
                text = self.data_2
                cadre = self.cadreNotifs_2
                twitchTitle = self.Twitch_Title_2
                button = self.buttonIMG_2
            elif i == 2:
                img = self.img_PP_3
                text = self.data_3
                cadre = self.cadreNotifs_3 
                twitchTitle = self.Twitch_Title_3
                button = self.buttonIMG_3
            elif i == 3:
                img = self.img_PP_4
                text = self.data_4
                cadre = self.cadreNotifs_4 
                twitchTitle = self.Twitch_Title_4
                button = self.buttonIMG_4
            else:
                print("Indice not within correct range (GUI)")
            button.setHidden(True)
            data = self.notifs[i]
            web = data.get("website", "")
            if web == "Twitch": # Twitch
                self.printStreams(data, text, img, twitchTitle, cadre)
            elif web == "Twitter":
                self.printTweet(data, text, img, twitchTitle, cadre, button)
            elif web == "Youtube":
                self.printYoutube(data, text, img, twitchTitle, cadre)
            else:
                print("Problemo")    
        
    def printGraphRaspi(self, data):
        self.progressBar.setValue(data["ram"])
        self.progressBar_2.setValue(data["cpu"])
        self.raspi_temp.setText("{:.1f}°C".format(data["temp"]))
        self.raspi_ram_2.setText(str(data["ram"]) + "%")
        self.raspi_cpu_2.setText(str(data["cpu"]) + "°%")
        
    def updateStats(self, list_):
        self.stats_artist.setText(list_[0])
        self.stat_song.setText(list_[1])
        
    def printGame(self, dico):
        mmr_3v3 = dico.get("3v3",{}).get('mmr', "")
        mmr_2v2 = dico.get("2v2",{}).get('mmr', "")
        self.rank_rl_1.setText(mmr_3v3)
        self.rank_rl_2.setText(mmr_2v2)
        
        self.rl_rank_img_1.setPixmap(QtGui.QPixmap("img/GUI2/RL/" + dico.get("3v3",{}).get('rank', "") + ".png"))
        self.rl_rank_img_2.setPixmap(QtGui.QPixmap("img/GUI2/RL/" + dico.get("2v2",{}).get('rank', "") + ".png"))   
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
