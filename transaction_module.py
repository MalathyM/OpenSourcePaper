# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time

chromedriver = "C:/Web Drivers"
driver = webdriver.Chrome(executable_path = "chromedriver")

driver.get('https://opencollective.com/wwcode/transactions')

downloadcsv_button = driver.find_element_by_xpath('//a[@class = "download-csv"]')
downloadcsv_button.click()

#amt = driver.find_elements_by_xpath("//span[contains(@class, 'annualBudget')]")

start_date = driver.find_element_by_xpath("//input[contains(@class, 'form-control')]")

time.sleep(5)
start_date.click()
start_date.clear()
start_date.send_keys("01/01/2000")
download_button = driver.find_element_by_xpath('//*[@id="csv-date-range"]/div[2]/button')
download_button.click()