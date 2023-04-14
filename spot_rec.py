from __future__ import print_function    # (at top of module)
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from mender import cluster
import pandas as pd
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ef27885a20a94167909332ff507bfde5",
 client_secret="b4382247b3b746858ada7072907788ee",
 redirect_uri="http://localhost:8080",  scope = 'user-top-read'
))
final_songs = (cluster('anger'))
give = []
for i in range(len(final_songs)):
    give.append(str(final_songs[i]))
related = sp.recommendations( seed_tracks = give, limit = 11)


names = []
urls = []
artists = []
art = []

for i in range(len(related['tracks'])):
    names.append(related['tracks'][i]['name'])    
    res = related['tracks'][i]['artists']['items']
    urls.append(related['tracks'][i]['href'])    