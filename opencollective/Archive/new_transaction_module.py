# Author: Raghav
# Purpose: 
from selenium import webdriver
import random
import shutil
import time
import csv
import os

file_path = '/home/raghavramky/Downloads/'
all_names = []
all_url = []

csvFile_main = open('Budget&team_details_new.csv', 'w')
writer_main = csv.writer(csvFile_main)
writer_main.writerow(['Project Name', 'Description', 'Current Budget', 'Team Info'])

#Module to Check for the Latest file in a path and rename the downloaded File
def file_rename(newname, folder_of_download):
	    filename = max([f for f in os.listdir(folder_of_download)], key=lambda xa :   os.path.getctime(os.path.join(folder_of_download,xa)))
	    if '.part' in filename:
	        time.sleep(1)
	        os.rename(os.path.join(folder_of_download, filename), os.path.join(folder_of_download, newname))
	    else:
	        os.rename(os.path.join(folder_of_download, filename),os.path.join(folder_of_download,newname))


driver = webdriver.Chrome()

#To Read from our CSV File
with open('test.csv') as csv_file:
	csv_reader= csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:
			all_names.append(row[0])
			all_url.append(row[8])
			line_count += 1

for instance, alpha in enumerate(all_url):
	
	target_filename = (all_names[instance]+".csv")

	driver.get(alpha+"#budget")

	amt = driver.find_elements_by_xpath("//div[@class='jsx-2398233635 subtitle']")
	amt_list = ""
	team_list = ""
	if (len(amt) > 0):
		try:
			desc_list = ((amt[1].text).encode('utf-8'))
			amt_list = ((amt[2].text).encode('utf-8'))
			team_list = ((amt[3].text).encode('utf-8'))
		except:
			pass
	writer_main.writerow([all_names[instance], desc_list, amt_list, team_list])

	driver.get(alpha+"/transactions")

	curr_budget = driver.find_elements_by_xpath("//div[@class='jsx-136688120 value']")
	

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
	try:
		file_rename(target_filename, file_path)
	except:
		pass
