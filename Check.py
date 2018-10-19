import json
import os
import glob
json_path="C:/Users/Nameetha/Desktop/Github"
json_files=[json_file for json_file in os.listdir(json_path)if json_file.endswith('.json')]
for every_file in json_files:

		data=open(every_file)
		jsonrecords=data.readlines()
		data.close()
		for every_line in jsonrecords:
			jsonstrings=json.loads(every_line)
			checkwords=["\\"," ","You"]
			Replacewords=["","","'//You//'"]
			for check, rep in zip(checkWords, repWords)
				jsonstrings = jsonstrings.replace(check, rep)
				filtered_data=json.loads(jsonstrings)
filtered_data['Payload']
