import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
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
  state_sent=dict()
  with open(tweet_file) as tf:
    for line in tf:
      tweet = json.loads(line , 'utf=8')
      if 'text' in tweet.keys():
        score = sentiment(tweet['text'], sent_lib)
        location = tweet['user']['location'].replace(' ','')
        state = convert_location_to_state_abbr(location)
        # now all state names are converted to abbr
        if state in state_sent:
          state_sent[state].append(score)
        else:
          state_sent[state] = [score]
  get_happiest_state(state_sent)            

def convert_location_to_state_abbr(location):
  if ',' in location: # the two letters after comma is the state abbr.
    locterm = location.split(',')
    state = locterm[-1]
  else:
    state = location    
  # if state name is not abbreviated, find it in the state names map
  for abbr in states:
    if state[:4].lower() == states[abbr][:4].lower():
      return abbr
    if state == abbr:
      return abbr



def get_happiest_state(state_sent):
  max = -1
  happystate = 'xx'
  for state, scores in state_sent.items():
    sum = 0.0
    for score in scores:
      sum += score
    avg = sum / len(scores)
    if avg > max:
      happystate = state
      max = avg
  print happystate
           
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
