import json as js
import os
import pandas as pd
#file for the unique id from Gitter
datagitteruser = pd.read_csv('/Volumes/BootCamp/MohitsDocs/Certification and Projects/VProject/Files/csv/user_name_2017.csv')
#create a list of the unique IDs
arrdataUserID = datagitteruser['username']
#file path for GitHub Data which is in Json
json_path='/Volumes/BootCamp/MohitsDocs/Certification and Projects/VProject/Files/'
#eventTypes on GitHub
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
#Function to create the userId and all the events with the count of 0 to initialized the counting
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
        for event in eventType:
            arr_evnt_count.update({event:0})
            arr.update({userid:arr_evnt_count})
        return arr
 #end of the function
#starting of the main function which can create the dictionary 
#creating the dictionary to store the unique ids and there eventcounts
arr=dict()
#this will have the event names and its counts for the perticular userid
arr_evnt_count=dict()
#data looks {moht:{even1:4,event2:5, event4:5}}
#i is used for the first iteration of the dictionary insert key and value pair
i=0
#getting the files list from the given path
json_files=[json_file for json_file in os.listdir(json_path)if json_file.endswith('.json')]
#iterating the files using For loop
for every_file in json_files:
    data=open(json_path+'/'+every_file)
    #reading the data and store it to the jsonrecord for the signle file
    jsonrecords=data.readlines()
    data.close()
    #iteration over the data line by line and loading to the json form
    for line in jsonrecords:
        jsonstrings=js.loads(line)
        #use unique Gitter UserID and now comparing the Gitter with Github login.
        for userid in arrdataUserID:
            if(jsonstrings['actor']['login']==userid):
                #creating the dummy nodes for all the events and checking whether the userID is alread there before creating it
                arr=createDummyNode(userid,arr,arr_evnt_count,eventType)
                #first iteration of loop and adding first element directly to dictionary
                eventName=jsonstrings['type']
                if(i==0):
                    arr_evnt_count.update({eventName:1})
                    arr.update({userid:arr_evnt_count})
                    i=1
                else:
                    #from the next iteration checking whether the userid already present or not
                    for key in list(arr):
                            if(key==userid):
                                k=arr.get(key)
                                val=k.get(eventName)
                                val=val+1;
                                k.update({eventName:val})
                                arr.update({userid:k})
                                val=0
                            else:
                                arr_evnt_count.update({eventName:1})
                                arr.update({userid:arr_evnt_count})
    
