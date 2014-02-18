twitter-sentiment-analysis
==========================




The scripts parses through twitter outputs (from twitter API, in JSON format) and matches them with sentiment dictionary. Then gives each tweet a sentiment score. 


Here I provide two example files that I saved from twitter: 
- short.txt - this is a shorter version, analyze this file to run faster
- filetosubmit.txt - longer version


To execute, try:

$ python tweet_sentiment.py AFINN-111.txt short.txt

this calculates the sentiment of every tweet in file short.txt


$ python top_ten.py short.txt

gives you the top ten hashtag of the file
