import wikipedia
import nltk
from difflib import SequenceMatcher
import urllib.parse

from nltk.corpus import stopwords


q = wikipedia.search('obama iowa 2012')
for item in q:
    page = wikipedia.page(item)
    print('starting...')
    page_title = page.title
    print(page_title)
    content = page.summary
    content = content.lower()
    print('Converting to sentences...')
    sentences = nltk.sent_tokenize(content)
    for sentence in sentences:
        print(sentence)
        print()
    break


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]
