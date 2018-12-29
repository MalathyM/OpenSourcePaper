#Plots the graph for different events in a file for the given month
import io
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd
jsonNlist=[]

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
dataframe=pd.read_csv(path)
ForkEvent=dataframe[ dataframe.EventName.isin(['ForkEvent'] )]
columns=['Date','RepName']
test = pd.DataFrame( columns=columns)
test['Date']=ForkEvent['Date']
test['RepName']=ForkEvent['RepName']
test['Date']=pd.DatetimeIndex(test['Date']).normalize()
forkPlot = (test.reset_index()
          .groupby(['Date','RepName'], as_index=False)
          .count()
          
          .rename(columns={'index':'count'})
       )
from matplotlib import pyplot as plt
fig, ax = plt.subplots()
fig.set_size_inches(22, 15, forward=True)
# key gives the group name (i.e. RepName), data gives the actual values
for key, data in forkPlot.groupby('RepName'):
    data.plot(x='Date', y='count', ax=ax, label=key)
plt.savefig("C://Users/Nameetha/Desktop/GithubResults.pdf")
