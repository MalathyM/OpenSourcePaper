import json
import os
import glob
import csv
import os
import xlwt
import sys
from tqdm import tqdm
# this is to get the path variable from the path.py file
import path
projectAI=['keras-team/keras','accord-net/framework','scikit-learn/scikit-learn','Microsoft/CNTK','Reference-LAPACK/lapack-release'
        ,'BVLC/caffe','Theano/Theano','torch/torch7','tensorflow/tensorflow','google-research/bert','pytorch/pytorch']
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

jsonNlist=[]

if(len(sys.argv)<2):
    print("Error: .py <parameter> 1. Mohit 2. Vivek's server 3. Arundathi's server 4. Malathy's server 5. Nameetha's server")

if(sys.argv[1]=='1'):
    json_path=path.Json_Mohit
elif (sys.argv[1]=='2'):
    json_path=path.Json_Vivek
elif (sys.argv[2]=='3'):
    json_path=path.Json_Arundathi
elif (sys.argv[3]=='4'):
    json_path=path.Json_Malathy
elif (sys.argv[4]=='5'):
    json_path=path.Json_Nameetha
else:
    print('Provide correct parameter')

#json_path="/Users/mohitdedhe/Desktop/MohitsDocs/Certification and Projects/VProject/Files"
json_files=[json_file for json_file in os.listdir(json_path)if json_file.endswith('.json')]
# flag counter used to keep track of number of times the header is printed in csv file
flag=0
#looping over the json files
for every_file in tqdm(json_files):
    #global flag
    data=open(json_path+'/'+every_file,encoding='utf-8')
    jsonrecords=data.readlines()
    data.close()
    #looping over the lines in jsonrecords to find the repository name, date, hour and event
    for line in jsonrecords:
        jsonstrings=json.loads(line)
        #looping over evry repository present in the json record
        for airproject in projectAI:
            if(jsonstrings['repo']['name']==airproject):
                #looping over every event in json record
                for event in eventType:
                    if(jsonstrings['type']==event):
                        Datevalue=every_file[0:10]
                        #Hourvalue=every_file[11:12] code changes for the getting the index of the '.' before the extension
                        index= every_file.index('.')
                        Hourvalue=every_file[11:index]
                        RepNamevalue=jsonstrings['repo']['name']
                        EventNamevalue=jsonstrings['type']
                        #creates a new csv file and appends repository name, date, hour and event into csv
                        with open('finalresult.csv','a',newline='') as csvfile:
                            fieldnames = ['Date', 'Hour', 'RepName','EventName']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            if flag==0:
                                writer.writeheader()
                            writer.writerow({'Date':Datevalue, 'Hour':Hourvalue, 'RepName':RepNamevalue,'EventName':EventNamevalue})
                            flag+=1
                    
