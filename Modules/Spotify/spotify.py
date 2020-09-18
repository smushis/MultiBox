# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:18:36 2020

@author: Barmando
"""

import spotipy
import json
import spotipy.util as util
import time

from Modules.Spotify import spotify_auth as auth2
from spotipy.oauth2 import SpotifyOAuth
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

token_file = "Modules/Spotify/spotify_token.oauth"

class Spotify(QtCore.QThread):
    Spotify_signal = pyqtSignal(dict)
    scope = "user-read-playback-state user-modify-playback-state"
    DEFAULT_DEVICE = ""
    token = ""
    
    def __init__(self, threadID, name, app):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
        self.app = app
        auth2.generate_token(self.scope, token_file)
        self.getToken()

    def run(self):
        print("Starting " + self.name + "\n\r")
        self.sp = spotipy.Spotify(self.token)
        self.showDevices()
        self.playTop97()
        time.sleep(1)
        #self.getCurrentTrack()          
            
    def getToken(self):      
        with open(token_file, 'r') as file:
            auth = json.load(file)           
        self.token = auth["token"]      
        
    def showDevices(self):
        res = self.sp.devices()
        print(res)
        
    def playTop97(self):
        self.sp.shuffle(True)
        self.sp.start_playback(context_uri='spotify:playlist:2EDQvU4v6zHH39G1pKAJrr')
        
    def getCurrentTrack(self):
        tr = self.sp.current_user_playing_track()
        artist = tr['item']['artists'][0]['name']
        track = tr['item']['name']
        img_album = tr['item']['album']['images'][1]['url']
        #if artist !="":
            #print("Currently playing " + artist + " - " + track)
        self.Spotify_signal.emit(self.createDico(artist, track, img_album))
            
    def createDico(self, artist, track, img_album):
        dico = {}
        dico["artist"] = artist
        dico["track"] = track
        dico["img_album"] = img_album
        return dico
    
    
class SpotifyListener(QtCore.QThread):
    
    timer_signal = pyqtSignal()
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
        
    def run(self):
        print("Starting " + self.name + "\n\r")
        i = True
        while i == True:
            time.sleep(10)
            self.timer_signal.emit()          
          