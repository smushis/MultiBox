# -*- coding: utf-8 -*-
import os
import pickle

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

channels = [
    'joueurdugrenier',
    'LinusTechTips',
    'MiniprodFR', # wankil
    'monsieurmv',
    'Vsauce',
    'KoteiLoL', # Kameto
    'ChannelSuperFun',
    # 'TevLouis',
    'LouisSan',
    'IciJapon',
    'physicsgirl',
    'LEROIDESRATS',
    'BestOfCorobizar',
    'tested',
    '3kliksphilip',
    'BestOfAntoineDaniel',
    'Corridor'
    ]

class Youtube(QtCore.QThread): 
    yt_signal = pyqtSignal(dict)
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
        
    def run(self):
        print("Starting " + self.name + "\n\r")
        self.youtube = getToken(path1)
        # ID = self.getUserID('MrNono42100')
        # print("ID= " + ID)
        # self.Subscribe(ID,'MrNono42100')
        self.SubscribeAll()
    
    def getUserID(self, username):
        request = self.youtube.channels().list(
            part="snippet,contentDetails,statistics",
            forUsername=username
        )
        response = request.execute()
        ID = response.get('items',[{}])[0].get('id', 0)
        return ID
    
    def Subscribe(self, ID, username):
        print("Subscribing")
        sub_url = 'https://pubsubhubbub.appspot.com/subscribe'
        youtube_hub = {
            'hub.mode' : 'subscribe',
            'hub.topic' : 'https://www.youtube.com/xml/feeds/videos.xml?channel_id=' + ID,
            'hub.callback' : 'http://85.170.28.49:22220/youtube/user/' + username,
        }
        # print(youtube_hub)
        header = {
            'Content-type' : 'application/x-www-form-urlencoded'
        }
        try:
            r = requests.post(sub_url, headers=header, params=youtube_hub)
            print(r.status_code)
        except:
            print(r)
            print("Not working YT")
            print(r.code_status)
            
    def SubscribeAll(self):
        for i in range(len(channels)):
            username = channels[i]
            ID = self.getUserID(username)
            if ID != 0:
                self.Subscribe(ID, username)
            else:
                print("Problem with username")
            sleep(1)
        print("Sub all finish")
    
    def incomming_Data(self, data):
        print(data)
        
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