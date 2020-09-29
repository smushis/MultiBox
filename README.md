# MultiBox
### Simple GUI interfacing Twitch and Twitter notifications, Spotify tracking, Weather data and Home temperature, designed for RaspberryPI 

#### Hardware needed:
  - Computer or Raspberry PI
  - A DHT11 Temperature Sensor (if you want to get the temperature with the RaspberryPI)
  
#### Software modules implemented:
  - **Twitch** live Notifications
  - **Twitter** Mentions(with media), Like or RT Notifications
  - **Spotify** Current track playing (You need premium Spotify for playing playlist)
  - **OpenWeatherMap** Weather for current hour and tomorrow
  - House temperature thanks to DHT11 sensor 
  - **New YOUTUBE** webhooks notifications (console only currently)

I recommand you to use the latest version of [Raspberry PI OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) if you are going to do a new project on your PI.
The software is using ~150MB of RAM and less than 20% of the CPU (less than 5% in idle) on my Raspberry PI 3 B+.
  
### Goals of the project
This project was made by me, for me. I didn't attend to publish it for other people to use it.
But this program can help you with your own project, so feel free to look at the code.
If you have any questions or ideas for the GUI, don't hesitate to do an issue!

### Future updates that might come (in order of  priority)
  - Find a way to wrap the text from Twitch and Twitter more correctly -> A bit better, but not satisfied yet
  - Better GUI interface -> Currently working on it on newGUI branch(90%) 
  - ~~7 days weather~~ -> Working on new GUI  
  - ~~Twitch Secret message~~
  - Better Handling of Exception and Json reading
  - Twitter Video 
  - ~~Delete @username before tweet printing~~
  - ~~Buttons to skip music, play/pause/resume, launch a playlist, progress bar of the song~~
  - ~~Change Avatar border~~ -> Need simple avatar border for notifications
  - Fix connection with Bluetooth speaker with Raspi 3 (or use cable)
  - Maybe switch from Raspotify to classic Spotify player on Raspi
  - ~~New Modules~~ -> Youtube API webhooks, Rocket League Stats tracking and Analog clock
  - ~~Spotify tracker ? (like Lastfm)~~ -> Data Display on new GUI, maybe I will track songs myself
  - Thinking of responsive design (involved HTML so meh)
  
### Recommanded Spotify playlist
I want to share my personnal playlist to all of you, so go [here](https://open.spotify.com/playlist/2EDQvU4v6zHH39G1pKAJrr?si=BH-ZqEx-SRayr16gIOj58w) right now!

### Social Medias
  - Twitter : [@Smushis](https://twitter.com/Smushis)

### References:
  - [Twitch API reference](https://dev.twitch.tv/docs/api/reference/)
  - [TwitterAPI, wrapper for Python](https://github.com/geduldig/TwitterAPI)
  - [Twitter API reference for webhooks](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/subscribe-account-activity/overview)
  - [Spotipy, Spotify wrapper for Python](https://spotipy.readthedocs.io/en/2.16.0/)
  - [Open Weather Map API](https://openweathermap.org/api)
  - [Github DHT11 Sensor Adafruit](https://github.com/adafruit/Adafruit_CircuitPython_DHT)
  - [Youtube webhooks](https://developers.google.com/youtube/v3/guides/push_notifications)
  
# Exemples of GUI notifications:
### Twitch Live Notification
![alt text](https://i.imgur.com/r5V5wby.png)

### Twitter RT
![alt text](https://i.imgur.com/xzcZgxQ.png)

### Twitter Like
![alt text](https://i.imgur.com/QgSqztf.png)

### Twitter Mentions
![alt text](https://i.imgur.com/B2zn40F.png)

### Twitter Mentions with Media
![alt text](https://i.imgur.com/Gojcjfz.png)

Yes, this is an avatar border from Rocket League
