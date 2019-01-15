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
#aggregating the columns date and day to find the message count per day
day = big_frame.groupby(by=['date','day'])['Number of messages'].sum().copy()
df_day = pd.DataFrame(day)
df_day.set_index(pd.to_datetime(df_day.index.get_level_values(0) ) +
             pd.to_timedelta(df_day.index.get_level_values(1), unit='D'),
             inplace=True)
new_idx = pd.date_range(df_day.index.min(), df_day.index.max(), freq='D')
df_day['Number of messages']=df_day.reindex(new_idx, fill_value=0)
#plot for year 2015 and saving it to PDF
df_day[df_day.index.year == 2015].plot(marker='*',color="green")
plt.legend().set_visible(False)
plt.title("Number of messages on a daily basis")
plt.savefig('D:/GitHub/Gitter/Plots/Gitter_daily_plot_2015.pdf')
#plot for year 2016 and saving it to PDF
df_day[df_day.index.year == 2016].plot(marker='*',color="green")
plt.legend().set_visible(False)
plt.title("Number of messages on a daily basis")
plt.savefig('D:/GitHub/Gitter/Plots/Gitter_daily_plot_2016.pdf')
#plot for year 2017 and saving it to PDF
df_day[df_day.index.year == 2017].plot(marker='*',color="green")
plt.legend().set_visible(False)
plt.title("Number of messages on a daily basis")
plt.savefig('D:/GitHub/Gitter/Plots/Gitter_daily_plot_2017.pdf')
