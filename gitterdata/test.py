from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time

#Using Chrome for Selenium
chromedriver = "/home/raghavramky/Documents/chromedriver"

#Loading the Chrome Driver in Selenium
driver = webdriver.Chrome(chromedriver)	

#Loading the Website to Selenium
driver.get("https://opencollective.com/discover")
for i in range(0,10):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(3)

#Traversing to the end file
#eow = driver.find_element_by_tag_name('html')
#eow.send_keys(Keys.END)

time.sleep(10)

p_name = driver.find_elements_by_xpath('//div[@class = "CollectiveCard-name"]')
for i in p_name:
	print("Project Name : " + i.text)
	alpha = i.text
	driver.get("https://opencollective.com/"+alpha)
	p_desc = driver.find_elements_by_xpath('//p[@class = "jsx-2501124983 description"]')
	for x in p_desc:
		print ("Project Description: " + x.text)	
	
	p_team = driver.find_elements_by_xpath('//div[@class = "jsx-1387900743 name"]')
	for x in p_team:
		print ("The Team members are : " + x.text)

	p_ea_budget = driver.find_elements_by_xpath('//span[@class = "jsx-2826454633 annualBudget"]')
	for x in p_ea_budget:
		print ("The Estimated Annual Budget is: " + x.text)

	p_curr_budget = driver.find_elements_by_xpath('//span[@class = "jsx-3142884600 amount"]')
	for x in p_curr_budget:
		print ("The Current Budget is: " + x.text)	

	#Prototype
	#r_ea_budget = [x.text for x in p_ea_budget]
	#print (r_ea_budget)
	
#p_desc = driver.find_elements_by_xpath('//div[@class = "CollectiveCard-description"]')
#r_desc = [y.text for y in p_desc]

#print (r_name)

with open('discover_file.csv', mode='w') as discover_file:
	discover_writer = csv.writer(discover_file, delimiter = ',')
	discover_writer.writerow(r_name)
#discover_writer.writerow(r_desc)
