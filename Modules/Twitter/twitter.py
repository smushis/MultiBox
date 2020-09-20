# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:55:34 2020

@author: Barmando
"""
from TwitterAPI import TwitterAPI
from pyngrok import ngrok
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

credentials_file = 'Modules/Twitter/twitter_credentials.oauth'

class Twitter(QtCore.QThread):
    twitter_signal = pyqtSignal(dict)
    id = ''
    
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_TOKEN = ''
    ACCESS_TOKEN_SECRET = '' 
    
    ENVNAME = 'AcountActivity'
     
    url_callback = ''
    
    # Important NOTE: After Startup, you need to unsubscribe and resubscribe because the url callback
    # will change
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)     
        self.threadID = threadID
        self.name = name
        if ngrok.get_tunnels() == []:
            ngrok.connect(port="22220")
        tunnels = ngrok.get_tunnels()
        if tunnels[0].public_url.find("https") == -1:
            self.url_callback = tunnels[1].public_url + "/twitter/webhooks"
        else:
            self.url_callback = tunnels[0].public_url + "/twitter/webhooks"
        self.readCredentials()            
        
    def run(self):
        print("Starting " + self.name + "\n\r")
        self.twitterAPI = TwitterAPI(self.CONSUMER_KEY, self.CONSUMER_SECRET, self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        self.deleteWebhooks()
        self.registerWebhooks() 
        self.addSubscription()
        # self.getWebhooks()  
        # self.getSubscription()

    def readCredentials(self):
        with open(credentials_file, "r") as file:
            auth = json.load(file)
        self.CONSUMER_KEY = auth["CONSUMER_KEY"]
        self.CONSUMER_SECRET = auth["CONSUMER_SECRET"]
        self.ACCESS_TOKEN = auth["ACCESS_TOKEN"]
        self.ACCESS_TOKEN_SECRET = auth["ACCESS_TOKEN_SECRET"]
                
    def registerWebhooks(self):
        print("Registering Webhooks")        
        r = self.twitterAPI.request('account_activity/all/:%s/webhooks' % self.ENVNAME, {'url': self.url_callback})
        #print(r.text)
    
    def getWebhooks(self):
        print("Getting Webhooks")
        r = self.twitterAPI.request('account_activity/all/webhooks')  
        a = json.loads(r.text)
        #print(a)
        if a['environments'][0]['webhooks'] == []:
            return -1
        else:
            #print("ID Webhooks=" + a['environments'][0]['webhooks'][0]['id'])
            return a['environments'][0]['webhooks'][0]['id']
        
    def deleteWebhooks(self):
        id = self.getWebhooks()
        if id ==-1:
            print("No Webhooks to delete")
        else:
            print("Deleting Webhooks")        
            r = self.twitterAPI.request('account_activity/all/:%s/webhooks/:%s' % (self.ENVNAME, id))
            #print(r.text)
            #self.getWebhooks()        
        
    def addSubscription(self):
        print("Adding Subscription")        
        r = self.twitterAPI.request('account_activity/all/:%s/subscriptions' % self.ENVNAME, None, None, "POST")
        #print (r.text)
        
    def getSubscription(self):
        print("Verificating subscription")
        r = self.twitterAPI.request('account_activity/all/:%s/subscriptions' % self.ENVNAME, None, None, "GET")
        if r.text == "":
            print("You are already subscribe") 
        else:
            print("You do not have an active subscription")
            
    def getTweet(self, ID):
        print('Récupération du tweet')
        r = self.twitterAPI.request('statuses/show/:%s' %ID)
        print(r.text)
            
    def tweetAnalyzer(self, tweet):
        if "tweet_create_events" in tweet:
            self.tweetCreationEvent(tweet)
        elif "favorite_events" in tweet:
            self.tweetFavoriteEvent(tweet)
        else:
            print("nothing to be done")
            
    def tweetCreationEvent(self, tweet):
        if "user_has_blocked" in tweet:
            print("@Mentions")
            self.analyzeMention(tweet)
        else:
            #print("Tweets, Retweets, Replies, QuoteTweets")
            if tweet["tweet_create_events"][0]["user"]["screen_name"] == "Smushis":
                print("Tweet from yourself")
            elif tweet["tweet_create_events"][0]["text"].find("RT") == 0:
                self.analyzeRetweet(tweet)            
                      
    def analyzeMention(self, tweet):
        user = tweet["tweet_create_events"][0]["user"]["screen_name"]
        data = tweet["tweet_create_events"][0]["text"]
        profile_img = tweet["tweet_create_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
        text =  user + " a répondu à votre tweet! : \n" + data
        print(text)
        if "media" in tweet["tweet_create_events"][0]["entities"]:
            tweet_image_link = tweet["tweet_create_events"][0]["entities"]["media"][0]["media_url"]
            tweet_image_id = tweet["tweet_create_events"][0]["entities"]["media"][0]["id_str"]
            tweet_image_info = {}
            tweet_image_info["link"] = tweet_image_link
            tweet_image_info["id"] = tweet_image_id
            self.twitter_signal.emit(self.createDico("Mention", text, user, profile_img, tweet_image_info))
        else:
            self.twitter_signal.emit(self.createDico("Mention", text, user, profile_img))
        
    def tweetFavoriteEvent(self, tweet):
        user = tweet["favorite_events"][0]["user"]["screen_name"]
        if user != "Smushis":
            profile_img = tweet["favorite_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
            text = user + " a aimé votre tweet!"
            print(text)
            self.twitter_signal.emit(self.createDico("fav", text, user, profile_img))
        else:
            profile_img = tweet["favorite_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
            text = 'Vous avez aimé un tweet'
            print(text)
            self.twitter_signal.emit(self.createDico("fav", text, user, profile_img))
        
    def analyzeRetweet(self, tweet):
        user = tweet["tweet_create_events"][0]["user"]["screen_name"]
        profile_img = tweet["tweet_create_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
        text = user + " a retweeté votre tweet!"
        print(text)
        self.twitter_signal.emit(self.createDico("rt", text, user, profile_img))

    def createDico(self, event, text, username, url, image=None):
        dico = {}
        dico["events"] = event
        dico["username"] = username
        dico["url"] = url
        dico["text"] = text
        dico["media"] = image
        return dico

    def getTweetID(self, event, tweet):
        if event == "fav":
            return tweet["favorite_events"][0]["id"]
        else:
            return tweet["tweet_create_events"][0]["id_str"]
        
    def getTweetURL(self, event, tweet):
        ID = self.getTweetID(event, tweet)
        if event == "fav":
            name = tweet["favorite_events"][0]["user"]["screen_name"]
        else:
            name = tweet["tweet_create_events"][0]["user"]["screen_name"]        
        url = "https://twitter.com/" + name +"/status/" + ID
        return url
    
    def getOEmbedURL(self, event, tweet):
        #print(tweet)
        url = self.getTweetURL(event, tweet)
        print(url)
        r = self.twitterAPI.request('statuses/oembed', {'url': url})
        return r.json()["html"]