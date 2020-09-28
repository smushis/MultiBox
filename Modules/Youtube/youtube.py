# -*- coding: utf-8 -*-
import os
import pickle
import json

import requests
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

from time import sleep

path0 = 'token.pickle'
path1 = 'Modules/Youtube/token.pickle'
webhooks_file = 'Modules/Youtube/webhooks.json'

channels = [
    'joueurdugrenier',
    'LinusTechTips',
    'MiniprodFR', # wankil
    'monsieurmv',
    'Vsauce',
    'KoteiLoL', # Kameto
    'ChannelSuperFun',
    'Tev & Louis',
    'Louis-San',
    'IciJapon',
    'Physics Girl',
    'LE ROI DES RATS',
    'Best Of Corobizar',
    'Adam Savage’s Tested',
    '3kliksphilip',
    'BestOfAntoineDaniel',
    'Corridor',
    'Alderiate'
    ]

class Youtube(QtCore.QThread): 
    yt_signal = pyqtSignal(dict)
    
    webhooks = {}
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
        
    def run(self):
        print("Starting " + self.name + "\n\r")
        self.youtube = getToken(path1)
        self.list = self.getSubscriptionsList()
        # self.SubscribeAll()
        # ID = self.getUserID('MrNono42100')
        # print("ID= " + ID)
        # self.Subscribe(ID,'MrNono42100')
    
    def getUserID(self, username):
        request = self.youtube.channels().list(
            part="snippet,contentDetails,statistics",
            forUsername=username
        )
        response = request.execute()
        ID = response.get('items',[{}])[0].get('id', 0)
        if ID == 0:
            self.list = self.getSubscriptionsList()
            if username in self.list:
                ID = self.list[username]
        return ID
    
    def sub_unsub(self, ID, username, mode):
        print("Subscribing")
        sub_url = 'https://pubsubhubbub.appspot.com/subscribe'
        youtube_hub = {
            'hub.mode' : mode,
            'hub.topic' : 'https://www.youtube.com/xml/feeds/videos.xml?channel_id=' + ID,
            'hub.callback' : 'http://85.170.28.49:22220/youtube/user/' + username,
            'hub.lease_seconds' : 10000
        }
        # print(youtube_hub)
        header = {
            'Content-type' : 'application/x-www-form-urlencoded'
        }
        try:
            r = requests.post(sub_url, headers=header, params=youtube_hub)
            if mode == "subscribe":
                self.webhooks.update({username : youtube_hub})
            elif mode == "unsubscribe":
                del self.webhooks[username]
                
        except:
            print(r)
            print("Not working YT")
            print(r.code_status)
            
    def Subscribe(self, ID, username):
        self.sub_unsub(ID, username, 'subscribe')
            
    def Unsubscribe(self, ID, username):
        self.sub_unsub(ID, username, 'unsubscribe')

    def SubscribeList(self):
        for i in range(len(channels)):
            username = channels[i]
            ID = self.getUserID(username)
            if ID != 0:
                self.Subscribe(ID, username)
            else:
                print("Problem with username: " + username)
            sleep(1)
        print("Sub all finish")
        
    # def SubscribeAll(self):
        for i in self.list:
            self.Subscribe(self.list[i], i)
        
    def updateWebhooks(self):
        with open(webhooks_file, "w") as file:
            json.dump(self.webhooks, file)              
        
    def getSubscriptionsList(self):
        subList = {}
        
        request = self.youtube.subscriptions().list(
            part="snippet,contentDetails",
            maxResults=50,
            mine=True,
            order="alphabetical"
        )        
        response = request.execute()
        next_page = True
        while next_page:
            for i in range(len(response["items"])):
                # subList.append({"Name" : response["items"][i]["snippet"]["title"], "ID" : response["items"][i]["id"]}) 
                subList.update({response["items"][i]["snippet"]["title"] : response["items"][i]["snippet"]["resourceId"]["channelId"]}) 
            if "nextPageToken" in response:
                request = self.youtube.subscriptions().list(
                    part="snippet,contentDetails",
                    maxResults=50,
                    mine=True,
                    order="alphabetical",
                    pageToken=response["nextPageToken"]
                )      
                response = request.execute()                  
            else:   
                next_page = False          
        # print(subList)            
        return subList
    
    def getVideoByID(self, ID):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=ID
        )
        response = request.execute()  
        return response
    
    def getChannelByID(self, user_id):
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=user_id
        )
        response = request.execute()
        return response        
    
    def getImageChannel(self, user_id):
        channel = self.getChannelByID(user_id)
        return channel.get("items", [{}])[0].get("snippet", {}).get("thumbnails", {}).get("medium", "no url")
        
        
    def incomming_Data(self, data):
        video_id = data["feed"]["entry"]["yt:videoId"]
        info = self.getVideoByID(video_id)
        title = info.get("items",[{}])[0].get("snippet",{}).get("title","No title available")
        user = info.get("items",[{}])[0].get("snippet",{}).get("channelTitle","")
        user_id = data["feed"]["entry"]["yt:channelId"]
        url = self.getImageChannel(user_id)
        self.yt_signal.emit(self.createDico(title, user, user_id, url))
        
    def createDico(title, username, user_id, img_user):
        dico = {}
        dico["title"] = title
        dico["username"] = username
        dico["user_id"] = user_id
        dico["url"] = img_user
        return dico
    
def getToken(path):
    api_service_name = "youtube"
    api_version = "v3"

    credentials = None

    # token.pickle stores the user's credentials from previously successful logins
    if os.path.exists(path):
        print('Loading Credentials From File...')
        with open(path, 'rb') as token:
            credentials = pickle.load(token)
      
    # If there are no valid credentials available, then either refresh the token or log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing Access Token...')
            credentials.refresh(Request())
        else:
            print('Fetching New Tokens...')
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                'Modules/Youtube/client_secrets.json',
                scopes=[
                    'https://www.googleapis.com/auth/youtube.readonly'
                ]
            )
    
            flow.run_local_server(port=8080, prompt='consent',
                                  authorization_prompt_message='')
            credentials = flow.credentials
    
            # Save the credentials for the next run
            with open(path, 'wb') as f:
                print('Saving Credentials for Future Use...')
                pickle.dump(credentials, f)
                
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
    return youtube

if __name__ == "__main__":
    
    youtube = getToken(path0)             
    request = youtube.subscriptions().list(
        part="snippet,contentDetails",
        mine=True
    )
    response = request.execute()
    print(response)