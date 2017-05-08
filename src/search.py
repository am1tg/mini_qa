import sys
import time
import os
import nltk
import nltk.data
from nltk.stem.snowball import SnowballStemmer

path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src",  "/corpora/")
stemmer = SnowballStemmer("english", ignore_stopwords=True)


query = ['google', 'founded']
query_stem = []
for k in range(0, len(query)):
    q = stemmer.stem(query[k])
    query_stem.append(q)
print(query_stem)

documents = ['Customer_relationship_management.txt', 'Google+.txt', 'Google_Talk.txt', 'Google_Maps.txt', 'Google_Search.txt']
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

with open(path+documents[0], 'r') as file:
    file_data = file.read()
    sentence = tokenizer.tokenize(file_data)
    print(sentence)
