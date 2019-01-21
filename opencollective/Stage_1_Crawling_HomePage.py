######################################################
#UTF-8 Encoded
#Created Date - Jan 18th, 2019
#Author - Raghav Ramky
#Stage_1 : Crawling Homepage for Project Names and URL
######################################################

from selenium import webdriver
import datetime
import random
import time
import csv

start = time.time()

#Writing to CSV File
csv_stage_1 = open('Stage_1.csv', 'w')
writer_stage_1 = csv.writer(csv_stage_1)
writer_stage_1.writerow(['Project Name', 'Project Link'])

#Loading Headless version of Firefox Driver in Selenium
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

#Load the Discover homepage to Selenium
driver.get("https://opencollective.com/discover")

#Stage_1_Variables
all_links = []
all_names = []

try:
	while (True):
		
		#Retrieving the links to all the projects in the page 
		link_tag = driver.find_elements_by_xpath("//a[@href]")
		links = link_tag[5:17]
		
		for link in links:
			x = link.get_attribute('href')
			all_links.append(x)
		
		#Retrieving the name of the projects from the Page
		names = driver.find_elements_by_xpath("//div[@class='jsx-136688120 name']")
		for name in names:
			all_names.append((name.text).encode('utf-8'))

		#Navigate to the next page
		next_pg = driver.find_element_by_link_text('Next')
		next_pg.click()
		time.sleep(random.randint(15, 30))

except:
	pass

#Writing Project names and links to Stage_1 CSV File
for z in range (0,757):
	writer_stage_1.writerow([all_names[z], all_links[z]])

driver.quit()

csv_stage_1 = open('Stage_1_LogFile.csv', 'a')
writer_stage_1 = csv.writer(csv_stage_1)
writer_stage_1.writerow([start_time, end_time, program])