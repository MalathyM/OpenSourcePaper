# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:18:51 2018

@author: Aru
"""

import csv
import requests
import json
f = open('F:\\Twitter+GitHub.csv', 'r', encoding="utf8")
urllist = []
readfile = csv.reader(f)
for row in readfile:
    urllist.append(row[5])
f.close()
print(urllist)

newurllist = []
xlist = ['https://github.com', 'http://github.com']
for each in urllist:
    for x in xlist:
        if x in each:
            newurllist.append(each.replace(x,"https://api.github.com"))
print(newurllist)

myToken = '97daa6ca22f09886525353c735226b877d21f72e'
myUrl = urllist[2]
head = {'Content-Type': 'application/json','Authorization': 'token {}'.format(myToken)}
response = requests.get(myUrl, headers=head)
print(response.status_code)
json.loads(response.content.decode('utf-8'))
#print(response.json())




    

