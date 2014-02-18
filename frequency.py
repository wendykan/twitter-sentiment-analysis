import sys
import json
import string
import collections

def freq_each_tweet(tweet_file):
  freq = collections.defaultdict(int)
  with open(tweet_file) as tf:
    for line in tf:
      tweet = json.loads(line , 'utf=8')
      if 'text' in tweet.keys():
        words = unicode(tweet['text']).split()
        for word in words:
          word = clean_word(word)
          freq[word] += 1
#          print word, freq[word]
  all_term_sum = sum(freq.itervalues())
  sorted_freq = collections.OrderedDict(sorted(freq.items()))
  for key,value in sorted_freq.items():
    print key, value/all_term_sum


def clean_word(word):
  word = word.lower()
  # remove the punctuations in the words
  exclude = set(string.punctuation)
  word = ''.join(ch for ch in word if ch not in exclude)
  return word
        

def main():
    tweet_file = sys.argv[1]
    freq_each_tweet(tweet_file)

if __name__ == '__main__':
    main()
