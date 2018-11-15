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

import json
import os
import glob
import csv
import os
import xlwt
jsonNlist=[]
json_path="/Users/mohitdedhe/Desktop/MohitsDocs/Certification and Projects/VProject/Files"
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
for every_file in json_files:
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
