import spacy
from spacy.vocab import Vocab
from spacy.language import Language

nlp = spacy.load("en_core_web_lg")

word1="running"
word2="walking"


# w1 = nlp.vocab("word1")
# w2 = nlp.vocab("word2")

# similarity = w1.similarity(w2)
# print("similarity - ", similarity)