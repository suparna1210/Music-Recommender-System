from tensorflow import keras
import tensorflow as tf
from nltk.corpus import stopwords
import re
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer,PorterStemmer
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4') 
num_words = 10000 
tokenizer=Tokenizer(num_words,lower=True)
stop=set(stopwords.words('english'))
model = keras.models.load_model('model (4).h5')


X = str("I have been thinking about going to a beach. I enjoy listening to music and singing .Chilling with friends, playing pubg. Getting an internship in summer, applying for companies.Yes I have been getting decent sleep.")
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer() 
def preprocess(sentence):
    sentence=str(sentence)
    sentence = sentence.lower()
    sentence=sentence.replace('{html}',"") 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', sentence)
    rem_url=re.sub(r'http\S+', '',cleantext)
    rem_num = re.sub('[0-9]+', '', rem_url)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(rem_num)  
    filtered_words = [w for w in tokens if len(w) > 2 if not w in stopwords.words('english')]
    stem_words=[stemmer.stem(w) for w in filtered_words]
    lemma_words=[lemmatizer.lemmatize(w) for w in stem_words]
    return " ".join(lemma_words)

def result(X):
  in_pre = preprocess(X)
  direct = ['anger', 'joy', 'fear', 'love', 'sadness']
  in_tok = tokenizer.texts_to_sequences(in_pre)
  in_pad = pad_sequences(in_tok, maxlen = 300, padding = 'post')
  return direct[max(np.argmax(model.predict(in_pad, verbose = 0), axis=1))]

sentiment = result(X)
