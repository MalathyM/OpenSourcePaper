#plot for number of msgs per day from gitter chatroom
import os
import glob
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
path = "D:/GitHub/GitHub/csv"
allFiles = glob.glob(os.path.join(path,"*.csv"))
np_array_list = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    np_array_list.append(df.as_matrix())
comb_np_array = np.vstack(np_array_list)
big_frame = pd.DataFrame(comb_np_array)
#assigning default value for message count as message column has string value
big_frame.columns = ["sent_time","dname","uname","msg","read_by","issues"]
big_frame['Number of messages']=1
#separating and populating the sent_time into different columns like date, year, month, day and hour
big_frame['date'] = pd.to_datetime(big_frame['sent_time']).dt.date
big_frame['year'] = pd.to_datetime(big_frame['sent_time']).dt.year
big_frame['month'] = pd.to_datetime(big_frame['sent_time']).dt.month
big_frame['day'] = pd.to_datetime(big_frame['sent_time']).dt.day
big_frame['hour'] = pd.to_datetime(big_frame['sent_time']).dt.hour
#aggregating the columns year and month to find the message count per month
month = big_frame.groupby(by=['year','month'])['Number of messages'].sum().copy()
df_m = pd.DataFrame(month)
df_month = df_m.reset_index()
df_month = df_month.set_index('month')
#plot for year 2015 and save it to PDF
df_month.loc[df_month['year'] == 2015, 'Number of messages'].plot(marker='*',color="red")
plt.legend().set_visible(False)
plt.title("Number of messages on a monthly basis")
plt.savefig('D:/GitHub/Gitter/Plots/Gitter_monthly_plot_2015.pdf')
#plot for year 2016 and save it to PDF
df_month.loc[df_month['year'] == 2016, 'Number of messages'].plot(marker='*',color="red")
plt.legend().set_visible(False)
plt.title("Number of messages on a monthly basis")
plt.savefig('D:/GitHub/Gitter/Plots/Gitter_monthly_plot_2016.pdf')
#plot for year 2015 and save it to PDF
df_month.loc[df_month['year'] == 2017, 'Number of messages'].plot(marker='*',color="red")
plt.legend().set_visible(False)
plt.title("Number of messages on a monthly basis")
plt.savefig('D:/GitHub/Gitter/Plots/Gitter_monthly_plot_2017.pdf')
