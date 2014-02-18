import sys
import json
import string
import collections

def sentiment_lib(sent_file):
  sent_lines = open(sent_file)
  scores = {} # initialize an empty dictionary
  for line in sent_lines:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  return scores
  
# reads the whole tweet log and parse it, calculates the sentiment of each tweet
def score_each_tweet(tweet_file, sent_lib):
  term_lib = {}
  with open(tweet_file) as tf:
    for line in tf:
      tweet = json.loads(line , 'utf=8')
      if 'text' in tweet.keys():
        word = clean_word(tweet['text'])
        score = sentiment(word, sent_lib)
        if score != 0:
        	new_term_lib = update_sent(score, word, sent_lib)
        	term_lib = merge_term_lib(term_lib, new_term_lib)
#        print term_lib
        sorted_term_lib = collections.OrderedDict(sorted(term_lib.items()))
  for key,value in sorted_term_lib.items():
    print key, value

def merge_term_lib(x, y):
  return dict( [ (n, x.get(n, 0)+y.get(n, 0)) for n in set(x)|set(y) ] )

def clean_word(word):
  word = unicode(word.lower())
  # remove the punctuations in the words
  exclude = set(string.punctuation)
  word = ''.join(ch for ch in word if ch not in exclude)
  return word
        
def update_sent(score, tweet, sent_lib):
  term_lib = {}
  words = tweet.split()
  for word in words:
    if word.startswith('@') != True:
      if sent_lib.has_key(word) != True and word!='':
        term_score = score/10
        term_lib[word] = term_score
  return term_lib  
           
# calculates sentiment of the tweet input param
def sentiment(tweet, sent_lib):
  words = tweet.split()
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
