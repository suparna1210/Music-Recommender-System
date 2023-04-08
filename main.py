from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
from spotipy.oauth2 import SpotifyOAuth
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

sea_dir = {}
result = sp.search(search_str)
print(result)
