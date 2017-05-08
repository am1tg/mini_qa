import nltk
from bs4 import BeautifulSoup
import nltk
import nltk.data
import collections
import json
from bs4 import BeautifulSoup
from google import search

# Who is world's richest person?

question = input("Q. ").strip()
question = question.lower()
question_tok = nltk.word_tokenize(question)
print(question_tok)
'''
path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src",  "/corpora/")
for filename in os.listdir(path):
    file = open(path+filename, 'r').read()
    # print(file)

places = GeoText(file)
print('Cities are: ', set(places.cities), '\n')
print('Country are: ', set(places.countries))
'''
questionwords = ["who", "what", "where", "when", "why", "how", "whose", "which", "whom"]

print(search(question))