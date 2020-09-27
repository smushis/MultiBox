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

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel 
import requests
import io
from PIL import Image
from PIL import ImageCms
from os import path
from time import sleep
import os
from datetime import date

from constants import TEMP_ON

if TEMP_ON:
    from Modules.Temperature.Temperature import DHT11


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, app):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.data_1 = QtWidgets.QLabel(self.centralwidget)
        self.data_1.setGeometry(QtCore.QRect(890, 70, 241, 91))
        self.data_1.setBaseSize(QtCore.QSize(531, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_1.setFont(font)
        self.data_1.setStyleSheet("")
        self.data_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.data_1.setWordWrap(True)
        self.data_1.setObjectName("data_1")
        self.Twitch_Title = QtWidgets.QLabel(self.centralwidget)
        self.Twitch_Title.setGeometry(QtCore.QRect(890, 120, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Twitch_Title.setFont(font)
        self.Twitch_Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
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
        self.titleMusic.setGeometry(QtCore.QRect(250, 576, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.titleMusic.setFont(font)
        self.titleMusic.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.titleMusic.setWordWrap(True)
        self.titleMusic.setObjectName("titleMusic")
        self.artistMusic = QtWidgets.QLabel(self.centralwidget)
        self.artistMusic.setGeometry(QtCore.QRect(251, 620, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
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
        self.cadreNotifs_1.setGeometry(QtCore.QRect(855, -10, 410, 221))
        self.cadreNotifs_1.setText("")
        self.cadreNotifs_1.setPixmap(QtGui.QPixmap("img/GUI2/tweet_like.png"))
        self.cadreNotifs_1.setObjectName("cadreNotifs_1")
        self.cadreNotifs_2 = QtWidgets.QLabel(self.centralwidget)
        self.cadreNotifs_2.setGeometry(QtCore.QRect(855, 160, 591, 221))
        self.cadreNotifs_2.setText("")
        self.cadreNotifs_2.setPixmap(QtGui.QPixmap("img/GUI2/tweet_like.png"))
        self.cadreNotifs_2.setObjectName("cadreNotifs_2")
        self.cadreNotifs_3 = QtWidgets.QLabel(self.centralwidget)
        self.cadreNotifs_3.setGeometry(QtCore.QRect(855, 330, 591, 221))
        self.cadreNotifs_3.setText("")
        self.cadreNotifs_3.setPixmap(QtGui.QPixmap("img/GUI2/tweet_like.png"))
        self.cadreNotifs_3.setObjectName("cadreNotifs_3")
        self.cadreNotifs_4 = QtWidgets.QLabel(self.centralwidget)
        self.cadreNotifs_4.setGeometry(QtCore.QRect(855, 500, 591, 221))
        self.cadreNotifs_4.setText("")
        self.cadreNotifs_4.setPixmap(QtGui.QPixmap("img/GUI2/tweet_like.png"))
        self.cadreNotifs_4.setObjectName("cadreNotifs_4")
        self.buttonIMG_1 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonIMG_1.setGeometry(QtCore.QRect(890, 120, 45, 45))
        self.buttonIMG_1.setStyleSheet("background-image: url(:/bg/img.png);")
        self.buttonIMG_1.setText("")
        self.buttonIMG_1.setObjectName("buttonIMG_1")
        self.date_1 = QtWidgets.QLabel(self.centralwidget)
        self.date_1.setGeometry(QtCore.QRect(17, -5, 111, 61))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 210, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 540, 411, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/GUI2/music.png"))
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(160, 270, 121, 51))
        self.lcdNumber.setStyleSheet("")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setObjectName("lcdNumber")
        self.spot_play = QtWidgets.QPushButton(self.centralwidget)
        self.spot_play.setGeometry(QtCore.QRect(610, 610, 60, 60))
        self.spot_play.setObjectName("spot_play")
        self.spot_forward = QtWidgets.QPushButton(self.centralwidget)
        self.spot_forward.setGeometry(QtCore.QRect(700, 609, 60, 60))
        self.spot_forward.setObjectName("spot_forward")
        self.spot_back = QtWidgets.QPushButton(self.centralwidget)
        self.spot_back.setGeometry(QtCore.QRect(520, 610, 60, 60))
        self.spot_back.setObjectName("spot_back")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1150, 50, 101, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/GUI2/kurisux100.png"))
        self.label_3.setObjectName("label_3")
        self.buttonIMG_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonIMG_2.setGeometry(QtCore.QRect(890, 290, 45, 45))
        self.buttonIMG_2.setStyleSheet("background-image: url(:/bg/img.png);")
        self.buttonIMG_2.setText("")
        self.buttonIMG_2.setObjectName("buttonIMG_2")
        self.data_2 = QtWidgets.QLabel(self.centralwidget)
        self.data_2.setGeometry(QtCore.QRect(890, 240, 241, 91))
        self.data_2.setBaseSize(QtCore.QSize(531, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_2.setFont(font)
        self.data_2.setStyleSheet("")
        self.data_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.data_2.setWordWrap(True)
        self.data_2.setObjectName("data_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1150, 220, 101, 111))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/GUI2/kurisux100.png"))
        self.label_4.setObjectName("label_4")
        self.Twitch_Title_2 = QtWidgets.QLabel(self.centralwidget)
        self.Twitch_Title_2.setGeometry(QtCore.QRect(890, 290, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Twitch_Title_2.setFont(font)
        self.Twitch_Title_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Twitch_Title_2.setWordWrap(True)
        self.Twitch_Title_2.setObjectName("Twitch_Title_2")
        self.buttonIMG_3 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonIMG_3.setGeometry(QtCore.QRect(890, 460, 45, 45))
        self.buttonIMG_3.setStyleSheet("background-image: url(:/bg/img.png);")
        self.buttonIMG_3.setText("")
        self.buttonIMG_3.setObjectName("buttonIMG_3")
        self.data_3 = QtWidgets.QLabel(self.centralwidget)
        self.data_3.setGeometry(QtCore.QRect(890, 410, 241, 91))
        self.data_3.setBaseSize(QtCore.QSize(531, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_3.setFont(font)
        self.data_3.setStyleSheet("")
        self.data_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.data_3.setWordWrap(True)
        self.data_3.setObjectName("data_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1150, 390, 101, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("img/GUI2/kurisux100.png"))
        self.label_5.setObjectName("label_5")
        self.Twitch_Title_3 = QtWidgets.QLabel(self.centralwidget)
        self.Twitch_Title_3.setGeometry(QtCore.QRect(890, 460, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Twitch_Title_3.setFont(font)
        self.Twitch_Title_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Twitch_Title_3.setWordWrap(True)
        self.Twitch_Title_3.setObjectName("Twitch_Title_3")
        self.buttonIMG_4 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonIMG_4.setGeometry(QtCore.QRect(890, 630, 45, 45))
        self.buttonIMG_4.setStyleSheet("background-image: url(:/bg/img.png);")
        self.buttonIMG_4.setText("")
        self.buttonIMG_4.setObjectName("buttonIMG_4")
        self.data_4 = QtWidgets.QLabel(self.centralwidget)
        self.data_4.setGeometry(QtCore.QRect(890, 580, 241, 91))
        self.data_4.setBaseSize(QtCore.QSize(531, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_4.setFont(font)
        self.data_4.setStyleSheet("")
        self.data_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.data_4.setWordWrap(True)
        self.data_4.setObjectName("data_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1150, 560, 101, 111))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/GUI2/kurisux100.png"))
        self.label_6.setObjectName("label_6")
        self.Twitch_Title_4 = QtWidgets.QLabel(self.centralwidget)
        self.Twitch_Title_4.setGeometry(QtCore.QRect(890, 630, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Twitch_Title_4.setFont(font)
        self.Twitch_Title_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Twitch_Title_4.setWordWrap(True)
        self.Twitch_Title_4.setObjectName("Twitch_Title_4")
        self.BG.raise_()
        self.label_2.raise_()
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
        self.notfis.raise_()
        self.cadreNotifs_1.raise_()
        self.cadreNotifs_2.raise_()
        self.cadreNotifs_3.raise_()
        self.cadreNotifs_4.raise_()
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
        self.label.raise_()
        self.lcdNumber.raise_()
        self.spot_play.raise_()
        self.spot_forward.raise_()
        self.spot_back.raise_()
        self.buttonIMG_1.raise_()
        self.label_3.raise_()
        self.buttonIMG_2.raise_()
        self.data_2.raise_()
        self.label_4.raise_()
        self.Twitch_Title_2.raise_()
        self.buttonIMG_3.raise_()
        self.data_3.raise_()
        self.label_5.raise_()
        self.Twitch_Title_3.raise_()
        self.buttonIMG_4.raise_()
        self.data_4.raise_()
        self.label_6.raise_()
        self.Twitch_Title_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.media.setBuddy(self.media)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.app = app
        self.media.setHidden(True)
        # self.clock.setHidden(True)
        self.path = os.getcwd()
        
        self.spot_play.setStyleSheet("background-image : url(img/GUI2/play.png);")
        self.spot_back.setStyleSheet("background-image : url(img/GUI2/backward.png);")
        self.spot_forward.setStyleSheet("background-image : url(img/GUI2/forward.png);")
        
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
        self.label.setText(_translate("MainWindow", "Dimanche 27 Septembre"))
        self.spot_play.setText(_translate("MainWindow", "PushButton"))
        self.spot_forward.setText(_translate("MainWindow", "PushButton"))
        self.spot_back.setText(_translate("MainWindow", "PushButton"))
        self.data_2.setText(_translate("MainWindow", "Text"))
        self.Twitch_Title_2.setText(_translate("MainWindow", "Twitch Title"))
        self.data_3.setText(_translate("MainWindow", "Text"))
        self.Twitch_Title_3.setText(_translate("MainWindow", "Twitch Title"))
        self.data_4.setText(_translate("MainWindow", "Text"))
        self.Twitch_Title_4.setText(_translate("MainWindow", "Twitch Title"))
        
    def launchTwitterThread(self):
        self.twitter_thread = Twitter(1, "Twitter Thread")
        self.twitter_thread.twitter_signal.connect(self.newNotifications)
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
        self.spotify_thread.start()
        return self.spotify_thread

    # def launchSpotifyListenerThread(self):
    #     self.spotListener_thread = SpotifyListener(5, "Timer Thread")
    #     self.spotListener_thread.timer_signal.connect(self.spotify_thread.getCurrentTrack)
    #     self.spotListener_thread.start()
    #     return self.spotListener_thread

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
        # self.youtube_thread.yt_signal.connect()
        self.youtube_thread.start()
        return self.youtube_thread             

    def printTweet(self, data, label, Photo, cadre, title):
        text = data["text"].split('https')[0]
        title.setHidden(True)
        label.setText(text) 
        label.adjustSize()
        self.getImage(data["url"], data["username"], "Twitter", 90)
        im = Image.open("img/Twitter/" + data["username"]+ ".png")
        im_conv = self.convert_to_srgb(im)
        im_conv.save("img/Twitter/" + data["username"] + ".png")
        Photo.setPixmap(QtGui.QPixmap("img/Twitter/" + data["username"] + ".png"))
        self.Twitch_Title.setHidden(True)
        if data["media"] != None:
            self.getImage(data["media"]["link"], data["media"]["id"], "Twitter_Media", 275)
            self.media.setPixmap(QtGui.QPixmap("img/Twitter_Media/" + data["media"]["id"] + ".png"))
            self.media.adjustSize()
            self.media.setVisible(True)
        if data["events"] == "Mention":
            cadre.setPixmap(QtGui.QPixmap("img/GUI2/tweet_mentions.png"))
        elif data["events"] == "rt":
            cadre.setPixmap(QtGui.QPixmap("img/GUI2/tweet_RT.png"))          
        elif data["events"] == "fav":
            cadre.setPixmap(QtGui.QPixmap("img/GUI2/tweet_like.png"))
        sleep(5)
            
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
        sleep(5)
        #self.Photo.setHidden(True)
        
    def showMusic(self, data):
        self.titleMusic.setText(data["track"])
        self.titleMusic.adjustSize()
        self.artistMusic.setText(data["artist"])
        self.artistMusic.adjustSize()
        self.getImage(data["img_album"], data["album"], "Spotify", 150)
        self.img_album.setPixmap(QtGui.QPixmap("img/Spotify/" + data["album"]+ ".png"))
        
    def HideMusic(self, state=False):
        if state:
            self.label_2.setHidden(True)
            self.titleMusic.setHidden(True)
            self.artistMusic.setHidden(True)
            self.cadreAlbum.setHidden(True)
            self.img_album.setHidden(True)
        elif not(state):
            self.label_2.setVisible(True)
            self.titleMusic.setVisible(True)
            self.artistMusic.setVisible(True)
            self.cadreAlbum.setVisible(True)
            self.img_album.setVisible(True)           
            
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
            self.date_2.setText(date_.strftime("%d/%m"))
        elif weather["day"] == 2:
            self.tempExte_3.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_3.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            self.date_3.setText(date_.strftime("%d/%m"))
        elif weather["day"] == 3:
            self.tempExte_4.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_4.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png")) 
            self.date_4.setText(date_.strftime("%d/%m"))
        elif weather["day"] == 4:
            self.tempExte_5.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_5.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            self.date_5.setText(date_.strftime("%d/%m"))
        elif weather["day"] == 5:
            self.tempExte_7.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_7.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            self.date_6.setText(date_.strftime("%d/%m"))
        elif weather["day"] == 6:
            self.tempExte_9.setText(weather["temp"])
            self.getImage(weather["icon_url"], weather["type"], "Weather", 100)
            self.IconWeather_9.setPixmap(QtGui.QPixmap("img/Weather/" + weather["type"] + ".png"))
            self.date_7.setText(date_.strftime("%d/%m"))
            
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
        self.label.setText(day_txt + " " + date.today().strftime("%B %d"))       
      
    def newNotifications(self, data):
        if len(self.notifs) == 4:
            self.notifs.remove(self.notifs[0])
        self.notifs.append(data)
        self.updateNotifs()
        print("Notification added")
        
    def updateNotifs(self):
        for i in range(len(self.notifs)):
            if i == 0:
                img = self.label_3
                text = self.data_1
                cadre = self.cadreNotifs_1
                twitchTitle = self.Twitch_Title
            elif i == 1:
                img = self.label_4
                text = self.data_2
                cadre = self.cadreNotifs_2
                twitchTitle = self.Twitch_Title_2
            elif i == 2:
                img = self.label_5
                text = self.data_3
                cadre = self.cadreNotifs_3 
                twitchTitle = self.Twitch_Title_3
            elif i == 3:
                img = self.label_6
                text = self.data_4
                cadre = self.cadreNotifs_4 
                twitchTitle = self.Twitch_Title_4
            else:
                print("Indice not within correct range (GUI)") 
            data = self.notifs[i]
            if "title" in data: # Twitch
                self.printStreams(data, text, img, twitchTitle, cadre)
            elif "media" in data:
                self.printTweet(data, text, img, twitchTitle, cadre)
            else:
                print("Problemo")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
