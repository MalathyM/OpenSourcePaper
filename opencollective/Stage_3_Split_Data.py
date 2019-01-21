##########################################################
#UTF-8 Encoded
#Created Date - Jan 18th, 2019
#Author - Raghav Ramky
#Stage_3: Filtering_the_output
#Convert currency to its
#Merge the csv files
#Filter out the dataframe for the Twitter and Github links
##########################################################

import pandas as pd
import numpy as np
import datetime
import time
import csv
import re

start = time.time()

#Stage_3_variables
current_currency_symbol = []
annual_currency_symbol = []
current_currency_value = []
annual_currency_value = []
corr_gitter = []
project = []
twitter = []
website = []
current = []
github = []
annual = []
names = []
desc = []
tweet= []
org = []
ppl = []

#Reading Project names and links from Stage_1 CSV File
with open('Stage_1.csv') as csv_file:
	csv_reader= csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:
			names.append(row[0])
			project.append(row[1])
			line_count += 1

#Reading Project related details from Stage_2
with open('Stage_2.csv') as csv_file:
	csv_reader= csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:
			desc.append(row[0])
			annual.append(row[1])
			current.append(row[2])
			tweet.append(row[3])
			github.append(row[4])
			org.append(row[5])
			ppl.append(row[6])
			website.append(row[7])
			line_count += 1

#Writing to a csv File
csv_stage_2_cleaned = open('Stage_2_Cleaned.csv', 'w')
writer_stage_2_cleaned = csv.writer(csv_stage_2_cleaned)
writer_stage_2_cleaned.writerow(['Project_Name', 'Project_Url', 'Project_Description', 'Currency', 'Annual_Budget', 'Current_Budget', 'Twitter_Username', 'GitHub_Url', 'No_of_Organizations', 'No_of_People_Supporting', 'Project_Website'])

#Cleaning the incoming data
for string in annual:
	if string:	
		match = re.search(r'([\D]+)([\d,]+)', string)
		annual_currency_symbol.append(match.group(1))
		annual_currency_value.append(match.group(2).replace(',',''))
	else:
		annual_currency_symbol.append("")
		annual_currency_value.append("")

for string in current:
	if string:
		match = re.search(r'([\D]+)([\d,]+)', string)
		current_currency_symbol.append(match.group(1))
		current_currency_value.append(match.group(2).replace(',',''))
	else:
		current_currency_symbol.append("")
		current_currency_value.append("")

#Conversion of Currency Value:

#Split Twitter Username and the 
for link in tweet:
	if link:
		tweet_tmp = link.split(".com/")
		twitter.append(tweet_tmp[1])
	else:
		twitter.append("")

