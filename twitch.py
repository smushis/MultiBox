# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:22:49 2020

@author: Barmando
"""
# Importing libraries
import requests
import threading
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

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
    
    twitch_app_token_json = {}
    
    follows_list = [] #
    follows_live = []
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
        self.SecretKey = 'zf587mdfjjflqyfceevk9vom1h71ze'
        self.Client_ID = '8q8so0fn0nr5ujbt27phhbum8wks52'

    def run(self):
        print("Starting " + self.name + "\n\r")
        #self.initStateLive()
        #print("ID = " + id)
        #self.fullUnsub()
        #self.getNotif()
        #self.getUnsub('552015849')      
        #self.getNotifAllFollows()
        #self.getUnsubAllFollows()
        #self.getSubAllFollows()
        
    #Oauth token
    def authorize(self):
        token_params = {
            'client_id': self.Client_ID,
            'client_secret': self.SecretKey,
            'grant_type': 'client_credentials',
        }
        app_token_request = requests.post('https://id.twitch.tv/oauth2/token', params=token_params)
        self.twitch_app_token_json = app_token_request.json()
        return self.twitch_app_token_json

    def getOAuthHeader(self):
        return {
            'client-id': self.Client_ID,
            'Authorization': 'Bearer ' + self.twitch_app_token_json['access_token']
        }   

    def getSub(self, ID):
        self.authorize()
        username = self.getUsername(ID)
        if username != -1:
            twitch_header = {
                'client-id': self.Client_ID,
                "Content-Type":"application/json", 
                'Authorization': 'Bearer ' + self.twitch_app_token_json['access_token']            
            }
            twitch_hub = {
                'hub.callback': 'http://85.170.28.49:22220/twitch/user/' + username,
                'hub.mode': 'subscribe',
                'hub.topic': self.url_streams +'?user_id=' + ID,
                'hub.lease_seconds': 800000
            } 
            twitch_hub_json = json.dumps(twitch_hub)
            requests.post(self.url_hub, headers=twitch_header, data = twitch_hub_json)
        
    def getUnsub(self, ID, callback, topic):
        #ID = self.getUserID("shroud")
        self.authorize()
        twitch_header = {
            'client-id': self.Client_ID,
            "Content-Type":"application/json", 
            'Authorization': 'Bearer ' + self.twitch_app_token_json['access_token']            
        }
        if ID != 0:
            print("Par ID")
            twitch_hub = {
                'hub.callback': callback,
                'hub.mode': 'unsubscribe',
                'hub.topic': topic,
                'hub.lease_seconds': 800000
            }
        else:
            print("Par URL")            
            twitch_hub = {
                'hub.callback': callback,
                'hub.mode': 'unsubscribe',
                'hub.topic': topic,
                'hub.lease_seconds': 800000
            }            
        twitch_hub_json = json.dumps(twitch_hub)
        requests.post(self.url_hub, headers=twitch_header, data = twitch_hub_json)
        #self.follows_list.remove(ID)
        
    def getStreamInfo(self, user):    
        self.authorize()       
        twitch_header = {
            'client-id': self.Client_ID,
            'Authorization': 'Bearer ' + self.twitch_app_token_json['access_token']
        }        
        twitch_txt = requests.get(self.url_id + user, headers=twitch_header)
        twitch_json = twitch_txt.json()
        stream_json = twitch_json["data"][0]     
        return stream_json
    
    def getUserID(self, user):
        stream_json = self.getStreamInfo(user)
        return stream_json["id"]
    
    def getSubList(self, pagination):
        self.authorize()       
        twitch_header = {
            'client-id': self.Client_ID,
            'Authorization': 'Bearer ' + self.twitch_app_token_json['access_token']
        }
        if pagination !=0:
            resp = requests.get(self.url_sub + "?after=" + pagination, headers=twitch_header)
        else:
            resp = requests.get(self.url_sub, headers=twitch_header)
        print(resp.json())
        return resp.json()
             
    def getUserFollows(self):
        self.authorize()
        twitch_header = {
            'client-id': self.Client_ID,
            'Authorization': 'Bearer ' + self.twitch_app_token_json['access_token']
        }       
        resp = requests.get(self.url_follows + "36365680" + "&first=100", headers=twitch_header)
        #print(resp.json())
        i = resp.json()["total"]
        print("indice =", i)
        for j in range((i//100)+1):
            prev_resp = resp.json()    
            for h in range(len(prev_resp["data"])):              
                self.follows_list.append(prev_resp['data'][h]["to_id"])
            pag = prev_resp["pagination"]["cursor"]
            resp = requests.get(self.url_follows + "36365680&after=" + pag + "&first=100", headers=twitch_header)
        print("Fin Recup Follow\r")

    def getSubAllFollows(self):
        self.getUserFollows()
        print("Début Subscribe\r")
        for i in range(len(self.follows_list)):
            #print(self.follows_list[i])
            self.getSub(self.follows_list[i])
        self.getSubList()

    def getUsername(self, ID):
        self.authorize()       
        twitch_header = {
            'client-id': self.Client_ID,
            'Authorization': 'Bearer ' + self.twitch_app_token_json['access_token']
        }        
        twitch_txt = requests.get(self.url_name + str(ID), headers=twitch_header)
        twitch_json = twitch_txt.json()
        #print(twitch_json)
        if twitch_json["data"] == []:
            print("Problème ID=" + str(ID))
            return -1
        else:    
            username = twitch_json["data"][0]["login"] 
            return username
            
    def incoming_data(self, data, username):
        if data['data'] == []:
            print(username + " is offline !")
            #self.twitch_signal.emit(username + " is offline !")
            dico = self.search_username(username)
            if dico == False:
                self.follows_live.append({'Name':username, 'Live?':False})           
            else:
                if dico['Live?'] == True:
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
        resp = self.getSubList(0)
        total = resp["total"]
        print("total= " + str(total))
        print("Debut unsub")
        for j in range(total//20 +1):
            print("j=" + str(j))
            prev_resp = resp
            for h in range(len(prev_resp["data"])):
                self.getUnsub(0, prev_resp["data"][h]["callback"], prev_resp["data"][h]["topic"])
            pag = prev_resp["pagination"]["cursor"]
            resp = self.getSubList(pag)
        resp = self.getSubList(0)
        
    def initStateLive(self):
        self.authorize()
        self.getUserFollows()
        print("Init Streams")
        for i in self.follows_list:
            r = requests.get(self.url_streams + "?user_id=" + i, headers = self.getOAuthHeader())
            if r.json()["data"] == []:
                self.follows_live.append({'Name': self.getUsername(i), 'Live?':False})                 
            else:
                self.follows_live.append({'Name':r.json()["data"][0]["user_name"], 'Live?':True})  
        print("Fin init")
        
    def getProfileImage(self, username):
        self.authorize()
        r = requests.get(self.url_photo + username, headers = self.getOAuthHeader())
        #print(r.json()["data"][0]["profile_image_url"])
        return r.json()["data"][0]["profile_image_url"]
    
    def getGameTitle(self, ID):
        self.authorize()
        r = requests.get(self.url_games + ID, headers = self.getOAuthHeader())
        return r.json()["data"][0]["name"]
        
    def createDico(self, text, username, url, title):
        dico = {}
        dico["username"] = username
        dico["url"] = url
        dico["text"] = text
        dico["title"] = title
        return dico        
            
        