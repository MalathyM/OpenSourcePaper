from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time
import csv

#Using Chrome for Selenium
chromedriver = "/home/raghavramky/Documents/chromedriver"

#Loading the Chrome Driver in Selenium
driver = webdriver.Chrome(chromedriver)	

with open('discover_file.csv', mode='w') as discover_file:
			discover_writer = csv.writer(discover_file, delimiter = ',')
			#Loading the Website to Selenium
			driver.get("https://opencollective.com/discover")
			for i in range(0,1):
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(3)
				discover_writer.writerow(['Project_Name', 'Project_Description'])
				p_name = driver.find_elements_by_xpath('//div[@class = "CollectiveCard-name"]')
				for i in p_name:
							discover_writer.writerow([i.text])
				p_desc = driver.find_elements_by_xpath('//div[@class = "CollectiveCard-description"]')
				for i in p_desc:
							discover_writer.writerow([unicode([i.text])])
				for i in p_name:
					alpha = i.text
					driver.get("https://opencollective.com/"+alpha)
					p_team = driver.find_elements_by_xpath('//div[@class = "jsx-1387900743 name"]')
					print(p_team[0].text)
					p_ea_budget = driver.find_elements_by_xpath('//span[@class = "jsx-2826454633 annualBudget"]')
					p_curr_budget = driver.find_elements_by_xpath('//span[@class = "jsx-3142884600 amount"]')
						
