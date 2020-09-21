# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:22:49 2020

@author: Barmando
"""
# Importing libraries
import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from time import time, sleep

credentials_file = 'Modules/Twitch/twitch_credentials.oauth'

class Twitch(QtCore.QThread):
    twitch_signal = pyqtSignal(dict)

    url_streams = 'https://api.twitch.tv/helix/streams'
    url_hub = 'https://api.twitch.tv/helix/webhooks/hub'
    url_id = 'https://api.twitch.tv/helix/users?login='
    url_name = 'https://api.twitch.tv/helix/users?id='
    url_photo = 'https://api.twitch.tv/helix/users?login='
    url_sub = 'https://api.twitch.tv/helix/webhooks/subscriptions'
    url_follows = "https://api.twitch.tv/helix/users/follows?from_id="
    url_games = 'https://api.twitch.tv/helix/games?id='
    
    Client_ID = ''
    SecretKey = ''
    callback = ''
    
    twitch_app_token_json = {}
    
    follows_list = [] #
    follows_live = []
    
    user = "Smushis"
    #ayaya
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
        self.readCredentials()
        self.startTime = time()

    def run(self):
        print("Starting " + self.name + "\n\r")
        self.authorize()
        #self.getSubList()
        #self.fullUnsub()
        # self.SubscribeAllFollows()
        self.initStateLive()
        self.subToUser()
        
    def readCredentials(self):
        with open(credentials_file, "r") as file:
            auth = json.load(file)
        self.SecretKey = auth["SecretKey"]
        self.Client_ID = auth["Client_ID"]
        self.callback = auth["callback"]
        
    #Oauth token
    def authorize(self):
        token_params = {
            'client_id': self.Client_ID,
            'client_secret': self.SecretKey,
            'grant_type': 'client_credentials'
        }
        app_token_request = requests.post('https://id.twitch.tv/oauth2/token', params=token_params)
        self.twitch_app_token_json = app_token_request.json()

    def getOAuthHeader(self):
        if (time() - self.startTime) > self.twitch_app_token_json['expires_in']:
           self.authorize()
           print("regenerate token")
        return {
            'client-id': self.Client_ID,
            'Authorization': 'Bearer ' + self.twitch_app_token_json['access_token']
        } 

    def Subscribe(self, ID):
        username = self.getUsername(ID)
        if username != -1:
            twitch_hub = {
                'hub.callback': self.callback + username,
                'hub.mode': 'subscribe',
                'hub.topic': self.url_streams +'?user_id=' + ID,
                'hub.lease_seconds': 800000,
                'hub.secret': self.Client_ID
            } 
            twitch_hub_json = json.dumps(twitch_hub)
            requests.post(self.url_hub, headers=self.getOAuthHeader(), data = twitch_hub_json)
        
    def Unsubscribe(self, callback, topic):
        #ID = self.getUserID("shroud")          
        twitch_hub = {
            'hub.callback': callback,
            'hub.mode': 'unsubscribe',
            'hub.topic': topic,
            'hub.lease_seconds': 800000,
            'hub.secret': self.Client_ID
        }            
        twitch_hub_json = json.dumps(twitch_hub)
        requests.post(self.url_hub, headers=self.getOAuthHeader(), data = twitch_hub_json)
        #self.follows_list.remove(ID)
        
    def getStreamInfo(self, user):    
        twitch_txt = requests.get(self.url_id + user, headers=self.getOAuthHeader())
        twitch_json = twitch_txt.json()
        stream_json = twitch_json["data"][0]     
        return stream_json
    
    def getUserID(self, user):
        stream_json = self.getStreamInfo(user)
        return stream_json["id"]
    
    def getSubList(self, pagination=0):
        if pagination !=0:
            resp = requests.get(self.url_sub + "?after=" + pagination, headers=self.getOAuthHeader())
        else:
            resp = requests.get(self.url_sub, headers=self.getOAuthHeader())
            print(resp.json()["total"])
        return resp.json()
             
    def getUserFollows(self):   
        resp = requests.get(self.url_follows + "36365680" + "&first=100", headers=self.getOAuthHeader())
        #print(resp.json())
        i = resp.json()["total"]
        for j in range((i//100)+1):
            prev_resp = resp.json()    
            for h in range(len(prev_resp["data"])):              
                self.follows_list.append(prev_resp['data'][h]["to_id"])
            pag = prev_resp["pagination"]["cursor"]
            resp = requests.get(self.url_follows + "36365680&after=" + pag + "&first=100", headers=self.getOAuthHeader())
        print("Fin Recup Follow\r")

    def SubscribeAllFollows(self):
        self.getUserFollows()
        print("Début Subscribe\r")
        for i in range(len(self.follows_list)):
            #print(self.follows_list[i])
            self.Subscribe(self.follows_list[i])
        self.getSubList()

    def getUsername(self, ID):              
        twitch_txt = requests.get(self.url_name + str(ID), headers=self.getOAuthHeader())
        twitch_json = twitch_txt.json()
        #print(twitch_json)
        if twitch_json["data"] == []:
            print("Problème ID=" + str(ID))
            return -1
        else:    
            username = twitch_json["data"][0]["login"] 
            return username
        
    def subToUser(self):
        ID = self.getUserID(self.user)
        self.Subscribe(ID)
            
    def incoming_data(self, data, username):
        if data['data'] == []:
            print(username + " is offline !")
            #self.twitch_signal.emit(username + " is offline !")
            dico = self.search_username(username)
            if dico == False:
                self.follows_live.append({'Name':username, 'Live?':False})           
            else:
                    dico['Live?'] = False        
        else:
            dico = self.search_username(username)
            if dico == False:
                self.follows_live.append({'Name':username, 'Live?':True})           
                text = username + " is live !"
                game = self.getGameTitle(data["data"][0]["game_id"])
                text = username + " is live playing " + game +"!"
                title = data["data"][0]["title"]
                print(text)
                profile_img = self.getProfileImage(username)
                self.twitch_signal.emit(self.createDico(text, username, profile_img, title))
            else:
                if dico['Live?'] == False:
                    dico['Live?'] = True
                    game = self.getGameTitle(data["data"][0]["game_id"])
                    text = username + " is live playing " + game +" !"
                    title = data["data"][0]["title"]
                    print(text)
                    profile_img = self.getProfileImage(username)
                    self.twitch_signal.emit(self.createDico(text, username, profile_img, title))
                    
    def search_username(self, username):
        for dico in self.follows_live:
            if(username == dico['Name']):
                return dico              
        return False
    
    def fullUnsub(self):
        resp = self.getSubList()
        total = resp["total"]
        print("total= " + str(total))
        print("Debut unsub")
        for j in range(total//20 +1):
            print("Unsub page =" + str(j))
            prev_resp = resp
            for h in range(len(prev_resp["data"])):
                self.Unsubscribe(prev_resp["data"][h]["callback"], prev_resp["data"][h]["topic"])
            pag = prev_resp["pagination"]["cursor"]
            if pag == None:
                print(self.getSubList()["total"])
                break
            resp = self.getSubList(pag)
        print(self.getSubList()["total"])
        
    def initStateLive(self):
        self.getUserFollows()
        print("Init Streams")
        for i in self.follows_list:
            r = requests.get(self.url_streams + "?user_id=" + i, headers = self.getOAuthHeader())
            if r.json()["data"] == []:
                name = self.getUsername(i)
                if name !=-1:
                    self.follows_live.append({'Name': self.getUsername(i), 'Live?':False})
            else:
                self.follows_live.append({'Name':r.json()["data"][0]["user_name"], 'Live?':True}) 
        print("Fin init")
        
    def getProfileImage(self, username):
        r = requests.get(self.url_photo + username, headers = self.getOAuthHeader())
        #print(r.json()["data"][0]["profile_image_url"])
        return r.json()["data"][0]["profile_image_url"]
    
    def getGameTitle(self, ID):
        r = requests.get(self.url_games + ID, headers = self.getOAuthHeader())
        return r.json()["data"][0]["name"]
        
    def createDico(self, text, username, url, title):
        dico = {}
        dico["username"] = username
        dico["url"] = url
        dico["text"] = text
        dico["title"] = title
        return dico        
                   