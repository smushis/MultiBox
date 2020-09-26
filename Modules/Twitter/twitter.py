# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:55:34 2020

@author: Barmando
"""
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterRequestError
from pyngrok import ngrok
import json
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

credentials_file = 'Modules/Twitter/twitter_credentials.oauth'

class Twitter(QtCore.QThread):
    twitter_signal = pyqtSignal(dict)
    id = ''
    
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_TOKEN = ''
    ACCESS_TOKEN_SECRET = '' 
    
    ENVNAME = ''
     
    url_callback = ''
    
    username ='Smushis' #Your @
    
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
        self.ENVNAME = auth["ENVNAME"]
                
    def registerWebhooks(self):
        try:
            print("Registering Twitter Webhooks")        
            r = self.twitterAPI.request('account_activity/all/:%s/webhooks' % self.ENVNAME, {'url': self.url_callback})
        except TwitterRequestError as error:
            code = error.status_code
            if code == 403:
                print(r.json())
            else:
                print("Non expected problem during registering webhooks")
        #print(r.text)
    
    def getWebhooks(self):
        try:
            print("Getting Twitter Webhooks")
            r = self.twitterAPI.request('account_activity/all/webhooks')  
            a = json.loads(r.text)
            #print(a)
            if a['environments'][0]['webhooks'] == []:
                return -1
            else:
                #print("ID Webhooks=" + a['environments'][0]['webhooks'][0]['id'])
                return a['environments'][0]['webhooks'][0]['id']
        except TwitterRequestError as error:
            code = error.status_code
            if code == 99:
                print(r.json())
            else:
                print("Non expected problem during getting webhooks")
                
    def deleteWebhooks(self):
        try:
            id = self.getWebhooks()
            if id ==-1:
                print("No Twitter Webhooks to delete")
            else:
                print("Deleting Twitter Webhooks")        
                r = self.twitterAPI.request('account_activity/all/:%s/webhooks/:%s' % (self.ENVNAME, id))
        except:
            print("Problem during deleting webhooks from Twitter")
            print(r.json())
        
    def addSubscription(self):
        try:
            print("Adding Subscription")        
            r = self.twitterAPI.request('account_activity/all/:%s/subscriptions' % self.ENVNAME, None, None, "POST")
            #print (r.text)
        except TwitterRequestError as error:
            code = error.status_code
            if code == 348:
                print("Access to user's webhook not permitted")
            else:
                print("Non expected problem during getting webhooks")            
                print(r.json())
                
    def getSubscription(self):
        try:
            print("Verificating subscription")
            r = self.twitterAPI.request('account_activity/all/:%s/subscriptions' % self.ENVNAME, None, None, "GET")
            if r.text == "":
                print("You are already subscribe") 
            else:
                print("You do not have an active subscription")
        except TwitterRequestError as error:
            code = error.status_code
            if code == 99:
                print("You don't have access to this ressource")
            else:
                print("Non expected problem during getting webhooks")            
                print(r.json())            
            
    def getTweet(self, ID):
        try:
            print('Getting tweet')
            r = self.twitterAPI.request('statuses/show/:%s' %ID)
            #print(r.text)
            return(r.json())
        except TwitterRequestError:
            print("Non expected problem during getting the tweet")            
            print(r.json())              
            
    def tweetAnalyzer(self, tweet):
        if "tweet_create_events" in tweet:
            self.tweetCreationEvent(tweet)
        elif "favorite_events" in tweet:
            self.tweetFavoriteEvent(tweet)
        elif "direct_message_events" in tweet:
            self.analyzeDM(tweet)
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
        data = tweet["tweet_create_events"][0]["text"].split(self.username,1)[1]
        profile_img = tweet["tweet_create_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
        text =  user + " responded to your tweet! : \n" + data
        print(text)
        if "media" in tweet["tweet_create_events"][0]["entities"]:
            tweet_media = {}
            tweet_media["link"] = tweet["tweet_create_events"][0]["entities"]["media"][0]["media_url"]
            tweet_media["id"] = tweet["tweet_create_events"][0]["entities"]["media"][0]["id_str"]
            tweet_media["type"] = tweet["tweet_create_events"][0]["entities"]["media"][0]["type"]           
            if tweet_media["type"] == "photo":
                self.twitter_signal.emit(self.createDico("Mention", text, user, profile_img, tweet_media))
            else:
                print(tweet_media["type"] + "is not currently supported")     
        else:
            self.twitter_signal.emit(self.createDico("Mention", text, user, profile_img))
        
    def tweetFavoriteEvent(self, tweet):
        user = tweet["favorite_events"][0]["user"]["screen_name"]
        if user != "Smushis":
            profile_img = tweet["favorite_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
            text = user + " liked your tweet!"
            print(text)
            msg = self.getTweet(tweet["favorite_events"][0]["favorited_status"]["id_str"])["text"] 
            if "media" in tweet["favorite_events"][0]["favorited_status"]["entities"]:
                tweet_media = {}
                tweet_media["link"] = tweet["favorite_events"][0]["favorited_status"]["entities"]["media"][0]["media_url"]
                tweet_media["id"] = tweet["favorite_events"][0]["favorited_status"]["entities"]["media"][0]["id_str"] 
                tweet_media["type"] = ["favorite_events"][0]["favorited_status"]["entities"]["media"][0]["type"]
                if tweet_media["type"] == "photo":
                    self.twitter_signal.emit(self.createDico("fav", text + "\n" + msg, user, profile_img, tweet_media))
                else:
                    print(tweet_media["type"] + "is not currently supported")
            else:
                self.twitter_signal.emit(self.createDico("fav", text + "\n" + msg, user, profile_img))
        else:
            profile_img = tweet["favorite_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
            text = 'You liked a tweet!'
            print(text)
            # msg = self.getTweet(tweet["favorite_events"][0]["favorited_status"]["id_str"])["text"]
            # self.twitter_signal.emit(self.createDico("fav", text + "\n" + msg, user, profile_img))
        
    def analyzeRetweet(self, tweet):
        user = tweet["tweet_create_events"][0]["user"]["screen_name"]
        profile_img = tweet["tweet_create_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
        text = user + " retweeted your tweet! \n"
        msg = tweet["tweet_create_events"][0]["text"].split(self.username, 1)[1]
        if "media" in tweet["tweet_create_events"][0]["entities"]:
            tweet_media = {}
            tweet_media["link"] = tweet["tweet_create_events"][0]["entities"]["media"][0]["media_url"]
            tweet_media["id"] = tweet["tweet_create_events"][0]["entities"]["media"][0]["id_str"]
            tweet_media["type"] = tweet["tweet_create_events"][0]["entities"]["media"][0]["type"]
            self.twitter_signal.emit(self.createDico("rt", text + msg, user, profile_img, tweet_media))
        else:
            self.twitter_signal.emit(self.createDico("rt", text + msg, user, profile_img))
        
    def analyzeDM(self, tweet):
        ID_Sender = tweet.get("direct_message_events",[{}])[0].get('message_create', {}).get("sender_id")
        user = tweet.get('users', {}).get(ID_Sender, {}).get('screen_name', "No Name")
        msg = tweet.get("direct_message_events",[{}])[0].get('message_create', {}).get("message_data", {}).get("text", "Error with DM")
        profile_img = tweet.get('users', {}).get(ID_Sender, {}).get('profile_image_url', None)
        text = user + " send you a DM! \n" + msg
        if "media" in tweet['direct_message_events'][0]["message_create"]["message_data"]["attachment"]:
            tweet_media = {}
            tweet_media["link"] = tweet['direct_message_events'][0]["message_create"]["message_data"]["attachment"]["media"]['media_url']
            tweet_media["id"] = tweet['direct_message_events'][0]["message_create"]["message_data"]["attachment"]["media"]['id_str']
            tweet_media["type"] = tweet['direct_message_events'][0]["message_create"]["message_data"]["attachment"]["media"]['type']
            self.twitter_signal.emit(self.createDico("dm", text, user, profile_img, tweet_media))
        else:
            self.twitter_signal.emit(self.createDico("dm", text, user, profile_img))
        return self.createDico("dm", text, user, profile_img, tweet_media)
        
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
            return tweet["favorite_events"][0]["favorited_status"]["id_str"]
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