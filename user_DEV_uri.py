from __future__ import print_function    # (at top of module)
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth


# =============================================================================
# client_id="ef27885a20a94167909332ff507bfde5"
# client_secret="b4382247b3b746858ada7072907788ee"
# redirect_uri="http://localhost:8080"
# =============================================================================
 
def get_user_dev(client_id, client_secret, redirect_uri):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
     client_secret=client_secret,
     redirect_uri=redirect_uri,  scope = 'user-top-read'
    ))
    
    
    ranges = ['short_term']
    uris = []
    
    for sp_range in ranges:
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
