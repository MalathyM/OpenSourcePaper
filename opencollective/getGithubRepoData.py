# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:18:51 2018

@author: Aru
"""

import csv
import requests
import json
from github import Github
import pandas as pd
g = Github("a108dac5324ba6d2609061e7db6b70a811409888")
dir(g)

df = pd.read_csv("F:\Twitter+GitHub.csv")
print(df.head(5))
print(df.columns)
new = df["GitHub Url"].str.split("https://github.com/", n=1, expand = True)
print(new.head())
df["Repository Path"] = new[1]
print(df.head())
df.to_csv("F:\Twitter+GitHub_New.csv", index = False)
#repo = g.get_repo("mui-org/material-ui")
#repo.forks_count

#f = open('F:\\Twitter+GitHub.csv', 'r', encoding="utf8")
#urllist = []
#readfile = csv.reader(f)
#for row in readfile:
#    urllist.append(row[5])
#f.close()
#print(urllist)
#
#newurllist = []
#xlist = ['https://github.com', 'http://github.com']
#for each in urllist:
#    for x in xlist:
#        if x in each:
#            newurllist.append(each.replace(x,"https://api.github.com"))
#print(newurllist)
#
#myToken = 'xxxxxxxxxxxxx'
#myUrl = urllist[2]
#head = {'Content-Type': 'application/json','Authorization': 'token {}'.format(myToken)}
#response = requests.get(myUrl, headers=head)
#print(response.status_code)
#json.loads(response.content.decode('utf-8'))
#print(response.json())




    

