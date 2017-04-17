import os
import wikipedia
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
import time
from nltk.stem.snowball import SnowballStemmer
import re
import train_ans_type
import vsm
import download_data
# Q. when thomas cruise was born?
# Q. Which country has hindi as an official language other than india?


class MiniQA:
    stemmer = SnowballStemmer("english")  # Applied Stemming
    stop_words_list = set(stopwords.words('english'))

    def ask(self):
        question = input("Q. ").strip()
        question = question.lower()
        ans_typ = train_ans_type.ans_type(question)
        print('Answer type : ', ans_typ)
        q_tokens = nltk.word_tokenize(question)
        # print(q_tokens)
        question = question.replace("?", "")
        good_q = [i for i in question.lower().split() if i not in self.stop_words_list]
        download_data.fetch(good_q)
        # print(good_q)
        vsm.search(question)


start_time = time.time()
m = MiniQA()
m.ask()
end_time = time.time()
print('')
print('Total ', (end_time-start_time), " seconds.")
'''


# q_tagged = nltk.pos_tag(q_tokens)
# print(q_tagged)
# q_entities = nltk.chunk.ne_chunk(q_tagged)
# print(q_entities)
'''
'''
# mean = TextBlob(q).sentiment
# print(mean)
q = q.replace("?", "")
good_q = [i for i in q.lower().split() if i not in self.stop_words_list]
print(good_q)

ans = wikipedia.search()
print(ans)
'''