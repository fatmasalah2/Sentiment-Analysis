# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ip7UnBXzP_St8iUzfsixS1jXoqsdirCq
"""

# Nouran Ahmed 20200609
# Mariam Tarek 20200523
# Nada Ashraf  20200587
# Fatma Salah  20200376
# Farah Tawfiq 20200378


# UPDATE COMMIT

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import statistics
from collections import Counter
from matplotlib.backends.backend_pdf import PdfPages
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
import spacy
import string
import re
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neural_network import MLPClassifier
from keras.optimizers import Adam
import joblib
import pickle
from nltk.tokenize import word_tokenize
from google.colab import drive


import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


import warnings
warnings.filterwarnings("ignore")

count_vectorizer = joblib.load('count_vectorizer.pkl')

linear_svc_model = joblib.load('linear_svc_model.pkl')

test_data = ["i am traveling, and i am so happy","happy birhtday!", "I am extremely happy", "I am really sad now","I really enjoyed the movie", "The food was terrible", "The weather is perfect today", "This place was amazing", "I wouldn't recommend this", "I regret buying this product", "The internet speed is slow", "The hotel room was spacious and clean", "The beach was crowded", "The car broke down on the highway", "I haven't answered well, it was really difficult.", "The scenery here is beautiful", "The service at this restaurant was excellent", "The hike was refreshing"]
print(test_data)

def removePunctuation(sentence):
    sentenceWithoutPunc = ""
    sentenceWithoutPunc = "".join(i for i in sentence if i not in string.punctuation)
    return sentenceWithoutPunc

# removePunctuation from new test data
test_data = [removePunctuation(sentence) for sentence in test_data]
print(test_data)

# lowercase words
test_data = [s.lower() for s in test_data]
print(test_data)

# Tokenization
def Tokenization(sentence):
    tokens = re.split(r'\W+', sentence)
    return tokens
test_data = [Tokenization(sentence) for sentence in test_data]
print(test_data)

# Remove stop words

# spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
default_stop_words = set(nlp.Defaults.stop_words)
negationWords = set(["hadn't", "wouldn't", "doesn't", "mightn't", "won't", "shouldn't", 'haven', 'aren' , 'doesn', 'couldn', 'didn', "didnt",'isn', 'wouldn', 'mustn', "isn't", "shan't", "didn't", 'shan', 'hadn', 'wasn', 'weren', "hasn't", 'mightn', "couldn't", "needn't", "haven't", "weren't", "aren't", 'needn', 'not', 'shouldn', 'hasn', "mustn't", "wasn't", "don't", 'don'])

custom_stop_words = default_stop_words - negationWords
nlp.Defaults.stop_words = custom_stop_words
#X_filter = pd.DataFrame(data)
def stopWordsRemoval(sentenceTokenized):

    allInfo = nlp(' '.join(sentenceTokenized))
    filtered_tokens = [token.text for token in allInfo if token.text.lower() not in custom_stop_words]

    return filtered_tokens

# stopword removal
test_data = [stopWordsRemoval(sentence) for sentence in test_data]
print(test_data)

# lemmatize
def lemmatize(tokens):
    doc = nlp(' '.join(tokens))
    lemmatized_tokens = [token.lemma_ for token in doc]
    return lemmatized_tokens
test_data = [lemmatize(sentence) for sentence in test_data]

print(test_data)

print(test_data)

test_data = [' '.join(sentence) for sentence in test_data]

# Fit and transform the data
Xx = count_vectorizer.transform(test_data)



# Convert the result to a DataFrame (optional)
test_data_df = pd.DataFrame(Xx.toarray(), columns=count_vectorizer.get_feature_names_out())

# Displaying the embeddings
print(test_data_df)

y_predict = linear_svc_model.predict(test_data_df)
print(y_predict)

