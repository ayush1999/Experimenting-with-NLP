import nltk
import numpy as np

positive_vocab = open('positive.txt','r')
positive_vocab = positive_vocab.read().replace('\n',' ').replace('\t',' ')
positive_vocab = positive_vocab.split(' ')
positive_vocab = [wd.lower() for wd in positive_vocab]
print(positive_vocab)    

negative_vocab = open('negative.txt', 'r')
negative_vocab = negative_vocab.read().replace('\n', ' ').replace('\t', ' ')
negative_vocab = negative_vocab.split(' ')
negative_vocab = [wd.lower() for wd in negative_vocab]

def feature_extraction(words):
    return dict([word, True] for word in words)

positive_features = [(feature_extraction(pos),'pos') for pos in positive_vocab]
negative_features = [(feature_extraction(pos),'neg') for pos in negative_vocab]

train_set = negative_features+ positive_features

classifier = nltk.NaiveBayesClassifier.train(train_set)

sentence = input("Enter your sentence: ")
sentence = sentence.lower()
words = sentence.split(" ")
neg = pos = neu = 0
for word in words:
    classresult = classifier.classify(feature_extraction(word))
    if classresult == 'neg':
        neg += 1
    if classresult == 'pos':
        pos += 1
        
print('Positive sentiment percentage: {} '.format(float(pos)/len(words)))

print('Negative sentiment percentage: {} '.format(float(neg) / len(words)))

print('Neutral sentiment percentage: {} '.format(float(neu) / len(words)))
