from selenium import webdriver
import random
import time
import csv

csvFile_main = open('output_main.csv', 'w')
writer_main = csv.writer(csvFile_main)
writer_main.writerow(['Project_Description', 'Budget', 'Website', 'GitHub Url', 'Twitter Url'])

csvFile_sub = open('output_sub.csv', 'w')
writer_sub = csv.writer(csvFile_sub)
writer_sub.writerow(['Project Name', 'No of Backers', 'Project Link'])

#Loading the Firefox Driver in Selenium
driver = webdriver.Firefox()

#Loading the Website to Selenium
driver.get("https://opencollective.com/discover")

all_backers = []
all_links = []
all_names = []
try:
	while (True):
		#to be commented
		#if (len(all_links) > 5):
		#	break
		link_tag = driver.find_elements_by_xpath("//a[@href]")
		link = link_tag[5:17]
		
		for i in link:
			x = i.get_attribute('href')
			all_links.append(x)
		
		#Get all the names from the Page
		name = driver.find_elements_by_xpath("//div[@class='jsx-136688120 name']")
		for i in name:
			all_names.append((i.text).encode('utf-8'))

		#get all backers for a page
		backers = driver.find_elements_by_xpath("//div[@class='jsx-136688120 value']")
		for i in backers:
			if not ("," or "$") in (i.text):
				all_backers.append((i.text).encode('utf-8'))

		#navigate to the next page
		next_pg = driver.find_element_by_link_text('Next')
		next_pg.click()
		time.sleep(random.randint(15, 30))
	
except:

	for z in range (0,733):
		writer_sub.writerow([all_names[z], all_backers[z], all_links[z]])
	
	for i in all_links:
		driver.get(i)
		time.sleep(random.randint(15, 30))
		desc = driver.find_elements_by_xpath('//div[@class = "jsx-2157146343 description"]')
		desc_list = []
		if desc:
			for i in desc:
				desc_list.append((i.text).encode('utf-8'))
			print desc_list[0]
		else:
			desc_list.append((""))
			print desc_list[0]

		amt = driver.find_elements_by_xpath("//span[contains(@class, 'annualBudget')]")
		amt_list = ""
		if (len(amt) > 0):
			amt_list = ((amt[0].text).encode('utf-8'))
		
		web = driver.find_elements_by_xpath("//div[@class='jsx-2157146343 website']/a")
		url = ""
		if(len(web) > 0):
			url = web[0].get_attribute("href")

		git = driver.find_elements_by_xpath("//div[@class='jsx-2157146343 githubHandle']/a")
		git_url = ""
		if (len(git) > 0):
			git_url = git[0].get_attribute("href")

		twitter = driver.find_elements_by_xpath("//div[@class='jsx-2157146343 twitterHandle']/a")
		twitter_url = ""
		if (len(twitter) > 0):
			twitter_url = twitter[0].get_attribute("href")

		#final output
		writer_main.writerow([desc_list[0], amt_list, url, git_url, twitter_url])
