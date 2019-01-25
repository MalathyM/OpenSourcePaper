#creating the dictionary to store the unique ids and there eventcounts
arr=dict()
#this will have the event names and its counts for the perticular userid
arr_evnt_count=dict{}
#data looks {moht:{even1:4,event2:5, event4:5}}
#i is used for the first iteration of the dictionary insert key and value pair
i=0
#getting the files list from the given path
json_files=[json_file for json_file in os.listdir(json_path)if json_file.endswith('.json')]
#iterating the files using For loop
for every_file in json_files:
    data=open(json_path+'/'+every_file)
    #reading the data and store it to the jsonrecord for the signle file
    jsonrecords=data.readlines()
    data.close()
    #iteration over the data line by line and loading to the json form
    for line in jsonrecords:
        jsonstrings=js.loads(line)
        #use unique Gitter UserID and now comparing the Gitter with Github login.
        for userid in arrdataUserID:
            if(jsonstrings['actor']['login']==userid):
                #first iteration of loop and adding first element directly to dictionary
                if(i==0):
                    for(evnt:eventType ):
                        arr_evnt_count.update({evnt:1})
                        arr.update({userid:arr_evnt_count})
                        i=1
                else:
                    #from the next iteration checking whether the userid already present or not
                    for key in list(arr):
                            if(key==userid):
                         #need to write the code to check whether the event is already there or not 
                            k=arr.get(key)+1
                            arr.update({userid:k})
                            k=0
                        else:
                            arr.update({userid:1})
    
