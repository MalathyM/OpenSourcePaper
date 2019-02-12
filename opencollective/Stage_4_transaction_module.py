###############################################################
#UTF-8 Encoded
#Created Date - Jan 18th, 2019
# Author - Raghav Ramky
#Stage_4: Getting the transaction files for projects in Stage_3 
#Download the transaction File
#Rename it to the name of the project
###############################################################

from selenium import webdriver

import datetime
import random
import shutil
import time
import sys
import csv
import os

start = time.time()

#Stage_4 Global Variables
file_path = '/home/raghavramky/Downloads/'
all_names = []
all_url = []

#To Read from our CSV File
with open('Stage_3.csv') as csv_file:
	csv_reader= csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:
			all_names.append(row[0])
			all_url.append(row[1])
			line_count += 1

#Module to Check for the Latest file in a path and rename the downloaded File
def file_rename(newname, folder_of_download):
	    filename = max([f for f in os.listdir(folder_of_download)], key=lambda xa :   os.path.getctime(os.path.join(folder_of_download,xa)))
	    if '.part' in filename:
	        time.sleep(1)
	        os.rename(os.path.join(folder_of_download, filename), os.path.join(folder_of_download, newname))
	    else:
	        os.rename(os.path.join(folder_of_download, filename),os.path.join(folder_of_download,newname))

#Loading Headless version of Firefox Driver in Selenium
driver = webdriver.Chrome()

for instance, alpha in enumerate(all_url):
	
	target_filename = (all_names[instance]+".csv")

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

#Log Module {Can be Detached anytime}
end = time.time()
program = (end - start)
start_time = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

csv_stage_4 = open('Stage_4_LogFile.csv', 'a')
writer_stage_4 = csv.writer(csv_stage_4)
writer_stage_4.writerow([start_time, end_time, program])