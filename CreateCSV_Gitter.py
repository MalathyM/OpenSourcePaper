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
Workbook=xlwt.Workbook()
i=0
c=2
col=0
row=1
worksheet=Workbook.add_sheet('sheet')
worksheet.write(0,0,'Sent_Time')
worksheet.write(0,1,'Display_Name')
worksheet.write(0,2,'UserName')
worksheet.write(0,3,'Text')
worksheet.write(0,4,'ReadBy')
worksheet.write(0,5,'Issues')
Workbook.save('D:/Gitter_Data.xls')
for file in json_files[1:2]:
    with open(json_path+"/"+file,'r',encoding='utf-8') as infile:
        records = json.load(infile)
        col=0
        worksheet.write(row,col,records[i]['sent'])
        worksheet.write(row,col+1,records[i]['fromUser']['displayName'])
        worksheet.write(row,col+2,records[i]['fromUser']['username'])
        worksheet.write(row,col+3,records[i]['text'])
        worksheet.write(row,col+4,records[i]['readBy'])
        worksheet.write(row,col+5,records[i]['issues'])
        row=row+1
        i=1
Workbook.save('D:/Gitter_Data.xls')
