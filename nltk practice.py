import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

data = "My name is Ayush . I love football. I played Tennis."                   # data to analyse.

sentence = word_tokenize(data)

for sent in sentence:
    print(nltk.pos_tag(word_tokenize(sent)))