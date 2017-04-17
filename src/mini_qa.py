import os
import wikipedia
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
import train_ans_type
import download_data

# Q. when tom cruise was born?
# Q. Which country has hindi as an official language other than india?
stop_words_list = set(stopwords.words('english'))


def ask():
    question = input("Q. ").strip()
    question = question.lower()
    ans_typ = train_ans_type.ans_type(question)
    print('Answer type : ', ans_typ)
    q_tokens = nltk.word_tokenize(question)
    print(q_tokens)
    question = question.replace("?", "")
    good_q = [i for i in question.lower().split() if i not in stop_words_list]
    print(good_q)
    search_query = " ".join(good_q)
    # print(search_query)
    download_data.fetch(question)


ask()
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
good_q = [i for i in q.lower().split() if i not in stop_words_list]
print(good_q)

ans = wikipedia.search()
print(ans)
'''