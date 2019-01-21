#######################################################
#UTF-8 Encoded
#Created Date - Jan 20th, 2019
#Author - Raghav Ramky
#Stage_5: Extracting data from Github and Twitter using 
#		  the output from Stage_3
#######################################################

#Importing Developer Access_Keys to use Twitter API:
from credentials import *

import pandas as pd
import datetime
import tweepy
import time
import csv

start = time.time()

#Twitter_Module#################################################################
# Stage_5_Twitter global Variables
all_profiles = []
all_names = []
git_url = []

# Authorization to consumer key and consumer secret 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# Access to user's access key and access secret 
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Calling API 
api = tweepy.API(auth)

#To Read from our CSV File
with open('Stage_3.csv') as csv_file:
		csv_reader= csv.reader(csv_file, delimiter=',')
   		line_count = 0
    		for row in csv_reader:
		        if line_count == 0:
		            line_count += 1
		        else:
		        	all_names.append(row[0])
		            all_profiles.append(row[6])
		            git_url.append(row[7])
		            all
		            line_count += 1

#To write into the output file
s5_tweet = open('Stage_5_Twitter_Data.csv', 'w')
writer_tweet = csv.writer(s5_tweet)
writer_tweet.writerow(['Project_Name', 'UserName', 'Member Since', 'Bio', 'No of Followers', 'No of Tweets', 'Profile URL'])

for tweet_inst, profile in enumerate(all_profiles):
	try:
		if (api.get_user(profile)):
			user = api.get_user(profile)
			user_name = user.screen_name
			user_cr_dt = user.created_at
			user_desc = user.description.encode('utf-8')
			user_followers = user.followers_count
			user_tweets = user.statuses_count
			user_url = user.url

			writer_tweet.writerow([all_names[tweet_inst], user_name, user_cr_dt, user_desc, user_followers, user_tweets, user_url])
			
		else:
			writer_tweet.writerow([all_names[tweet_inst], "NA", "NA", "NA", "NA", "NA", "NA"])
	except:
		pass

#Github_Module#################################################################
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)

#To write into the output file
s5_gitter = open('Stage_5_Gitter_Data.csv', 'w')
writer_gitter = csv.writer(s5_gitter)
writer_gitter.writerow(['Project_Name', 'No of Commits', 'No of Branches', 'No of Releases', 'No of Contributors', 'No of Issues', 'No of Pulls', 'No of Watches', 'No of Stars', 'No of Forks'])

commits = []
branches = []
releases = []
contributors = []
issues = []
pulls = []
watches = []
stars = []
forks = []

for instance, link in enumerate(git_url):
	try:
		driver.get(link)
		print (link)
	except:
		pass

	x = driver.find_elements_by_xpath("//span[@class='num text-emphasized']")
	time.sleep(2)
	list1 = []
	try:
		for i in x:
			list1.append(i.text)

		commits.append(list1[0])
		branches.append(list1[1])
		releases.append(list1[2])
		contributors.append(list1[3])
        
	except:
		commits.append(0)
		branches.append(0)
		releases.append(0)
		contributors.append(0)

	y = driver.find_elements_by_xpath("//span[@class='Counter']")
	time.sleep(2)
	list2 = []
	try:
		for i in y:
			list2.append(i.text)
		issues.append(list2[0])
		pulls.append(list2[1])

	except:
		issues.append(0)
		pulls.append(0) 

	z = driver.find_elements_by_xpath("//a[@class='social-count']")
	time.sleep(2)
	list3 = []
	try:
		for i in z:
			list3.append(i.text)
		watches.append(list3[0])
		forks.append(list3[1])

	except:
		watches.append(0)
		forks.append(0)

	time.sleep(2)
	try:
		s = driver.find_element_by_xpath("//a[@class = 'social-count js-social-count']")
		stars.append(s.text)
	except:
		stars.append(0)

	writer_gitter.writerow([all_names[instance], commits[instance], branches[instance], releases[instance], contributors[instance], issues[instance], pulls[instance], watches[instance], stars[instance], forks[instance]])

driver.quit()
##################################################################

time.sleep(10)

df_main = pd.read_csv("Stage_3.csv")
df_tweet = pd.read_csv("Stage_5_Twitter_Data.csv")
df_gitter = pd.read_csv("Stage_5_Gitter_Data.csv")

dfs = [df_main, df_tweet, df_gitter]
df_final = reduce(lambda left,right: pd.merge(left,right,on='Project_Name'), dfs)

df_final.to_csv("Final_Output.csv", index = False)

#Log Module {Can be Detached anytime}
end = time.time()
program = (end - start)
start_time = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

csv_stage_5 = open('Stage_5_LogFile.csv', 'a')
writer_stage_5 = csv.writer(csv_stage_5)
writer_stage_5.writerow([start_time, end_time, program])