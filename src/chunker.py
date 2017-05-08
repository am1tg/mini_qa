
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags


q = input("Q. ")
# q = q.lower()
q_tok = word_tokenize(q)
q_tagged = pos_tag(q_tok)
q_chunks = ne_chunk(q_tagged)
print(q_chunks)
ne_tree = ne_chunk(pos_tag(word_tokenize(q)))

iob_tagged = tree2conlltags(ne_tree)
print(iob_tagged)