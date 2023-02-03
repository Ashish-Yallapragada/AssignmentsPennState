import tweepy
import re
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def wordcloud():
    API_KEY = input('Enter API Key: ')
    API_SECRET = input('Enter API Secret: ')
    textInput = input('Enter the text: ')
    ACCESS_KEY = '1332696035701899264-C6m5SNdUVTSVotOXGOEp7gtUgUmDJQ'
    ACCESS_SECRET = 'lmzwyJazAXAf3O2r3emVLEepORgxJzdQP0dUXSY3rFky4'
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAML4lAEAAAAAaTA%2F%2FMAQiZa3mrZr0UjGCjft344%3D1zwadbmYJrqPqC2UDLfIVhcKyGw8d6qmYmVNrBBuqmv7hm3PZf'

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)    
    client = tweepy.Client(BEARER_TOKEN)
    query = '#{}'.format(textInput)

    tweets = client.search_recent_tweets(query = query, max_results = 100)

    tweet_text_list = []
    for j in range(100):
        for i in tweets.data:
            tweet_text_list.append(i.text)
        if(tweets.meta.get('next_token') is None):
            break           
        tweets = client.search_recent_tweets(query = query, max_results = 100, next_token = tweets.meta['next_token'])            
    df_tweet = pd.DataFrame(tweet_text_list)
    
    file = open("C:/Users/ashis/OneDrive/Desktop/Assignments/NLPAssignment1/stopwords.txt",'r')
    stopwordsFile = file.readlines()
    stopWords = []
    for line in stopwordsFile:
        stopWords.append(line[:-1])    
    stopwords = set(STOPWORDS)
    stopwords.update(stopWords)

    bigstring = df_tweet.apply(lambda x: ' '.join(x)).str.cat(sep=' ')
    bigstring = re.sub('[^A-Za-z0-9]+',' ',bigstring)
    
    wordcloud = WordCloud(stopwords=stopwords,background_color='white',width=1500, height=1500,min_word_length=4,collocations=True,collocation_threshold=10).generate(bigstring)
    print('Result is displayed in wordcloud_output file')
    wordcloud.to_file('wordcloud_output.png')

if __name__ == "__main__":
    wordcloud()

