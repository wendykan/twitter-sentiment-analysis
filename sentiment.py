
# calculates sentiment of the input text
def sentiment(text, sent_lib):
  words = unicode(text).split()
  score = 0.0
  for word in words:
    word_score = sent_lib.get(word, 0.0)
    score += word_score
  return score


# loads the sentiment library
def sentiment_lib(sent_file):
  sent_lines = open(sent_file)
  scores = {} # initialize an empty dictionary
  for line in sent_lines:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  return scores