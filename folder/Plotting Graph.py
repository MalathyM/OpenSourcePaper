#Plots the graph for different events in a file for the given month
import pandas as pd
from matplotlib import pyplot as plt
import datetime
import matplotlib.dates as mdates
jsonNlist=[]
#Select the path to read the csv file
if(len(sys.argv)<2):
    print("Error: .py <parameter> 1. Mohit 2. Vivek's server 3. Arundathi's server 4. Malathy's server 5. Nameetha's server")

if(sys.argv[1]=='1'):
    path=path.Json_Mohit
elif (sys.argv[1]=='2'):
    path=path.Json_Vivek
elif (sys.argv[2]=='3'):
    path=path.Json_Arundathi
elif (sys.argv[3]=='4'):
    path=path.Json_Malathy
elif (sys.argv[4]=='5'):
    path=path.Json_Nameetha
else:
    print('Provide correct parameter')
#read the selected path 
Githubdataframe1=pd.read_csv(path,header=0)
unique_event=Githubdataframe1['EventName'].unique().tolist()
unique_eventList=Githubdataframe1.EventName.unique().tolist()
for event in unique_eventList:
    if(event=='EventName'):
        unique_eventList.remove(event)
from matplotlib.backends.backend_pdf import PdfPages
figure_var=plt.figure()
#creating a list of markers to iteratee while plotting
markers_array=['+',
 '*',
 'o',
 'v',
 '^',
 '<',
 '>',
 'x',
 'D',
 'd',
 '|',
 '_',
        ]
#iterate over unique eveents in a list to plot the graph
for eventtype in unique_eventList:
    event=Githubdataframe1[ Githubdataframe1.EventName.isin([eventtype] )]
    columns=['Date','RepName']
    test = pd.DataFrame( columns=columns)
    test['Date']=event['Date']
    test['RepName']=event['RepName']
    unique_repositories=test.RepName.unique()
    marker_counter=0
    fig,ax=plt.subplots()
    #iterate over unique repositories which contains the above event
    for repo in unique_repositories:
        data_filtered_for_one_repository=test[test['RepName']==repo]
        # add a new column 'value' which is '1' for all rows. This will help us to aggreagte
        #values. This might throw a warning, but just ignore it.
        data_filtered_for_one_repository['value']=1
        data_groupe_by_date_for_one_repo=data_filtered_for_one_repository.groupby(['Date'])['value'].sum()
        tmp=pd.DataFrame()
        #strips the data into month,day and year format for every date in data_filtered_for_one_repository dataframe and saves it in tm dataframe
        tmp['Date']= [datetime.datetime.strptime(x,'%m/%d/%Y') for x in data_groupe_by_date_for_one_repo.index.values] 
        #saves the number of events occured on that date
        tmp['number_of_events']= data_groupe_by_date_for_one_repo.values
        start = datetime.datetime.strptime("01-01-2015", "%d-%m-%Y")
        end = datetime.datetime.strptime("01-02-2015", "%d-%m-%Y")
        date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        #setting the values to be displayed on x axis
        ax.set_xlim(datetime.date(2015,1,1),datetime.date(2015,1,30))
        #plt.locator_params(numticks=5)
        xfmt = mdates.DateFormatter('%Y-%m-%d')
        ax.xaxis.set_major_formatter(xfmt)
        ax.set_xticks([datetime.date(2015,1,1),datetime.date(2015,1,15),datetime.date(2015,1,30)])
        ax.plot(tmp.Date,tmp.number_of_events,markers_array[marker_counter], label=repo)
        #fig=plt.gcf()
        marker_counter+=1
    plt.legend()
    plt.savefig(eventtype+'.pdf')

