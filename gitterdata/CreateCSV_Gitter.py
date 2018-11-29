import json
import os
import glob
import csv
import os
import xlwt
jsonNlist=[]
#json_path="D:/GitHub/GitHub/Data/Gitter"
json_path="D:/GitHub/GitHub/Data/Gitter_2"
json_files=[json_file for json_file in os.listdir(json_path)if json_file.endswith('.json')]
flag=0
for file in json_files:
    with open(json_path+"/"+file,'r',encoding='utf-8') as infile:
        records = json.load(infile)
        print(records[1])
        print(type(records))
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
                    with open('D:/GitHub/data.csv','a',encoding='utf-8',newline='') as csvfile:
                        fieldnames = ['Sent_Time','Display_Name','UserName','Messages','ReadBy','Issues']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        if flag==0:
                            writer.writeheader()
                        writer.writerow({'Sent_Time':sent_value, 'Display_Name':disp, 'UserName':usrname, 'Messages':msg_value, 'ReadBy':ReadBy_value, 'Issues':Issues_value})
                        flag =+1
            except:
                pass
