# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:36:43 2020

@author: Barmando
"""
import flask
import base64
import hashlib
import hmac
import json
import sys


from flask import request
from flask import Response
from Modules.GUI.GUI2 import Ui_MainWindow
from PyQt5 import  QtWidgets

from constants import Twitter_, Spotify_, Twitch_, HTML_, Weather_, TEMP_ON, GUI_, Youtube_

app = flask.Flask("Webhooks listener")
app.config["DEBUG"] = False


# Logger
# import logging
# logger = logging.getLogger("werkzeug")
# logger.setLevel(logging.ERROR)


@app.route('/twitch/user/<username>', methods=["GET","POST"])
def notifs_event(username):
    raw_data = request.get_data()
    try:
        data = request.json
    except Exception as e:
        print(e)
        data = {}
        return Response(status=400)
    
    signed = False
    signature = request.headers.get("x-hub-signature", "=").split("=")[-1]
    hash = hmac.new(str.encode(twitch_thread.Client_ID), msg=raw_data, digestmod=hashlib.sha256).hexdigest()
    if hash == signature:
        signed = True
       
    if request.method == 'GET':
        return request.args.get("hub.challenge") 
    elif signed:
        twitch_thread.incoming_data(data, username)
        return Response(status=200)
    else:
        print("Sign ature could not be verified")
        return Response(status=401)

@app.route('/twitter/webhooks', methods=["GET", "POST"])
def twitter_requests():
    if request.method == 'GET':
        crc=request.args.get('crc_token')
        validation = hmac.new(
            key=bytes(twitter_thread.CONSUMER_SECRET, 'utf-8'),
            msg=bytes(crc, 'utf-8'),
            digestmod=hashlib.sha256
        )
        digested = base64.b64encode(validation.digest())
        response = {
            'response_token': 'sha256=' + format(str(digested)[2:-1])
        }
        return json.dumps(response)
    else:
        #print(request.get_json())
        twitter_thread.tweetAnalyzer(request.get_json())
        return Response(status=200)
    
@app.route('/youtube/user/<username>')
def youtube_webhooks(username):
    if request.method == 'GET':
        return Response(str(request.args.get("hub.challenge")), status=200, mimetype="text/plain")
    else:
        print("Data for" + username + "\n")
        print(request.get_json())
        data = request.json
        yt_thread.incomming_Data(data)
        return Response(status=200)
    
if __name__ == "__main__":
        
    appThread = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, app)
    if Twitch_:
        twitch_thread = ui.launchTwitchThread()
    if Twitter_:
        twitter_thread = ui.launchTwitterThread()
    if HTML_:
        HTML_thread = ui.launchHTMLThread()
    if Spotify_:
        spotify_thread = ui.launchSpotifyThread()
    if Weather_:
        weather_thread = ui.launchWeatherThread()
    if TEMP_ON:
        temp_thread = ui.launchTemperatureThread()
    if Youtube_:
        yt_thread = ui.launchYoutubeThread()
    if GUI_:
        MainWindow.show()
        sys.exit(appThread.exec_())        

    

