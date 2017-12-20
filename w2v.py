import gensim
from nltk.corpus import brown

# Training
sentences = brown.sents()
model = gensim.models.Word2Vec(sentences, min_count=1)
model.save('brown_model')

print('W2V using brown corpus trained successfully')

# Test

model = gensim.models.Word2Vec.load('brown_model')
# Print words similar to 'mother'
print(model.most_similar('mother'))

# Print vector representation of word 'human'
print(model['human'])