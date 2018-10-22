import json
import os
import glob
import sys
import path
#creating the list of eventType to find out in the repo on the basis of for loop

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


#creating the list to append the final output in it
jsonlist=[]
jsonNlist=[]
jsonRlist=[]
result = dict()
result1=dict()

if(len(sys.argv)<2):
    print("Error: .py <parameter> 1. Mohit 2. Vivek's server 3. ")

if(sys.argv[1]=='1'):
    json_path="/Users/mohitdedhe/Desktop/MohitsDocs/Certification and Projects/VProject/Files"
elif (sys.argv[1]=='2'):
    json_path='/home/vivek/github-data'
elif (sys.argv[2]=='3'):
    json_path=path.json
elif (sys.argv[3]=='4'):
    json_path=path.json
elif (sys.argv[4]=='5'):
    json_path=path.
else:
    print('Provide correct parameter')

json_files=[json_file for json_file in os.listdir(json_path)if json_file.endswith('.json')]
for every_file in json_files:
    print(json_path+'/'+every_file)
    data=open(json_path+'/'+every_file)
    jsonrecords=data.readlines()
    data.close()
    for line in jsonrecords:
        jsonstrings=json.loads(line)
        #print(jsonstrings)
        if(jsonstrings['repo']['name']=='contoso-x-production/azure-xplat-cli'):
            for event in eventType:
                if(jsonstrings['type']==event):
                    jsonlist.append(jsonstrings['type'])
                    result.update({every_file+str(uuid):jsonstrings['type']+', '+jsonstrings['actor']['avatar_url']+', '+jsonstrings['created_at']})
                    uuid=uuid+1
                elif(jsonstrings['type']!=event and len(eventType)==eventType.index(event)):
                    jsonNlist.append(jsonstrings['type'])
                    result1.update({every_file+str(uuid):jsonstrings['type']+', '+jsonstrings['actor']['avatar_url']+', '+jsonstrings['created_at']})
                    uuid=uuid+1
