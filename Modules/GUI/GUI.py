# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultiBox.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from Modules.Twitter.twitter import Twitter
from Modules.Twitch.twitch import Twitch
from Modules.Listener.html_serv import htmlServ
from Modules.Spotify.spotify import Spotify
from Modules.Spotify.spotify import SpotifyListener
temperature_on = True
if temperature_on:
    from Modules.Temperature.Temperature import DHT11 
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import io
from PIL import Image
from PIL import ImageCms
from os import path
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, app):
        MainWindow.setObjectName("Notifications")
        MainWindow.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(500, 200, 491, 221))
        self.label1.setBaseSize(QtCore.QSize(531, 261))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label1.setFont(font)
        self.label1.setStyleSheet("")
        self.label1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label1.setWordWrap(True)
        self.label1.setObjectName("label1")
        self.Photo = QtWidgets.QLabel(self.centralwidget)
        self.Photo.setGeometry(QtCore.QRect(110, 150, 201, 201))
        self.Photo.setStyleSheet("")
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap("img/kurisux200.png"))
        self.Photo.setObjectName("Photo")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(140, 400, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.Twitch_Title = QtWidgets.QLabel(self.centralwidget)
        self.Twitch_Title.setGeometry(QtCore.QRect(490, 290, 491, 121))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Twitch_Title.setFont(font)
        self.Twitch_Title.setWordWrap(True)
        self.Twitch_Title.setObjectName("Twitch_Title")
        self.cadrePP = QtWidgets.QLabel(self.centralwidget)
        self.cadrePP.setGeometry(QtCore.QRect(60, 30, 351, 441))
        self.cadrePP.setText("")
        self.cadrePP.setPixmap(QtGui.QPixmap("img/PS4-Tranquility-(Avatar-Border).png"))
        self.cadrePP.setObjectName("cadrePP")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(0, 0, 1451, 721))
        self.BG.setText("")
        self.BG.setPixmap(QtGui.QPixmap("img/TwitchBG.png"))
        self.BG.setObjectName("BG")
        self.media = QtWidgets.QLabel(self.centralwidget)
        self.media.setGeometry(QtCore.QRect(630, 350, 331, 291))
        self.media.setStyleSheet("border: 10px double blue;")
        self.media.setText("")
        self.media.setAlignment(QtCore.Qt.AlignCenter)
        self.media.setObjectName("media")
        self.cadre = QtWidgets.QLabel(self.centralwidget)
        self.cadre.setGeometry(QtCore.QRect(380, 40, 741, 481))
        self.cadre.setText("")
        self.cadre.setPixmap(QtGui.QPixmap("img/twitch_bg.png"))
        self.cadre.setObjectName("cadre")
        self.img_album = QtWidgets.QLabel(self.centralwidget)
        self.img_album.setGeometry(QtCore.QRect(50, 490, 151, 151))
        self.img_album.setText("")
        self.img_album.setPixmap(QtGui.QPixmap("img/kurisux150.png"))
        self.img_album.setObjectName("img_album")
        self.cadreMusic = QtWidgets.QLabel(self.centralwidget)
        self.cadreMusic.setGeometry(QtCore.QRect(200, 470, 421, 201))
        self.cadreMusic.setText("")
        self.cadreMusic.setPixmap(QtGui.QPixmap("img/music_bg.png"))
        self.cadreMusic.setObjectName("cadreMusic")
        self.titleMusic = QtWidgets.QLabel(self.centralwidget)
        self.titleMusic.setGeometry(QtCore.QRect(280, 525, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.titleMusic.setFont(font)
        self.titleMusic.setObjectName("titleMusic")
        self.artistMusic = QtWidgets.QLabel(self.centralwidget)
        self.artistMusic.setGeometry(QtCore.QRect(280, 590, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.artistMusic.setFont(font)
        self.artistMusic.setObjectName("artistMusic")
        self.cadreAlbum = QtWidgets.QLabel(self.centralwidget)
        self.cadreAlbum.setGeometry(QtCore.QRect(20, 450, 191, 211))
        self.cadreAlbum.setText("")
        self.cadreAlbum.setPixmap(QtGui.QPixmap("img/spot.png"))
        self.cadreAlbum.setObjectName("cadreAlbum")
        self.tempImg = QtWidgets.QLabel(self.centralwidget)
        self.tempImg.setGeometry(QtCore.QRect(980, 570, 101, 111))
        self.tempImg.setText("")
        self.tempImg.setPixmap(QtGui.QPixmap("img/thermometer.png"))
        self.tempImg.setObjectName("tempImg")
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(1120, 520, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.humi = QtWidgets.QLabel(self.centralwidget)
        self.humi.setGeometry(QtCore.QRect(1120, 600, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.humi.setFont(font)
        self.humi.setAlignment(QtCore.Qt.AlignCenter)
        self.humi.setObjectName("humi")        
        self.temp.setFont(font)
        self.temp.setObjectName("temp")
        self.BG.raise_()
        self.Photo.raise_()
        self.username.raise_()
        self.cadrePP.raise_()
        self.cadre.raise_()
        self.label1.raise_()
        self.Twitch_Title.raise_()
        self.media.raise_()
        self.img_album.raise_()
        self.cadreMusic.raise_()
        self.titleMusic.raise_()
        self.artistMusic.raise_()
        self.cadreAlbum.raise_()
        self.tempImg.raise_()
        self.temp.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        self.app = app
        self.media.setHidden(True)
        self.path = os.getcwd()
        
    def switchIMG(self, state):
        if state == "Twitch":
            self.media.setHidden(True)
            self.BG.setPixmap(QtGui.QPixmap("img/TwitchBG.png"))
        else:
            self.media.setHidden(True)
            self.BG.setPixmap(QtGui.QPixmap("img/twitter_bg.png"))            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Text"))
        self.username.setText(_translate("MainWindow", "TextLabel"))
        self.Twitch_Title.setText(_translate("MainWindow", "Twitch Title"))
        self.titleMusic.setText(_translate("MainWindow", "TextLabel"))
        self.artistMusic.setText(_translate("MainWindow", "TextLabel"))
        self.temp.setText(_translate("MainWindow", " X°C"))
        self.humi.setText(_translate("MainWindow", "85%"))
        
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
    
    def launchSpotifyThread(self):
        self.spotify_thread = Spotify(3, "Spotify Thread", self.app)
        self.spotify_thread.Spotify_signal.connect(self.showMusic)
        self.spotify_thread.start()
        return self.spotify_thread

    def launchSpotifyListenerThread(self):
        self.spotListener_thread = SpotifyListener(3, "Timer Thread")
        self.spotListener_thread.timer_signal.connect(self.spotify_thread.getCurrentTrack)
        self.spotListener_thread.start()
        return self.spotListener_thread

    def launchTemperatureThread(self):       
        self.temp_thread = DHT11(3, "Temperature Thread")
        self.temp_thread.DHT11_signal.connect(self.printTemp)
        self.temp_thread.start()
        return self.temp_thread           

    def printTweet(self, data):
        self.media.setHidden(True)
        self.switchIMG("Twitter")
        text = data["text"].split('https')[0]
        self.label1.setText(text) 
        self.label1.adjustSize()
        self.getImage(data["url"], data["username"], "Twitter")
        im = Image.open("img/Twitter/" + data["username"]+ ".png")
        im_conv = self.convert_to_srgb(im)
        im_conv.save("img/Twitter/" + data["username"] + ".png")
        self.Photo.setPixmap(QtGui.QPixmap("img/Twitter/" + data["username"] + ".png"))
        self.username.setText(data["username"])
        self.username.adjustSize()
        self.Twitch_Title.setHidden(True)
        if data["media"] != None:
            self.getImage(data["media"]["link"],data["media"]["id"], "Twitter_Media")
            self.media.setPixmap(QtGui.QPixmap("img/Twitter/media" + data["media"]["id"] + ".png"))
            self.media.adjustSize()
            self.media.setVisible(True)
        if data["events"] == "Mention":
            self.cadre.setPixmap(QtGui.QPixmap("img/Mentions_bg.png"))
            self.cadre.adjustSize()
        elif data["events"] == "rt":
            self.cadre.setPixmap(QtGui.QPixmap("img/RT_bg.png"))
            self.cadre.adjustSize()           
        elif data["events"] == "fav":
            self.cadre.setPixmap(QtGui.QPixmap("img/like_bg.png"))
            self.cadre.adjustSize()  
            
    def printStreams(self,data):
        self.media.setHidden(True)
        self.switchIMG("Twitch")
        self.label1.setText(data["text"])     
        self.label1.adjustSize()
        self.getImage(data["url"], data["username"], "Twitch")
        self.Photo.setPixmap(QtGui.QPixmap("img/Twitch/" + data["username"]+ ".png"))
        self.username.setText(data["username"])
        self.username.adjustSize()
        self.Twitch_Title.setVisible(True)
        self.Twitch_Title.setText(data["title"])      
        self.Twitch_Title.adjustSize()
        self.cadre.setPixmap(QtGui.QPixmap("img/twitch_bg.png"))
        self.cadre.adjustSize()
        #self.Photo.setHidden(True)
        
    def showMusic(self, data):
        self.media.setHidden(True)
        self.titleMusic.setText(data["track"])
        self.titleMusic.adjustSize()
        self.artistMusic.setText(data["artist"])
        self.artistMusic.adjustSize()
        self.getImage(data["img_album"], data["album"], "Spotify")
        self.img_album.setPixmap(QtGui.QPixmap("img/Spotify/" + data["album"]+ ".png"))
         
        
    def getImage(self, url, username, web):
        if web == "Twitter":
            img_path = "img/Twitter/" + username + ".png"
            if not(path.isdir("img/Twitter")):
                os.mkdir("img/Twitter")
            if path.exists(img_path) == False:
                Response = requests.get(url)
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
                self.reduceImageSize(200, img_path)
        elif web == "Twitter_Media":
            img_path = "img/Twitter/media/" + username + ".png"
            if not(path.isdir("img/Twitter/media")): 
                os.mkdir("img/Twitter/media")
            if path.exists(img_path) == False:
                Response = requests.get(url)
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
                self.reduceImageSize(300, img_path)
        elif web == "Spotify":
            img_path = "img/Spotify/" + username + ".png"
            if not(path.isdir("img/Spotify")): 
                os.mkdir("img/Spotify")                
            if path.exists(img_path) == False:
                Response = requests.get(url)
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
                self.reduceImageSize(150, img_path)            
        elif web == "Twitch":
            img_path = "img/Twitch/" + username + ".png"
            if not(path.isdir("img/Twitch")):
                os.mkdir("img/Twitch")            
            if path.exists(img_path) == False:
                Response = requests.get(url)
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
                self.reduceImageSize(200, img_path)
        else:
            print("Website not recognize")
        
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
        
    def printTemp(self, temp):
        self.temp.setText(temp["Temp"])
        self.temp.adjustSize()
        self.humi.setText(temp["Humi"])
        self.humi.adjustSize()
        
# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
