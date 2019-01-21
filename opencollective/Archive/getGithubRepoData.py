# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:18:51 2018

@author: Aru
"""

from github import Github
import pandas as pd
import socket
g = Github("9a943c0128ea8806c6e364701aa106fa4ea3ab2c")
dir(g)

#df = pd.read_csv("F:\Twitter+GitHub.csv")
#print(df.head(5))
#print(df.columns)
#new = df["GitHub Url"].str.split("https://github.com/", n=1, expand = True)
#print(new.head())
#df["Repository Path"] = new[1]
#print(df.head())
#df.to_csv("F:\Twitter+GitHub_New.csv", index = False)

if(socket.gethostname()=='c063144'):
    path='C:\\Users\\vivek4\\Downloads\\gitterFiles\\'
else:
    path='F:\\'
# A copy of following file is available in google drive at 
# Github-Gitter Project>OpenCollective>arundhati_files
newdf = pd.read_csv(path+"Twitter+GitHub_New1.csv")

commits = []
branches = []
contributors = []
issues = []
releases = []
pulls = []

for each in newdf["Repository Path"]:
    repo = g.get_repo(each)
    
    # Commits
    commits_count = repo.get_commits().totalCount
    commits.append(commits_count)
    
    #Branches
    branches_count = repo.get_branches().totalCount
    branches.append(branches_count)  

    #Contributors 
    contributors_count = repo.get_contributors().totalCount
    #for _ in repo.get_stats_contributors():
    #    contributors_count = contributors_count + 1
    contributors.append(contributors_count)
 
    #Issues
    issues_count = repo.open_issues_count
    issues.append(issues_count)

    #Releases
    releases_count = repo.get_releases().totalCount
    #for _ in repo.get_releases():
    #    releases_count = releases_count + 1
    releases.append(releases_count)

    #Pulls
    pulls_count = repo.get_pulls().totalCount
    #for _ in repo.get_pulls():
    #    pulls_count = pulls_count + 1
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






    






    

