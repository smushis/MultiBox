# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:18:36 2020

@author: Barmando
"""

import spotipy
import json
import time

from Modules.Spotify import spotify_auth as auth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from time import sleep
from requests import exceptions

token_file = "Modules/Spotify/spotify_token.oauth"

class Spotify(QtCore.QThread):
    Spotify_signal = pyqtSignal(dict)
    idle_spoti_signal = pyqtSignal(bool)
    
    scope = "user-read-playback-state user-modify-playback-state"
    DEFAULT_DEVICE = ""
    token = ""
    device_ID = ""
    sleep_count = 0
    
    
    def __init__(self, threadID, name, app):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
        self.app = app
        auth2.generate_token(self.scope, token_file)
        self.readToken()

    def run(self):
        print("Starting " + self.name + "\n\r")
        self.sp = spotipy.Spotify(self.token)
        while(not(self.playTop97())):
              sleep(10)        
        # self.showDevices()
        while True:
            self.getCurrentTrack()
            sleep(0.5)
                   
    def readToken(self):      
        with open(token_file, 'r') as file:
            auth = json.load(file)           
        self.token = auth["token"]      
        
    def showDevices(self):
        try:
            res = self.sp.devices()
            # print(res)
            return res
        except SpotifyException as E:
            self.handleException(E)
            print(E)
        
    def playTop97(self):
        try:
            self.sp.shuffle(True)
            self.sp.start_playback(context_uri='spotify:playlist:2EDQvU4v6zHH39G1pKAJrr')
            sleep(1)
            return True
        except SpotifyException as e:
            return self.handleException(e)
        except:
            print("ALED")
            
    def getCurrentTrack(self):
        try:
            tr = self.sp.current_user_playing_track()
            #print(tr)
            if tr != None:
                artist = tr['item']['artists'][0]['name']
                track = tr['item']['name']
                img_album = tr['item']['album']['images'][1]['url']
                album = tr['item']['album']['id']
                #if artist !="":
                    #print("Currently playing " + artist + " - " + track)
                self.Spotify_signal.emit(self.createDico(artist, track, img_album, album))
                if self.sleep_count ==0:
                    self.idle_spoti_signal.emit(False)
            else :
                if self.sleep_count < 10:
                    print("No playing track, retrying in 5s")
                    self.sleep_count += 1
                    sleep(2)
                else:
                    print("Idle until Device is Active again")
                    self.idle_spoti_signal.emit(True)
                    while(not(self.showDevices()["devices"][0]["is_active"])):
                        sleep(10)
                    self.sleep_count = 0
        except SpotifyException as e:
            sleep(10)
            return self.handleException(e)
        except exceptions.ReadTimeout:
            print("Timeout during getting current track")
        
            
    def handleException(self, e):
        if e.reason == "NO_ACTIVE_DEVICE":
            print("No devices active, retrying in 10s")
            return False
        elif e.http_status == 401:
            self.refreshToken()
            return False
        else:
            print("Reason" + str(e.http_status))
            return True
            
    def createDico(self, artist, track, img_album, album):
        dico = {}
        dico["artist"] = artist
        dico["track"] = track
        dico["img_album"] = img_album
        dico["album"] = album
        return dico
    
    def refreshToken(self):
        auth2.generate_token(self.scope, token_file)
        self.readToken()
        self.sp = spotipy.Spotify(self.token)
        
    def changeAudioOutput(self, output):
        devices = self.showDevices()
        for i in devices["devices"]:
            if i["type"] == output:
                self.sp.pause_playback()
                sleep(1)
                self.device_ID = i["id"]
                print(i)
                self.sp.start_playback(device_id=self.device_ID)
                break
    
# class SpotifyListener(QtCore.QThread):
    
#     timer_signal = pyqtSignal()
    
#     def __init__(self, threadID, name):
#         QtCore.QThread.__init__(self, parent=None)   
#         self.threadID = threadID
#         self.name = name
        
#     def run(self):
#         print("Starting " + self.name + "\n\r")
#         while True :
#             time.sleep(1)
#             self.timer_signal.emit()
            
            
