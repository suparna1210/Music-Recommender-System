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

seeder = []
with open('seeder.txt', 'r') as f:
    for line in f: 
        seeder.append(line.strip())
        

related = sp.recommendations( seed_tracks = seeder, limit = 11)
