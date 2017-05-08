import os
import nltk.data
from corenlp import *
import collections
import difflib

commonwords = ["the", "a", "an", "is", "are", "were", "."]
target = ['important', 'aspect', 'CRM', 'approach']

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src",  "/corpora/")

article = open(path+'Customer_relationship_management.txt', 'r')
file_data = article.read()
sentence = tokenizer.tokenize(file_data)
# print(sentence)

searchstring = ' '.join(target)

for i in range(0, len(sentence)):
    # print(sentence[i])
    seq = difflib.SequenceMatcher(None, searchstring, sentence[i])
    d = seq.ratio() * 100
    print(d, '--->', sentence[i])
