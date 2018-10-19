import json
import os
import glob

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

json_path="/Users/mohitdedhe/Desktop/MohitsDocs/Certification and Projects/VProject/Files"
json_files=[json_file for json_file in os.listdir(json_path)if json_file.endswith('.json')]
for every_file in json_files:
    print(json_path+'/'+every_file)
    data=open(json_path+'/'+every_file)
    jsonrecords=data.readlines()
    data.close()
    for line in jsonrecords:
        jsonstrings=json.loads(line)
        #print(jsonstrings)
        #print('**********inside the jsonstrings loop**********')
        if(jsonstrings['repo']['name']=='contoso-x-production/azure-xplat-cli'):
            #print('#########inside the repo name loop#############')
            for event in eventType:
                #print('%%%%%%%%%%%%%%%%checking for the event type%%%%%%%%%%%%%%%%%')
                if(jsonstrings['type']==event):
                    #print('&&&&&&&&&&&&&&getting the eventType&&&&&&&&&&&&&&&&&')
                    jsonlist.append(jsonstrings['payload'])
