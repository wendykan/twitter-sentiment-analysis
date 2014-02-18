twitter-sentiment-analysis
==========================




The scripts parses through twitter outputs (from twitter API, in JSON format) and matches them with sentiment dictionary. Then gives each tweet a sentiment score. 


Here I provide two example files that I saved from twitter: 
>short.txt
>filetosubmit.txt


To execute, try:

bash> python tweet_sentiment.py AFINN-111.txt short.txt


this calculates the sentiment of every tweet in file short.txt



