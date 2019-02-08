import json as js
import os
import pandas as pd
import csv
import xlwt
import sys
from tqdm import tqdm
datagitteruser = pd.read_csv('user_name_2017_sampled_5000.csv')
datagitteruser.head()
arrdataUserID = datagitteruser['user_name']
json_path='/home/vivek/github-data_2017/'
eventType=['CheckRunEvent',
'CheckSuiteEvent',
'CommitCommentEvent',
'CreateEvent'
,'DeleteEvent',
'DeploymentEvent'
,'DeploymentStatusEvent'
,'DownloadEvent'
,'FollowEvent'
,'ForkEvent'
,'ForkApplyEvent'
,'GitHubAppAuthorizationEvent'
,'GistEvent'
,'GollumEvent'
,'InstallationEvent'
,'InstallationRepositoriesEvent'
,'IssueCommentEvent'
,'IssuesEvent',
'LabelEvent'
,'MarketplacePurchaseEvent'
,'MemberEvent'
,'MembershipEvent'
,'MilestoneEvent'
,'OrganizationEvent'
,'OrgBlockEvent'
,'PageBuildEvent'
,'ProjectCardEvent'
,'ProjectColumnEvent'
,'ProjectEvent'
,'PublicEvent'
,'PullRequestEvent'
,'PullRequestReviewEvent',
'PullRequestReviewCommentEvent'
,'PushEvent'
,'ReleaseEvent',
'RepositoryEvent',
'RepositoryImportEvent',
'RepositoryVulnerabilityAlertEvent',
'SecurityAdvisoryEvent',
'StatusEvent',
'TeamEvent',
'TeamAddEvent',
'WatchEvent']

month_type=['1','2','3','4','5','6','7','8','9','10','11','12']

def createDummyNode(userid,arr,arr_evnt_count,eventType):
    flag =False
    for key in list(arr):
        if(key==userid):
            flag=True
            break
        else:
            flag=False
    if(flag==True):
        return arr
    else:
        for month in month_type:
            for event in eventType:
                arr_evnt_count.update({event:0})
                arr.update({userid+"_"+month:arr_evnt_count})
        return arr
    

    
#creating the dictionary to store the unique ids and there eventcounts
arr=dict()
#this will have the event names and its counts for the perticular userid
arr_evnt_count=dict()
#data looks {login_Month:{even1:4,event2:5, event4:5}}
#data looks like in excel sheet is below
#UserID Month  NoEven1 NoEvent2 NoEvent3 NoEvent4 NoEvent5 NoEvent6 
#mdeh  Jan         1        2        3       5        7         0 
#i is used for the first iteration of the dictionary insert key and value pair
i=0
countexc=0
#getting the files list from the given path
json_files=[json_file for json_file in os.listdir(json_path)if json_file.endswith('.json')]
#iterating the files using For loop
for every_file in tqdm(json_files):
    data=open(json_path+'/'+every_file)
    monthValue=every_file[5:7]
    #reading the data and store it to the jsonrecord for the signle file
    jsonrecords=data.readlines()
    data.close()
    #iteration over the data line by line and loading to the json form
    for line in jsonrecords:
        jsonstrings=js.loads(line)
        #use unique Gitter UserID and now comparing the Gitter with Github login.
        #for userid in arrdataUserID:
        try:
            if(jsonstrings['actor']['login'] in arrdataUserID):
                #creating the dummy nodes for all the events and checking whether the userID is alread there before creating it
                arr=createDummyNode(userid,arr,arr_evnt_count,eventType)
                #first iteration of loop and adding first element directly to dictionary
                eventName=jsonstrings['type']
                if(i==0):
                    arr_evnt_count.update({eventName:1})
                    arr.update({userid+"_"+monthValue:arr_evnt_count})
                    i=1
                else:
                    #from the next iteration checking whether the userid already present or not
                    for key in list(arr):
                        if(key==userid):
                            k=arr.get(key)
                            val=k.get(eventName)
                            val=val+1;
                            k.update({eventName:val})
                            arr.update({userid+"_"+monthValue:k})
                            val=0
                        else:
                            arr_evnt_count.update({eventName:1})
                            arr.update({userid+"_"+monthValue:arr_evnt_count})
            #print('count of exception',countexc) 
        except:
            countexc=countexc+1
            #print("done",e)
print("Number of exceptions="+str(countexc))
header=['UserID', 'Month','CheckRunEvent',
'CheckSuiteEvent',
'CommitCommentEvent',
'CreateEvent'
,'DeleteEvent',
'DeploymentEvent'
,'DeploymentStatusEvent'
,'DownloadEvent'
,'FollowEvent'
,'ForkEvent'
,'ForkApplyEvent'
,'GitHubAppAuthorizationEvent'
,'GistEvent'
,'GollumEvent'
,'InstallationEvent'
,'InstallationRepositoriesEvent'
,'IssueCommentEvent'
,'IssuesEvent',
'LabelEvent'
,'MarketplacePurchaseEvent'
,'MemberEvent'
,'MembershipEvent'
,'MilestoneEvent'
,'OrganizationEvent'
,'OrgBlockEvent'
,'PageBuildEvent'
,'ProjectCardEvent'
,'ProjectColumnEvent'
,'ProjectEvent'
,'PublicEvent'
,'PullRequestEvent'
,'PullRequestReviewEvent',
'PullRequestReviewCommentEvent'
,'PushEvent'
,'ReleaseEvent',
'RepositoryEvent',
'RepositoryImportEvent',
'RepositoryVulnerabilityAlertEvent',
'SecurityAdvisoryEvent',
'StatusEvent',
'TeamEvent',
'TeamAddEvent',
'WatchEvent']



#creating csv using the dictionary values 
with open('githubGittercollection.csv','w',newline='') as csvfile:
    fieldnames = ['UserID', 'Month','CheckRunEvent',
'CheckSuiteEvent',
'CommitCommentEvent',
'CreateEvent'
,'DeleteEvent',
'DeploymentEvent'
,'DeploymentStatusEvent'
,'DownloadEvent'
,'FollowEvent'
,'ForkEvent'
,'ForkApplyEvent'
,'GitHubAppAuthorizationEvent'
,'GistEvent'
,'GollumEvent'
,'InstallationEvent'
,'InstallationRepositoriesEvent'
,'IssueCommentEvent'
,'IssuesEvent',
'LabelEvent'
,'MarketplacePurchaseEvent'
,'MemberEvent'
,'MembershipEvent'
,'MilestoneEvent'
,'OrganizationEvent'
,'OrgBlockEvent'
,'PageBuildEvent'
,'ProjectCardEvent'
,'ProjectColumnEvent'
,'ProjectEvent'
,'PublicEvent'
,'PullRequestEvent'
,'PullRequestReviewEvent',
'PullRequestReviewCommentEvent'
,'PushEvent'
,'ReleaseEvent',
'RepositoryEvent',
'RepositoryImportEvent',
'RepositoryVulnerabilityAlertEvent',
'SecurityAdvisoryEvent',
'StatusEvent',
'TeamEvent',
'TeamAddEvent',
'WatchEvent']
    writer = csv.writer(csvfile, dialect='excel')
    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(header)
    for key in list(arr):
        uid_mon = key
        um=key.split('_')
        uid = um[0]
        mon=um[1]
        innerdict=arr.get(key)
        l=list()
        l.append(uid)
        l.append(mon)
        for keyevent in list(innerdict):
            keyevname = keyevent
            val=innerdict.get(keyevname)
            l.append(val)
        writer.writerow(l)
