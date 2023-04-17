from __future__ import print_function    # (at top of module)
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from mender import cluster
import pandas as pd

'''
client_id="ef27885a20a94167909332ff507bfde5"
client_secret="b4382247b3b746858ada7072907788ee"
redirect_uri="http://localhost:8080"
sentiment = 'anger'
'''

def get_output(client_id, client_secret, redirect_uri, sentiment):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
     client_secret=client_secret,
     redirect_uri=redirect_uri,  scope = 'user-top-read'
    ))
    
    give = []
    names = []
    artists = []
    art = []
    urls =[]
    
    final_songs = (cluster(sentiment))
    
    for i in range(len(final_songs)):
        give.append(str(final_songs[i]))
    related = sp.recommendations( seed_tracks = give, limit = 11)

    
    for i in range(len(related['tracks'])):
        names.append((related['tracks'][i]['name']))
        urls.append((related['tracks'][i]['href']))
        artists.append((related['tracks'][i]['artists'][0]['name']))
        
    for i in range(len(artists)):
        results = sp.search(q='artist:' + artists[i], type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            art.append((artist['images'][0]['url']))
            
    output_DB = pd.DataFrame()
    output_DB['name'] = names
    output_DB['artists'] = artists
    output_DB['url'] = urls
    output_DB['art_url'] = art
    return output_DB

fin = get_output(client_id, client_secret, redirect_uri, sentiment)
#output_DB.to_csv('output_data', index = False)
