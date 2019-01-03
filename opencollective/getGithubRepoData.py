# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:18:51 2018

@author: Aru
"""

from github import Github
import pandas as pd
g = Github("XXXXXXXXXXXXXXXX")
dir(g)

#df = pd.read_csv("F:\Twitter+GitHub.csv")
#print(df.head(5))
#print(df.columns)
#new = df["GitHub Url"].str.split("https://github.com/", n=1, expand = True)
#print(new.head())
#df["Repository Path"] = new[1]
#print(df.head())
#df.to_csv("F:\Twitter+GitHub_New.csv", index = False)
newdf = pd.read_csv("F:\Twitter+GitHub_New1.csv")

commits = []
branches = []
contributors = []
issues = []
releases = []
pulls = []

for each in newdf["Repository Path"]:
    repo = g.get_repo(each)
    
    # Commits
    commits_count = 0
    for _ in repo.get_commits():
        commits_count = commits_count + 1
    commits.append(commits_count)
    
    #Branches
    branches_count = 0
    for _ in repo.get_branches():
        branches_count = branches_count + 1
    branches.append(branches_count)  

    #Contributors 
    contributors_count = 0
    for _ in repo.get_stats_contributors():
        contributors_count = contributors_count + 1
    contributors.append(contributors_count)
 
    #Issues
    issues_count = repo.open_issues_count
    issues.append(issues_count)

    #Releases
    releases_count = 0
    for _ in repo.get_releases():
        releases_count = releases_count + 1
    releases.append(releases_count)

    #Pulls
    pulls_count = 0
    for _ in repo.get_pulls():
        pulls_count = pulls_count + 1
    pulls.append(pulls_count)

# Adding the lists to the dataframe
newdf["Commits"] = commits
newdf["Branches"] = branches
newdf["Contributors"]  = contributors
newdf["Issues"] = issues
newdf["Releases"] = releases
newdf["Pulls"] = pulls

print(newdf.head())

# Wrting the new data frame back to Csv file
newdf.to_csv("F:\Twitter+GitHub_New1.csv", index = False)




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




    






    

