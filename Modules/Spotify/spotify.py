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
    play_pause_signal = pyqtSignal(bool)
    stat_signal = pyqtSignal(list)
    
    scope = "user-read-playback-state user-modify-playback-state user-top-read"
    DEFAULT_DEVICE = ""
    token = ""
    device_ID = ""
    sleep_count = 0
    playing = True # play = true, pause = false
     
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
        self.showDevices()
        # self.getCurrentTopArtist("short_term")
        i = 0
        self.sendStats()
        while True:
            i += 1
            self.getCurrentTrack()
            sleep(0.5)
            if i == 14000:
                self.sendStats()
                   
    def readToken(self):      
        with open(token_file, 'r') as file:
            auth = json.load(file)           
        self.token = auth["token"]  
        
    def sendStats(self):
        list_ = []
        list_[0] = self.getCurrentTopArtist(time_range="short_term", max_limit=5)
        list_[1] = self.getCurrentTopTracks(time_range="short_term", max_limit=5)
        self.stat_signal.emit(list_)
        
    def showDevices(self):
        try:
            res = self.sp.devices()
            if res["devices"]!= []:
                return res
            else:
                #print("No devices")
                return {"devices": [{"is_active" : False}]}
        except SpotifyException as E:
            if E.http_status == 404:
                print("No Device Active")
                return {"devices": [{"is_active" : False}]}
            elif E.http_status == 401:
                self.refreshToken()
                return {"devices": [{"is_active" : False}]}
                
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
                artist = tr.get("item",{}).get('artists',[{}])[0].get('name','Unknown Artist')
                track = tr.get("item",{}).get('name', 'Unknown Track')
                img_album = tr.get("item", {}).get("album", {}).get("images", [{}])[1].get("url",'')
                album = tr.get("item", {}).get("album",{}).get("id", 0)
                self.Spotify_signal.emit(self.createDico(artist, track, img_album, album))
                if self.sleep_count == 0:
                    self.idle_spoti_signal.emit(False)
                if tr.get("is_playing", False):
                    self.playing = True
            else :
                if self.sleep_count < 5:
                    print("No playing track, retrying in 5s")
                    self.sleep_count += 1
                    self.playing = False
                    sleep(5)
                else:
                    print("Idle until Device is Active again")
                    self.idle_spoti_signal.emit(True)
                    while(not(self.showDevices().get("devices",[{}])[0].get('is_active', False))):
                        sleep(5)
                    self.sleep_count = 0
        except SpotifyException as e:
            sleep(10)
            return self.handleException(e)
        except exceptions.ReadTimeout:
            print("Timeout during getting current track")
        except AttributeError :
            print("Like wtf is the program doing")
        
            
    def handleException(self, e):
        if e.http_status == 404:
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
            if i.get("type", "nothing") == output:
                self.sp.pause_playback()
                sleep(1)
                self.device_ID = i["id"]
                print(i)
                self.sp.start_playback(device_id=self.device_ID)
                break
    
    def getCurrentTopArtist(self, time_range='long_term', max_limit=None):
        data = self.sp.current_user_top_artists(time_range=time_range)
        text = ""
        for i in range(len(data.get("items", [{}]))):     
            text += "#" + str(i+1) + " "+ data.get("items", [{}])[i].get("name", "No name") + '\n'
            if i == max_limit:
                break
        return text
        
    def getCurrentTopTracks(self, time_range='long_term', max_limit=None):
        text = ""
        data = self.sp.current_user_top_tracks(time_range=time_range)
        for i in range(len(data.get("items", [{}]))):
            dico = {}
            dico['track'] = data.get("items", [{}])[i].get("name", "No name")
            dico['album'] = data.get("items", [{}])[i].get("album", {}).get('name', "no album name")
            dico['artists'] = data.get("items", [{}])[i].get("artists", [{}])[0].get('name', "no artists")        
            text += "#" + str(i+1) + " "+ dico["track"] + '\n'
            if i == max_limit:
                break
        return text
            
    def playMusic(self, uri=None):
        try:
            self.sp.start_playback(uris=uri)
        except SpotifyException as e:
            self.handleException(e)
        except exceptions.ReadTimeout:
            print("Timeout during getting current track")
        except AttributeError :
            print("Like wtf is the program doing")
            
    def pauseMusic(self):
        try:
            self.sp.pause_playback()
        except SpotifyException as e:
            self.handleException(e)
        except exceptions.ReadTimeout:
            print("Timeout during getting current track")
        except AttributeError :
            print("Like wtf is the program doing")
            
    def play_pause(self):
        if self.playing:
            self.pauseMusic()
            self.play_pause_signal.emit(False)
            self.playing = False
        else:
            self.playMusic()
            self.play_pause_signal.emit(True)
            self.playing = True
            
    def nextTrack(self):
        try:
            self.sp.next_track()
        except SpotifyException as e:
            self.handleException(e)
        except exceptions.ReadTimeout:
            print("Timeout during getting current track")
        except AttributeError :
            print("Like wtf is the program doing") 
            
    def prevTrack(self):
        try:
            self.sp.previous_track()
        except SpotifyException as e:
            self.handleException(e)
        except exceptions.ReadTimeout:
            print("Timeout during getting current track")
        except AttributeError :
            print("Like wtf is the program doing")            
            
            

            
            
