#Plots the graph for different events in a file for the given month
import io
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd
dataframe=pd.read_csv("/Users/mohitdedhe/Downloads/finalresult.csv")
ForkEvent=dataframe[ dataframe.EventName.isin(['ForkEvent'] )]
columns=['Date','RepName']
test = pd.DataFrame( columns=columns)
test['Date']=ForkEvent['Date']
test['RepName']=ForkEvent['RepName']
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
