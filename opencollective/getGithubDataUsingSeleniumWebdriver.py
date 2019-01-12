# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 18:14:37 2019

@author: Aru
"""

from selenium import webdriver
import pandas as pd
import time

chromedriver = "C:/Web Drivers"
driver = webdriver.Chrome(executable_path = "chromedriver")

df = pd.read_csv("F:\Twitter+GitHub.csv")

commits = []
branches = []
releases = []
contributors = []
issues = []
pulls = []
watches = []
stars = []
forks = []

for link in df["GitHub_Url"]:
    driver.get(link)
    x = driver.find_elements_by_xpath("//span[@class='num text-emphasized']")
    time.sleep(2)
    list1 = []  
    try:
    
        
        for i in x:
            list1.append(i.text)
        commits.append(list1[0])
        branches.append(list1[1])
        releases.append(list1[2])
        contributors.append(list1[3])
        
    except:
       
       commits.append(0)
       branches.append(0)
       releases.append(0)
       contributors.append(0)
       
    
    y = driver.find_elements_by_xpath("//span[@class='Counter']")
    time.sleep(2)
    list2 = []
    try:
        for i in y:
            list2.append(i.text)
        issues.append(list2[0])
        pulls.append(list2[1])
        
    except:
       issues.append(0)
       pulls.append(0) 
    
    
    z = driver.find_elements_by_xpath("//a[@class='social-count']")
    time.sleep(2)
    list3 = []
    try:
        for i in z:
            list3.append(i.text)
        watches.append(list3[0])
        forks.append(list3[1])
        
    except:
        watches.append(0)
        forks.append(0)
        
        

    s = driver.find_element_by_xpath("//a[@class = 'social-count js-social-count']")
    time.sleep(2)
    try:
        stars.append(s.text)
    except:
        stars.append(0)
        
    
    
#print(commits)

df["commits"] = commits
df["branches"] = branches
df["releases"] = releases
df["contributors"] = contributors
df["issues"] = issues
del issues[21]
df["pulls"] = pulls
df["watches"] = watches
df["stars"] = stars
df["forks"] = forks

print(df.head(5))

df.to_csv("F:\Twitter+GitHub_New2.csv", index = False)

