from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
train = [
    ('which', 'entity'),
    ('when', 'time'),
    ('where', 'location'),
    ('what', 'entity'),
    ('how many', 'count'),
    ("how", 'reason'),
    ('when was', 'time')
]


def ans_type(question):
    cl = NaiveBayesClassifier(train)
    return cl.classify(question)  # "pos"
    # cl.classify("I don't like their pizza.")  # "neg"

