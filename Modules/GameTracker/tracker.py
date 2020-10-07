# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:47:04 2020

@author: Barmando
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import requests
from time import sleep
import json

class GameTracker(QtCore.QThread): 
    game_signal = pyqtSignal(dict)
    user_id = "76561198055870358"
    
    endpoint = "https://rocketleague.tracker.network/rocket-league/profile/steam/76561198055870358/overview"
    
    def __init__(self, threadID, name):
        QtCore.QThread.__init__(self, parent=None)   
        self.threadID = threadID
        self.name = name
        
    def run(self):
        print("Starting " + self.name + "\n\r")
        while True:
            self.sendRanks_RL()
            sleep(600)

    def getRanks_RL(self):
        try:
            r = requests.get(self.endpoint)
            lines = r.text
        except:
            print('Error')
            
        rank_info_script_index = lines.find('<script>window')
        end_rank_info_script_index = lines.find('</script>', rank_info_script_index) 
        
        site_script_json = json.loads(lines[rank_info_script_index+33:end_rank_info_script_index-122])
        stat_json = site_script_json.get('stats-v2').get('standardProfiles').get(f'rocket-league|steam|{self.user_id}')
        segments = stat_json.get('segments', "")        
        playlists_json = {
            "Ranked Duel 1v1": segments[2],
            "Ranked Doubles 2v2": segments[3],
            "Ranked Standard 3v3": segments[5],
            "Hoops": segments[6],
            "Rumble": segments[7],
            "Dropshot": segments[8],
            "Snowday": segments[9]
        }
    
        all_playlist_rank_json = {
            "Ranked Duel 1v1": {},
            "Ranked Doubles 2v2": {},
            "Ranked Standard 3v3": {},
            "Hoops": {},
            "Rumble": {},
            "Dropshot": {},
            "Snowday": {}
        }
        for playlist in all_playlist_rank_json.keys():
            playlist_stats_json = playlists_json.get(playlist).get('stats')
            all_playlist_rank_json[playlist]['mmr'] = playlist_stats_json.get('rating').get('displayValue').replace(',', '')
            all_playlist_rank_json[playlist]['rank'] = playlist_stats_json.get('tier').get('metadata').get('name')
            all_playlist_rank_json[playlist]['division'] = playlist_stats_json.get('division').get('metadata').get('name')
    
        return all_playlist_rank_json

    def sendRanks_RL(self):
        ranks = self.getRanks_RL()
        dico = {}
        dico["3v3"] = ranks.get("Ranked Standard 3v3", {})
        dico["2v2"] = ranks.get("Ranked Doubles 2v2", {})
        # print(dico)
        self.game_signal.emit(dico)
        