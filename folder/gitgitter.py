import json as js
import os
import pandas as pd
import csv
import xlwt
import sys
datagitteruser = pd.read_csv('/Volumes/BootCamp/MohitsDocs/Certification and Projects/VProject/Files/user_name_2017_sampled_5000.csv')
datagitteruser.head()
arrdataUserID = datagitteruser['user_name']
json_path='/Volumes/BootCamp/MohitsDocs/Certification and Projects/VProject/Files/'
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

month_type=['01/1/2017','02/1/2017','03/1/2017','04/1/2017','05/1/2017','06/1/2017','07/1/2017','08/1/2017','09/1/2017','10/1/2017','11/1/2017','12/1/2017']

def createDummyNode(userid,monthValue,arr,eventType):
    arr_evnt_count=dict()
    flag =False
    for key in list(arr):
        com1=userid+"_"+monthValue
        
        
        if(key==com1):
            flag=True
            break
        else:
            flag=False
    if(flag==True):
        return arr
    else:
        for event in eventType:
            arr_evnt_count.update({event:0})
        for month in month_type:
            arr.update({userid+"_"+month:arr_evnt_count})
        return arr

#creating the dictionary to store the unique ids and there eventcounts
arr=dict()
#this will have the event names and its counts for the perticular userid
#data looks {login_Month:{even1:4,event2:5, event4:5}}
#data looks like in excel sheet is below
#UserID Month  NoEven1 NoEvent2 NoEvent3 NoEvent4 NoEvent5 NoEvent6 
#mdeh  Jan         1        2        3       5        7         0 
#i is used for the first iteration of the dictionary insert key and value pair
i=0
#getting the files list from the given path
try:
    json_files=[json_file for json_file in os.listdir(json_path)if json_file.endswith('.json')]
    #iterating the files using For loop
    for every_file in json_files:
        data=open(json_path+'/'+every_file)
        monthValue=every_file[5:7]+"/1/2017"
        #reading the data and store it to the jsonrecord for the signle file
        jsonrecords=data.readlines()
        data.close()
        #iteration over the data line by line and loading to the json form
        for line in jsonrecords:
            jsonstrings=js.loads(line)
            if(jsonstrings['actor']['login'] in list(arrdataUserID)):
                #creating the dummy nodes for all the events and checking whether the userID is alread there before creating it
                userid=jsonstrings['actor']['login']
                arr=createDummyNode(userid,monthValue,arr,eventType)
                #first iteration of loop and adding first element directly to dictionary
                eventName=jsonstrings['type']
                
                for key, value in arr.items():
                    com=userid+"_"+monthValue
                    if(key==com):
                    	for ikey, ivalue in value.items():
                    		if(ikey==eventName):
                    			ivalue=ivalue+1
                    			newval=value.copy()
                    			newval.update({ikey:ivalue})
                    			break
                    	arr.update({key:newval})
                    	val=0
except Exception as e:
    print(e)


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
with open('/Volumes/BootCamp/MohitsDocs/Certification and Projects/VProject/githubGittercollection.csv','w',newline='') as csvfile:
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

