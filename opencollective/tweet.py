# To consume Twitter's API
import tweepy
import csv
import pandas as pd

# We import our access keys:
from credentials import *  # This will allow us to use the keys as variables
	
# Authorization to consumer key and consumer secret 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# Access to user's access key and access secret 
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Calling API 
api = tweepy.API(auth) 

# Initializations
number_of_tweets=20
all_profiles = []

#To write into the output file
csvFile_team = open('twitter_data.csv', 'w')
writer_team = csv.writer(csvFile_team)
writer_team.writerow(['UserName', 'Bio', 'No of Followers', 'No of Tweets', 'Profile URL'])

#To Read from our CSV File
with open('Output_Social.csv') as csv_file:
		csv_reader= csv.reader(csv_file, delimiter=',')
   		line_count = 0
    		for row in csv_reader:
		        if line_count == 0:
		            line_count += 1
		        else:
		            all_profiles.append(row[7])
		            line_count += 1

for profile in all_profiles:
	try:
		if (api.get_user(profile)):
			user = api.get_user(profile)
			user_name = user.screen_name
			user_desc = user.description.encode('utf-8')
			user_followers = user.followers_count
			user_tweets = user.statuses_count
			user_url = user.url

			writer_team.writerow([user_name, user_desc, user_followers, user_tweets, user_url])

			#Module to get the tweets
			"""tweets = api.user_timeline(screen_name = profile, count = number_of_tweets, tweet_mode = 'extended')

			if (tweets):
				print("Number of tweets extracted: {}.\n".format(len(tweets)))
				# We print the most recent 5 tweets:
				print("5 recent tweets:\n")
				for tweet in tweets[:5]:
				    print(tweet.full_text)
				
				# We create a pandas dataframe as follows:
				data = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['Tweets'])

				# We display the first 10 elements of the dataframe:

				print(tweets[0].created_at)
				print(tweets[0].favorite_count)
				print(tweets[0].retweet_count)"""
		else:
			break
	except:
		pass