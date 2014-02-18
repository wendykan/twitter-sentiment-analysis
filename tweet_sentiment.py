import sys
import json
# loads the sentiment library
def sentiment_lib(sent_file):
  sent_lines = open(sent_file)
  scores = {} # initialize an empty dictionary
  for line in sent_lines:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  return scores
  
# reads the whole tweet log and parse it, calculates the sentiment of each tweet
def score_each_tweet(tweet_file, sent_lib):
  with open(tweet_file) as tf:
    for line in tf:
      tweet = json.loads(line , 'utf=8')
      if 'text' in tweet.keys():
        score = sentiment(tweet['text'], sent_lib)
        print '<sentiment:',score,'>', tweet['text'] 
           
# calculates sentiment of the tweet input param
def sentiment(tweet, sent_lib):
  words = unicode(tweet).split()
  score = 0.0
  for word in words:
    word_score = sent_lib.get(word, 0.0)
    score += word_score
  return score

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    sent_lib = sentiment_lib(sent_file)
    score_each_tweet(tweet_file, sent_lib)

if __name__ == '__main__':
    main()
