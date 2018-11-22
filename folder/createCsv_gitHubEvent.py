import json
import os
import glob
import csv
import os
import xlwt
import sys
# this is to get the path variable from the path.py file
import path
projectAI=['keras-team/keras','accord-net/framework','scikit-learn/scikit-learn','Microsoft/CNTK','Reference-LAPACK/lapack-release'
        ,'BVLC/caffe','Theano/Theano','torch/torch7']
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
Workbook=xlwt.Workbook()
i=0
c=2
col=0
row=1
worksheet=Workbook.add_sheet('sheet 1')
worksheet.write(0,0,'Date')
worksheet.write(0,1,'Hour')
worksheet.write(0,2,'RepName')
worksheet.write(0,3,'Event Name')
Workbook.save('Data2.xls')
processed_files=0
for every_file in json_files:
    processed_files=+1
    print(str(processed_files*100/len(json_files)))
    print(json_path+'/'+every_file)
    data=open(json_path+'/'+every_file)
    jsonrecords=data.readlines()
    data.close()
    for line in jsonrecords:
        jsonstrings=json.loads(line)
        for airproject in projectAI:
            if(jsonstrings['repo']['name']==airproject):
                for event in eventType:
                    eve=jsonstrings['type']
                    if(jsonstrings['type']==event):
                        if(i>0):
                            row=row+1
                            col=0
                        worksheet.write(row,col,every_file[0:10])
                        worksheet.write(row,col+1,every_file[11:13])
                        worksheet.write(row,col+2,jsonstrings['repo']['name'])
                        worksheet.write(row,col+3,eve)
                        i=1
Workbook.save('Data2.xls')
