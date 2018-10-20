import json
path = 'C:/Users/Malathy/Desktop/Data'
json_files = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]
print(json_files)
for file in json_files:
    fp=open(path+"/"+file,encoding='utf-8')
    data=fp.readlines()
    fp.close()
    for line in data:
        data_lines = json.loads(line)
        if(data_lines['repo']['name'] == "jmoon018/rshell-unit-tester"):
              print(data_lines['created_at'])
