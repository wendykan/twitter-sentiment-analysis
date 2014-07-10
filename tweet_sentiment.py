import sys
import json
from sentiment import sentiment, sentiment_lib
  
# reads the whole tweet log and parse it, calculates the sentiment of each tweet
def score_each_tweet(tweet_file, sent_lib):
  with open(tweet_file) as tf:
    for line in tf:
      tweet = json.loads(line , 'utf=8')
      if 'text' in tweet.keys():
        score = sentiment(tweet['text'], sent_lib)
        print score
           
def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    sent_lib = sentiment_lib(sent_file)
    score_each_tweet(tweet_file, sent_lib)

if __name__ == '__main__':
    main()
