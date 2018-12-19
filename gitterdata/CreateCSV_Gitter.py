import json
import os
import glob
import csv
import xlwt
#json_path="D:/GitHub/GitHub/Data/Gitter"
json_path="D:/GitHub/Chats"
json_files=[json_file for json_file in os.listdir(json_path)if json_file.endswith('.json')]
flag=0
fileCount=0
logf = open("D:/GitHub/Chats/csv/err.log", "a")
for file in json_files:
    with open(json_path+"/"+file,'r',encoding='utf-8') as infile:
        records = json.load(infile)
        #print(type(records))
        #print(len(records))
        fileCount += 1
        with open('D:/GitHub/Chats/csv/'+'data_'+str(fileCount)+'.csv','w',encoding='utf-8',newline='') as csvfile:
            fieldnames = ['Sent_Time','Display_Name','UserName','Messages','ReadBy','Issues']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(records)):
                #used try and except block to catch exception - some files doesn't have the tags displayName available
                try:
                    if records[i]['sent'] is not None and records[i]['fromUser']['displayName'] is not None:
                        sent_value=records[i]['sent']
                        disp=records[i]['fromUser']['displayName']
                        usrname=records[i]['fromUser']['username']
                        msg_value=records[i]['text']
                        ReadBy_value=records[i]['readBy']
                        Issues_value=records[i]['issues']
                        writer.writerow({'Sent_Time':sent_value, 'Display_Name':disp, 'UserName':usrname, 'Messages':msg_value, 'ReadBy':ReadBy_value, 'Issues':Issues_value})
                except:
                    logf.write(str(records[i]))
                    pass
