#Give the file Path
file=open('/Users/mohitdedhe/Desktop/MohitsDocs/Certification and Projects/VProject/Files/2015-01-07-11.json',encoding='utf-8')
#Read the contain of the file
data= file.read()
#dump the data into json
records=json.dumps(data)
#load the string data into Json 
records1=json.loads(records)
#refine the data according to get the desired results
records1=records1.replace("\\","")
records1=records1.replace(" ","")
#get the type of the data 
type(records1)
#Need to get it because to get the proper json for single ID
rec=records1[0:16665]
# need to do this because of the character wasn't follow the json rule
rec=rec.replace('"You"',"'//You//'")
#Now refine data load into the Json and create the key value pair 
d = json.loads(rec)
#get the value for payload
d['payload']
