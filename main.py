# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ec833197e9ce4b79b11d2a86430849f5",
 client_secret="8688491a93a34f9f8459811d7a1bf472",
 redirect_uri="http://localhost:8080",  scope = 'user-top-read'
))
ranges = ['short_term']
uris = []
for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        uris.append(item['uri'])
        
features = ['danceability', 'energy', 'valence']
feature = []
final = []
feature = sp.audio_features(uris)
for i in feature:
    final.append(list(map(i.get, features)))

sea_dir = {'anger':['Heavy Metal','Punk Rock','Hip Hop','Industrial','Hardcore'],
           'joy':['Pop','Dance','Soul','Reggae','World Music'],
           'fear':['Horror','Ambient','Experimental','Dark Ambient','Soundtracks'],
           'love':['Blues','Classical','Jazz','Country','Indie'],
           'sadness':['Post-rock','Folk','Post-punk','Shoegaze','Chamber music']
           }
result = sp.search(search_str)
print(result)
