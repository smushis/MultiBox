# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:36:43 2020

@author: Barmando
"""
import flask
from flask import request
from flask import Response
from twitch import Twitch
from html_serv import htmlServ

app = flask.Flask("Twitch listener")
app.config["DEBUG"] = False

@app.route('/twitch/user/<username>', methods=["GET","POST"])
def notifs_event(username):
    if request.method == 'GET':
        chall = request.args.get("hub.challenge")
        return chall 
    else:
        twitch_thread.incoming_data(request.get_json(), username)
    return Response(status=200)

      
twitch_thread = Twitch(1,"Twitch Thread")
html_thread = htmlServ(2, "HTML Thread", app)
html_thread.start()
twitch_thread.start()

