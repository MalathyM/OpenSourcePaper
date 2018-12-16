#plot for number of msgs per hour from gitter chatroom
import os
import glob
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
path = "D:\GitHub\GitHub\csv"
allFiles = glob.glob(os.path.join(path,"*.csv"))
np_array_list = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    np_array_list.append(df.as_matrix())
comb_np_array = np.vstack(np_array_list)
big_frame = pd.DataFrame(comb_np_array)
#assigning default value for message count as message column has string value
big_frame['msg_count']=1
big_frame.columns = ["sent_time","dname","uname","msg","read_by","issues"]
#separating and populating the sent_time into different columns like date, year, month, day and hour
big_frame['date'] = pd.to_datetime(big_frame['sent_time']).dt.date
big_frame['year'] = pd.to_datetime(big_frame['sent_time']).dt.year
big_frame['month'] = pd.to_datetime(big_frame['sent_time']).dt.month
big_frame['day'] = pd.to_datetime(big_frame['sent_time']).dt.day
big_frame['hour'] = pd.to_datetime(big_frame['sent_time']).dt.hour
#aggregating the columns date and hour to find the message count per hour
t = big_frame.groupby(by=['dt','hr'])['msg_count'].sum().copy()
df = pd.DataFrame(t)
#filling the hour gaps as few hours had 0 message count
df.set_index(pd.to_datetime(df.index.get_level_values(0) ) +
             pd.to_timedelta(df.index.get_level_values(1), unit='H'),
             inplace=True)
new_idx = pd.date_range(df.index.min(), df.index.max(), freq='H')
df['msg_count']=df.reindex(new_idx, fill_value=0)
#plotting the data for year 2015
df[df.index.year == 2015].plot()
