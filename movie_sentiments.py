import nltk
from twython import Twython
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiments(sentence):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    for k in ss:
        print('{0} : {1} '.format(k, ss[k]))


TWITTER_APP_KEY = ' iUSzoDXavCwTlBqOJthuONdvb'  # supply the appropriate value
TWITTER_APP_KEY_SECRET = 'dnM6d1N04b2a6LsUS8f1y5fc9Xy5S28CnamfKkM0flgM6c6lAG'
TWITTER_ACCESS_TOKEN = '839858792619732992-61OMp6niBUgV00pkifeEepIeldgE7av'
TWITTER_ACCESS_TOKEN_SECRET = 'FYNZV32nBcO7SmB5PaFlBawc4zdKIvx2Bnllyxy6D1nP5'

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#padmavati',  # **supply whatever query you want here**
                  count=100)

tweets = search['statuses']

for tweet in tweets:
    print('{0} and {1}'.format(tweet['id_str'], tweet['text']))