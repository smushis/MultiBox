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
from PyQt5 import QtCore, QtGui, QtWidgets

import requests
import io
from PIL import Image
from PIL import ImageCms
from os import path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, app):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 720)
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 351, 441))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/PS4-Tranquility-(Avatar-Border).png"))
        self.label_2.setObjectName("label_2")
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
        self.BG.raise_()
        self.Photo.raise_()
        self.username.raise_()
        self.label_2.raise_()
        self.cadre.raise_()
        self.label1.raise_()
        self.Twitch_Title.raise_()
        self.media.raise_()
        self.img_album.raise_()
        self.cadreMusic.raise_()
        self.titleMusic.raise_()
        self.artistMusic.raise_()
        self.cadreAlbum.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        self.app = app
        self.media.setHidden(True)
        
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
        self.Photo.setPixmap(QtGui.QPixmap("img/Twitch/" + data["username"]+ "200x200.png"))
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
        self.getImage(data["img_album"], data["track"], "Spotify")
        self.img_album.setPixmap(QtGui.QPixmap("img/Spotify/" + data["track"]+ ".png"))
        
    def getImage(self, url, username, web):
        size = 200, 200
        Response = requests.get(url)
        if web == "Twitter":
            img_path = "img/Twitter/" + username + ".png"
            if path.exists(img_path) == False:
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
                self.reduceImageSize(200, img_path)
        elif web == "Twitter_Media":
            img_path = "img/Twitter/media" + username + ".png"
            if path.exists(img_path) == False:
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
                self.reduceImageSize(300, img_path)
        elif web == "Spotify":
            img_path = "img/Spotify/" + username + ".png"
            if path.exists(img_path) == False:
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
                self.reduceImageSize(150, img_path)            
        else:
            img_path = "img/Twitch/" + username + ".png"
            if path.exists(img_path) == False:
                file = open(img_path, "wb")
                file.write(Response.content)
                file.close()
            im = Image.open("img/Twitch/" + username + ".png")
            im = im.resize(size)
            im.save("img/Twitch/" + username + "200x200.png")                
        
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
        
    def OEmbed(self, html):
        file = open("tweet.html", "wb")
        file.write(html)
        file.close()
    

# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
