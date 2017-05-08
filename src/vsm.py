from __future__ import division
from collections import defaultdict
import math
import sys
import os
import nltk
from nltk.corpus import stopwords

from utilities.dataloader import load_data

'''
Term Frequency = 1 + log(tf(t,d))
Inverse Document Frequency = log (N / tf(t,d) )
'''

__author__ = 'Amit_g'


class VectorSpaceModel:

    def __init__(self):
        self.ans_bank = []
        self.doc_fnames = {}
        self.N = -1  # corpus size
        self.dictionary = set()  # to contain all terms (i.e, words)
        self.postings = defaultdict(dict)  # key: terms, values: posting list ; posting list = doc_id, freq
        self.documentTermFrequency = defaultdict(int)  # key: terms , values: count of docs containing the key
                                                        # 'a term appear in how many docs'
        self.termFrequency = defaultdict(dict)  # key: doc id, values: list ; list = term, freq
        self.cachedStopWords = stopwords.words('english')

    def initialize_terms_and_postings(self):
        self.N = len(self.doc_fnames)
        for id in self.doc_fnames:
            document = load_data(self.doc_fnames[id]).lower()
            terms = nltk.word_tokenize(document)
            terms = [word for word in terms if word not in self.cachedStopWords]
            unique_terms = set(terms)
            self.dictionary = self.dictionary.union(unique_terms)
            for term in unique_terms:
                self.postings[term][id] = terms.count(term)  # the value is the freq of the term in the document
                self.termFrequency[id][term] = 1.0 + math.log(terms.count(term), 2)

    def initialize_document_frequencies(self):
        for term in self.dictionary:
            self.documentTermFrequency[term] = len(self.postings[term])

    def normalize_term_frequencies(self):
        for id in self.termFrequency:
            vec = []
            for val in self.termFrequency[id].values():
                vec.append(val)
            for term in self.termFrequency[id]:
                self.termFrequency[id][term] = self.termFrequency[id][term] / self.norm_l2(vec)

    def inverse_document_frequency(self, term):
        # Return the idf of the term, if term not in dictionary then return 0.
        if term in self.dictionary:
            return math.log(self.N/self.documentTermFrequency[term], 2)
        else:
            return 0.0

    def tf_idf(self, term, id):
        if term in self.dictionary:
            if term in self.termFrequency[id]:
                return self.termFrequency[id][term] * self.inverse_document_frequency(term)
            else:
                return 0
        else:
            return 0

    def norm_l2(self, vec):
        sum = 0.
        for val in vec:
            sum += val ** 2

        return math.sqrt(sum)

    def cosine_similarity(self, query, id):
        dot_prod = 0.
        l_query = 0.
        l_doc = 0.
        cosine = 0.
        vec = []
        for term in query:
            vec.append(query.count(term))
        for term in query:
            tf_idf_q = query.count(term)/self.norm_l2(vec) * self.inverse_document_frequency(term);
            tf_idf_doc = self.tf_idf(term, id)
            prod = tf_idf_q * tf_idf_doc
            dot_prod += prod
            l_query += tf_idf_q ** 2
            l_doc += tf_idf_doc ** 2

        l_query = math.sqrt(l_query)
        l_doc = math.sqrt(l_doc)

        if not (l_query == 0 or l_doc == 0):
            cosine = dot_prod / (l_query * l_doc)

        return cosine

    def do_search(self, question):
        query = nltk.word_tokenize(question.lower())
        if query == []:
            sys.exit()

        scores = sorted([(id, self.cosine_similarity(query, id))
                         for id in self.doc_fnames],
                        key=lambda x: x[1],
                        reverse=True)
        # pick the top 2% results
        bound = int(len(scores) * 0.5)
        if bound > 1:
            top_results = scores[0:bound]
            print("Score:\t filename")
            for (id, score) in top_results:
                print(str(score) + "  : \t" + self.doc_fnames[id].split("/")[-1])
                self.ans_bank.append(self.doc_fnames[id].split("/")[-1])
            # print(self.ans_bank)
        else:
            print('There are no documents to search for !\n')

    def initialize_docs(self, path):
        self.doc_fnames = {}
        i = 0
        # Read all files in a directory
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for f in files:
                    if f.endswith('.txt'):
                        self.doc_fnames[i] = os.path.abspath(os.path.join(root, f))
                        i += 1
        else:
            print(path, ' is invalid !')
            return

    def test_vsm(self):
        print('\nRanked List of Text Documents.')
        path = os.path.dirname(os.path.realpath(__file__))
        path = path.replace("/src", "/corpora/")
        self.initialize_docs(path=path)
        self.initialize_terms_and_postings()
        self.initialize_document_frequencies()
        self.normalize_term_frequencies()


def search(question):
    m = VectorSpaceModel()
    m.test_vsm()
    m.do_search(question)

