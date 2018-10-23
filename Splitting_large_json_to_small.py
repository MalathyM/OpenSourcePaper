import json,os
path = "D:/GitHub/GitHub/Data/Gitter"
json_files = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]
print(json_files)
for file in json_files:
    with open(path+"/"+file,'r',encoding='utf-8') as infile:
        o = json.load(infile)
        print(file)
    print(len(o))
    chunkSize = 15000
    for i in range(0, len(o), chunkSize):
        with open(path+"/"+ 'new_' + str(i//chunkSize) + '.json', 'w') as outfile:
            json.dump(o[i:i+chunkSize], outfile)
