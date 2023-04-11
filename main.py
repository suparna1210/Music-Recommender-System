from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from collections import defaultdict
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
        
features = ['danceability', 'energy', 'valence']
feature = []
final = []
feature = sp.audio_features(uris)
for i in feature:
    final.append(list(map(i.get, features)))

final_df = pd.DataFrame(final)
final_df.to_csv('my_DEV')

sea_dir = {'anger':['Heavy_Metal','Punk_Rock','Hip_Hop','Industrial','Hardcore'],
           'joy':['Pop','Dance','Soul','Reggae','World_Music'],
           'fear':['Horror','Ambient','Experimental','Dark_Ambient','Soundtracks'],
           'love':['Blues','Classical','Jazz','Country','Indie'],
           'sadness':['Post-rock','Folk','Post-punk','Shoegaze','Chamber_music']}

songs = []
for i, key in enumerate(sea_dir):
    for j in sea_dir[key]:
        songs.append(sp.search(j))
    
song_dict=defaultdict(list)
for i in range(len(songs)):
    for j in(songs[i]['tracks']['items']):
        #song_uri.append(item['uri'])
        #song_uri[i].append(j['uri'])
        song_dict[i//5].append(j['uri'])
        
songs_features = defaultdict(list)
fin_features 


for i in range(len(song_dict)):
    songs_features[i].append(sp.audio_features(song_dict[i]))

fin_features = [0, 1 ,2, 3, 4]
for i in range(len(songs_features)):
    for j in songs_features[i][0]:
        print(j.get(features))
        

# =============================================================================
# for k,v in range(len(songs_features)):
#     print(songs_features.fromkeys(k))
# =============================================================================
# =============================================================================
# for i in range(len(songs_features)):
#     for j in (songs_features[i][0]):
#         
# =============================================================================
        


        
    
    