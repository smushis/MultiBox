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
from TwitterGUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal


app = flask.Flask("Webhooks listener")
app.config["DEBUG"] = False

# Logger
# import logging
# logger = logging.getLogger("werkzeug")
# logger.setLevel(logging.ERROR)


@app.route('/twitch/user/<username>', methods=["GET","POST"])
def notifs_event(username):
    if request.method == 'GET':
        chall = request.args.get("hub.challenge")
        return chall 
    else:
        twitch_thread.incoming_data(request.get_json(), username)
    return Response(status=200)

@app.route('/twitter/webhooks', methods=["GET", "POST"])
def webhook_challenge():
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
        
if __name__ == "__main__":
        
    appThread = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, app)
    twitch_thread = ui.launchTwitchThread()
    twitter_thread = ui.launchTwitterThread()
    HTML_thread = ui.launchHTMLThread()
    MainWindow.show()
    sys.exit(appThread.exec_())        

    

