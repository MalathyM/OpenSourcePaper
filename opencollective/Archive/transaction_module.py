from selenium import webdriver
import random
import time
#driver = webdriver.Firefox()

driver = webdriver.Chrome(executable_path = "chromedriver")

driver.get("https://opencollective.com/discover")

all_links = []
time.sleep(5)

while (True):
	#to be commented
	#if (len(all_links) > 5):
	#	break
	
	link_tag = driver.find_elements_by_xpath("//a[@href]")
	link = link_tag[5:17]
	for i in link:
				x = i.get_attribute('href')
				all_links.append(x)
	#navigate to the next page
	next_pg = driver.find_element_by_link_text('Next')
	next_pg.click()
	time.sleep(random.randint(15, 30))

for alpha in all_links:
	driver.get(alpha+"/transactions")
	time.sleep(2)
	downloadcsv_button = driver.find_element_by_xpath('//a[@class = "download-csv"]')
	downloadcsv_button.click()

	time.sleep(2)

	start_date = driver.find_element_by_xpath("//input[contains(@class, 'form-control')]")

	time.sleep(5)
	start_date.click()
	start_date.clear()
	start_date.send_keys("01/01/2000")
	download_button = driver.find_element_by_xpath("//button[@class='btn btn-sm btn-primary']")
	download_button.click()
	time.sleep(20)
