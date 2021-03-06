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
import xmltodict

from flask import request
from flask import Response
from Modules.GUI.GUI2 import Ui_MainWindow
from PyQt5 import  QtWidgets

from constants import Twitter_, Spotify_, Twitch_, HTML_, Weather_, TEMP_ON, GUI_, Youtube_, Game_, Raspi_

app = flask.Flask("Webhooks listener")
app.config["DEBUG"] = False


# Logger
# import logging
# logger = logging.getLogger("werkzeug")
# logger.setLevel(logging.ERROR)

quotes = ["But the Earth refused to die",
          "Come meet me by the river \n See how time it flows",
          "A blood black nothingness began to spin ",
          "A system of cells interlinked within cells interlinked within cells interlinked within one stem",
          "And dreadfully distinct against the dark, a tall white fountain played",
          ]

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
    
@app.route('/youtube/user/<username>', methods=["GET", "POST"])
def youtube_webhooks(username):
    if request.method == 'GET':
        return Response(str(request.args.get("hub.challenge")), status=200, mimetype="text/plain")
    else:
        try:
            print("Data for" + username + "\n")
            data = xmltodict.parse(request.data)
            # print(data)
            yt_thread.incomming_Data(data)
            return Response(status=200)
        except:
            print("Error during xml data shit")
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
    if Game_:
        game_thread = ui.launchGameTrackerThread()
    if Raspi_:
        raspi_thread = ui.launchRaspiThread()
    if GUI_:
        MainWindow.show()
        sys.exit(appThread.exec_())        

    

