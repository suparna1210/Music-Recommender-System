from __future__ import print_function    # (at top of module)
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from collections import defaultdict
import numpy as np
import ast 
from more_itertools import unique_everseen
import pickle
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ef27885a20a94167909332ff507bfde5",
 client_secret="b4382247b3b746858ada7072907788ee",
 redirect_uri="http://localhost:8080",  scope = 'user-top-read'
))



#top 5 genres of our emotion label
sea_dir = {'anger':['HeavyMetal','Punk Rock','Hip Hop','Industrial','Hardcore'],
           'joy':['Pop','Dance','Soul','Reggae','World_Music'],
           'fear':['Horror','Ambient','Experimental','Dark Ambient','Soundtracks'],
           'love':['Blues','Classical','Jazz','Country','Indie'],
           'sadness':['Post-rock','Folk','Post-punk','Shoegaze','Chamber music']}

features = ['danceability', 'energy', 'valence']
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


df_a = []
clust = []
bro = []
emo_dict = {}
emo_direct =['anger', 'joy', 'fear', 'love', 'sadness']
model = pickle.load(open('./finalized_model_1.pkl', 'rb'))
top50 = pd.read_csv('./top_50')
    
for i in top50.columns: 
    for j in range(len(top50[i])):
        top50[i][j] = np.asarray(ast.literal_eval(top50[i][j]))
    
for i in range(0, 5):
    df_a.append(top50.iloc[:, i].values)

for i in range(0, 5): 
    df_a[i] = np.stack(df_a[i])

for i in range(len(df_a)):
    clust.append(list(model.predict(df_a[i])))
    
for i in range(len(clust)):
    temp = sorted(clust[i],key=clust[i].count,reverse=True)
    bro.append(list(unique_everseen(temp)))

for i in range(len(bro)):
    emo_dict[i] = bro[i]

emotion_dict = dict(zip(emo_direct, list(emo_dict.values())))

with open('emotion_dict.pkl', 'wb') as fp:
    pickle.dump(emotion_dict, fp)
