import tweepy 

# We import our access keys:
from credentials import *  # This will allow us to use the keys as variables

# Function to extract tweets 
def get_tweets(username): 
		
	# Authorization to consumer key and consumer secret 
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

	# Access to user's access key and access secret 
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

	# Calling api 
	api = tweepy.API(auth) 

	# 200 tweets to be extracted 
	number_of_tweets=20
	tweets = api.user_timeline(screen_name=username, count = number_of_tweets, tweet_mode='extended') 

	# Empty Array 
	tmp=[] 

	# create array of tweet information: username, 
	# tweet id, date/time, text 
	tweets_for_csv = [tweet for tweet in tweets] # CSV file created 
	for j in tweets_for_csv: 

		# Appending tweets to the empty array tmp 
		tmp.append(j) 

	# Printing the tweets 
	print(tmp[0])
	print(len(tmp))

# Driver code 
if __name__ == '__main__': 

	# Here goes the twitter handle for the user 
	# whose tweets are to be extracted. 
	get_tweets("BarackObama") 
