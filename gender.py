# Guessing the gender based on name.


import nltk
from nltk.corpus import names


names = ([(name,'male') for name in names.words('male.txt')]+
            [(name,'female') for name in names.words('female.txt')])

def gender_features(word):
    return {'last_letter':word[-1]}

feature_sets = [(gender_features(n),g) for (n,g) in names]

classifier = nltk.NaiveBayesClassifier.train(feature_sets)
name = input('Please enter your name')

print(classifier.classify(gender_features(name)))
print(classifier.show_most_informative_features(5))
