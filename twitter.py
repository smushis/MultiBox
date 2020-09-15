# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:55:34 2020

@author: Barmando
"""
import threading
from TwitterAPI import TwitterAPI
from pyngrok import ngrok
import json

class Twitter(threading.Thread):
    
    id = ''
    CONSUMER_KEY = 'PHAt5klX2nYAPz1fGERYNBOYj'
    CONSUMER_SECRET = 'jMtbs9kGnr12zfKdDWiwP7rs5Leb04oxiAELwcF5qV99aVhnK4'
    ACCESS_TOKEN = '1050882356-O0vVTvBQWPlHU5FyCQUhwYZs47RA7xf4SL1Ippp'
    ACCESS_TOKEN_SECRET = 'QYxRmRkG42z1nOg3four99AbwWJRsq8HsRas16NPH5rh8' 
    
    ENVNAME = 'AcountActivity'
     
    url_callback = ''
      
    twitterAPI = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    # Important NOTE: After Startup, you need to unsubscribe and resubscribe because the url callback
    # will change
    
    def __init__(self, threadID, name, GUI):
        threading.Thread.__init__(self, name=name)        
        self.threadID = threadID
        self.name = name
        self.GUI = GUI
        if ngrok.get_tunnels() == []:
            ngrok.connect(port="22220")
        tunnels = ngrok.get_tunnels()
        if tunnels[0].public_url.find("https") == -1:
            self.url_callback = tunnels[1].public_url + "/twitter/webhooks"
        else:
            self.url_callback = tunnels[0].public_url + "/twitter/webhooks"            
        
    def run(self):
        print("Starting " + self.name + "\n\r")
        # self.deleteWebhooks()
        # self.registerWebhooks() 
        # self.addSubscription()
        # self.getWebhooks()  
        # self.getSubscription()
                
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
        text = tweet["tweet_create_events"][0]["text"]
        profile_img = tweet["tweet_create_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
        print(user + " a répondu à votre tweet! : " + text)
        self.GUI.printTweet(user, text)
        
    def tweetFavoriteEvent(self, tweet):
        user = tweet["favorite_events"][0]["user"]["screen_name"]
        if user != "Smushis":
            profile_img = tweet["favorite_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
            print(user + " a aimé votre tweet!")
            self.GUI.printFavTweet(user)
        else:
            print('Vous avez aimé un tweet')
            self.GUI.printFavTweet("Smushis")
        
    def analyzeRetweet(self, tweet):
        user = tweet["tweet_create_events"][0]["user"]["screen_name"]
        profile_img = tweet["tweet_create_events"][0]["user"]["profile_image_url"].replace("normal", "200x200")
        print(user + " a retweeté votre tweet!")              