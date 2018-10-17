import json
fp=open('/Users/mohitdedhe/Desktop/MohitsDocs/Certification and Projects/VProject/Files/2015-01-07-11.json')
datam=fp.readlines()
fp.close()

for line in datam:
    data=json.loads(line)
