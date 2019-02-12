##############################################
#UTF-8 Encoded
#Created Date - Jan 18th, 2019
# Author - Raghav Ramky
#Stage_2: Scrapping Details from project Pages
##############################################

from selenium import webdriver
import datetime
import random
import time
import csv

start = time.time()

#Loading Headless version of Firefox Driver in Selenium
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)

#Stage_2_Global_Variables
text_array = []
all_names = []
all_links = []

#Reading Project names and links from Stage_1 CSV File
with open('Stage_1.csv') as csv_file:
	csv_reader= csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:
			all_names.append(row[0])
			all_links.append(row[1])
			line_count += 1

#Stage_2_CSV
csv_stage_2 = open('Stage_2.csv', 'w')
writer_stage_2 = csv.writer(csv_stage_2)
writer_stage_2.writerow(['Project_Description', 'Annual_Budget', 'current_Budget', 'Twitter_Url', 'GitHub_Url', 'No of Organizations Supporting', 'No of People Supporting', 'Project_Website', 'Balance_Details', 'Team_Details'])

try: 
	for project in all_links:
			#Load the Discover homepage to Selenium
			driver.get(project)
			time.sleep(random.randint(15, 30))

			#Retrieving the Description
			desc = driver.find_elements_by_xpath('//div[@class = "jsx-2157146343 description"]')
			desc_list = []

			if desc:
				for i in desc:
					desc_list.append((i.text).encode('utf-8'))
			else:
				desc_list.append((""))

			#Retrieving the Twitter Url
			twitter = driver.find_elements_by_xpath("//div[@class='jsx-2157146343 twitterHandle']/a")
			twitter_url = ""
			if (len(twitter) > 0):
				twitter_url = twitter[0].get_attribute("href")

			#Retrieving the GitHub Url
			git = driver.find_elements_by_xpath("//div[@class='jsx-2157146343 githubHandle']/a")
			git_url = ""
			if (len(git) > 0):
				git_url = git[0].get_attribute("href")

			#Retrieving the Website Url
			web = driver.find_elements_by_xpath("//div[@class='jsx-2157146343 website']/a")
			website = ""
			if(len(web) > 0):
				url_determine = web[0].get_attribute("href")
				if "github.com" in url_determine:
					git_url = url_determine
					website = ""
				elif "twiter.com" in url_determine:
					twitter_url = url_determine
					website = ""
				else:
					website = url_determine	

			#Retrieving Annual Budget
			amt = driver.find_elements_by_xpath("//span[contains(@class, 'annualBudget')]")
			annualBudget = ""
			if (len(amt) > 0):
				annualBudget = ((amt[0].text).encode('utf-8'))

			#Retrieving Current Balance and Contributers Information
			big_array = driver.find_elements_by_xpath("//div[@class='jsx-2398233635 subtitle']")

			#Stage_2 Page_variables
			current_budget = ""
			people_support = ""
			team_details = ""
			org_support = ""
			balance = ""

			if (len(big_array) > 0):
				try:
					for element_1 in big_array:
						text_array.append((element_1.text).encode('UTF-8'))

					for element_2 in text_array:
						if "supporting us" in element_2:
							team_details = element_2
							x = element_2.split(" ")
							org_support = x[0]
							people_support = x[3]

						elif "Current balance:" in element_2:
							balance = element_2
							y = element_2.split(":")
							current_budget = y[1]

				except:
					pass
			#Writing all the page details to Stage_2 CSV File
			
			writer_stage_2.writerow([desc_list[0], annualBudget, current_budget, twitter_url, git_url, org_support, people_support, website, balance, team_details])

except:
	pass
#Close the Headless version of Firefox
driver.quit()

end = time.time()
program = (end - start)
start_time = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

csv_stage_2 = open('Stage_2_LogFile.csv', 'a')
writer_stage_2 = csv.writer(csv_stage_2)
writer_stage_2.writerow([start_time, end_time, program])