for instance, t in enumerate(twitter):
	if t == "babeljs":
		corr_gitter.append("https://github.com/babel/babel")
	elif t == "feathersjs":
		corr_gitter.append("https://github.com/feathersjs/feathers/feathersjs/feathers")
	elif t == "electronjs":
		corr_gitter.append("https://github.com/electron/electron")
	elif t == "ParsePlatform":
		corr_gitter.append("https://github.com/parse-community/parse-server")
	elif t == "darkreaderapp":
		corr_gitter.append("https://github.com/darkreader/darkreader")
	elif t == "idyll_lang":
		corr_gitter.append("https://github.com/idyll-lang/idyll")
	elif t == "foxhound87":
		corr_gitter.append("https://github.com/foxhound87/mobx-react-form")
	elif t == "getgrav":
		corr_gitter.append("https://github.com/getgrav/grav")
	elif t == "djangolondon":
		corr_gitter.append("https://github.com/djangolondon/djangolondon.github.io")
	elif t == "codeformiami":
		corr_gitter.append("https://github.com/Code-for-Miami/repository_status_keys")
	elif t == "simplysecureorg":
		corr_gitter.append("https://github.com/simplysecure/resources")	
	elif t == "octoboxio":
		corr_gitter.append("https://github.com/octobox/octobox")
	elif t == "yourls":
		corr_gitter.append("https://github.com/YOURLS/YOURLS")
	elif t == "FodyProject":
		corr_gitter.append("https://github.com/Fody/Fody")
	elif t == "hospitalrun":
		corr_gitter.append("https://github.com/HospitalRun/hospitalrun-frontend")
	elif t == "opensrcdesign":
		corr_gitter.append("https://github.com/CaptainFact/captain-fact-api")
	elif t == "ReactDenver":
		corr_gitter.append(" ")
	elif t == "AvogadroChem":
		corr_gitter.append("https://github.com/Avogadro/avogadro")
	elif t == "verdaccio_npm":
		corr_gitter.append("https://github.com/verdaccio/verdaccio")
	elif t == "ReactJSDallas":
		corr_gitter.append("https://github.com/reactjs-dallas/reactjs-dallas-site")
	elif t == "erikras":
		corr_gitter.append("https://github.com/final-form/final-form")
	elif t == "ArchiveBot":
		corr_gitter.append("https://github.com/ArchiveTeam/wpull")
	elif t == "ToSDR":
		corr_gitter.append("https://github.com/tosdr/tosback2")
	elif t == "AccelerateAI":
		corr_gitter.append("https://github.com/AccelAI/DemystifyingDeepLearning-AI")
	elif t == "buttercup_pw":
		corr_gitter.append("https://github.com/buttercup/buttercup-desktop")
	elif t == "kivyframework":
		corr_gitter.append("https://github.com/kivy/kivy")
	elif t == "dat_project":
		corr_gitter.append("https://github.com/datproject/dat")
	elif t == "Cheeselab":
		corr_gitter.append(" ")
	elif t == "cheton":
		corr_gitter.append("https://github.com/cncjs/cncjs")
	elif t == "souschefsorg":
		corr_gitter.append("https://github.com/sous-chefs/java")
	elif t == "sachadso":
		corr_gitter.append("https://github.com/freshOS")
	elif t == "hoaproject":
		corr_gitter.append("https://github.com/hoaproject/Console")
	elif t == "osdiversity":
		corr_gitter.append("https://github.com/opensourcediversity")
	elif t == "thpatch":
		corr_gitter.append("https://github.com/thpatch/thcrap")
	elif t == "ZNotesRevision":
		corr_gitter.append("https://github.com/ZNotes/notes")
	elif t == "MidnightLizard":
		corr_gitter.append("https://github.com/Midnight-Lizard/Midnight-Lizard")
	elif t == "getbootstrap":
		corr_gitter.append("https://github.com/twbs/bootstrap")
	elif t == "_hexworks":
		corr_gitter.append("https://github.com/Hexworks/zircon")
	elif t == "sarapisorg":
		corr_gitter.append(" ")
	else:
		corr_gitter.append(github[instance])

#Combining both Stage_1 and Stage_2 files
for i, item in enumerate(names):
	writer_stage_2_cleaned.writerow([names[i], project[i], desc[i], annual_currency_symbol[i], annual_currency_value[i], current_currency_value[i], twitter[i], corr_gitter[i], org[i], ppl[i], website[i]])

time.sleep(20)

#Filtering only the projects which have Twitter and Github url's
df = pd.read_csv("Stage_2_Cleaned.csv", engine = 'python')
df['Twitter_Username'].replace('', np.nan, inplace=True)
df['GitHub_Url'].replace('', np.nan, inplace=True)

df.dropna(subset=['Twitter_Username'], inplace=True)
df.dropna(subset=['GitHub_Url'], inplace=True)

df.to_csv("Stage_3.csv", index = False)

#Log Module {Can be Detached anytime}
end = time.time()
program = (end - start)
start_time = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

csv_stage_2 = open('Stage_3_LogFile.csv', 'a')
writer_stage_2 = csv.writer(csv_stage_2)
writer_stage_2.writerow([start_time, end_time, program])