from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from collections import defaultdict
import ast
import numpy as np
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ef27885a20a94167909332ff507bfde5",
 client_secret="b4382247b3b746858ada7072907788ee",
 redirect_uri="http://localhost:8080",  scope = 'user-top-read'
))


ranges = ['short_term']
uris = []

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        uris.append(item['uri'])
    '''finds uris of user top 50 songs'''


give = pd.DataFrame(uris)
give.to_csv('fin_uris')         #top 50 uri data

        
features = ['danceability', 'energy', 'valence']
feature = []
final = []
feature = sp.audio_features(uris)


for i in feature:
    final.append(list(map(i.get, features)))
final_df = pd.DataFrame(final)
final_df.to_csv('my_DEV')               #DEV values of user top 50 songs



#top 5 genres of our emotion label
sea_dir = {'anger':['HeavyMetal','Punk Rock','Hip Hop','Industrial','Hardcore'],
           'joy':['Pop','Dance','Soul','Reggae','World_Music'],
           'fear':['Horror','Ambient','Experimental','Dark Ambient','Soundtracks'],
           'love':['Blues','Classical','Jazz','Country','Indie'],
           'sadness':['Post-rock','Folk','Post-punk','Shoegaze','Chamber music']}


songs = []
for i, key in enumerate(sea_dir):
    for j in sea_dir[key]:
        songs.append(sp.search(j))
        

song_dict=defaultdict(list)
for i in range(len(songs)):
    for j in(songs[i]['tracks']['items']):
        song_dict[i//5].append(j['uri'])
        
songs_features = []
giver = defaultdict(list)
for i in range(len(song_dict)):
    temp = sp.audio_features(song_dict[i])
    if None in temp:
        id_d = (temp.index(None))
        temp[id_d] = temp[id_d-1]
    songs_features.append(temp)
for i in range(len(songs_features)):
        for j in songs_features[i]: 
            giver[i].append(list(map(j.get, features)))
cvt_DEV = pd.DataFrame(giver)
cvt_DEV.columns = sea_dir.keys()

cvt_DEV.to_csv('top_50',index=False)
# final data for top genre-emotion tracks

