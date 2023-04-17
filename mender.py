import numpy as np
import pandas as pd
import pickle
'''
cluster_pipeline = pickle.load(open('finalized_model.sav', 'rb'))
data_test = pd.read_csv('my_DEV')
data_test_uri = pd.read_csv('fin_uris')
data_test_v = data_test.iloc[:, 1:4].values
data_test_uri = data_test_uri.drop('Unnamed: 0', axis = 1)
data_test['cluster'] = cluster_pipeline.predict(data_test_v)
data_test['uris'] = data_test_uri.iloc[:, :].values
data_fin = data_test.iloc[:, 4: 6].values
songs = pd.DataFrame(data_fin, columns = ['cluster', 'uri'])

with open('emotion_dict.pkl', 'rb') as fp:
    final_dict = pickle.load(fp)'''

def cluster(x):
    cluster_pipeline = pickle.load(open('finalized_model_1.pkl', 'rb'))
    data_test = pd.read_csv('my_DEV')
    data_test_uri = pd.read_csv('fin_uris')
    data_test_v = data_test.iloc[:, 1:4].values
    data_test_uri = data_test_uri.drop('Unnamed: 0', axis = 1)
    data_test['cluster'] = cluster_pipeline.predict(data_test_v)
    data_test['uris'] = data_test_uri.iloc[:, :].values
    data_fin = data_test.iloc[:, 4: 6].values
    songs = pd.DataFrame(data_fin, columns = ['cluster', 'uri'])

    with open('emotion_dict.pkl', 'rb') as fp:
        final_dict = pickle.load(fp)
    seed_songs = []
    seed_cluster = final_dict[x]
    for i in seed_cluster: 
        values = songs.uri[songs.cluster == i]
        if len(values) == 0: 
                continue
        elif len(values)>=5:
                seed_songs = np.concatenate((seed_songs, values[0:5]))
        elif len(values)<0 and  len(values)>=5:
                seed_songs = np.concatenate((seed_songs, values))
    return seed_songs[0:5]













