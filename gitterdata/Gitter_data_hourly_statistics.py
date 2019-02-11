import os
import glob
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
path = "D:/GitHub/Gitter/Chats/csv"
allFiles = glob.glob(os.path.join(path,"*.csv"))
np_array_list = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    np_array_list.append(df.as_matrix())
comb_np_array = np.vstack(np_array_list)
big_frame = pd.DataFrame(comb_np_array)
big_frame.columns = ["sent_time","dname","uname","msg","read_by","issues"]
big_frame['msg_count']=1
big_frame['date'] = pd.to_datetime(big_frame['sent_time']).dt.date
big_frame['year'] = pd.to_datetime(big_frame['sent_time']).dt.year
big_frame['month'] = pd.to_datetime(big_frame['sent_time']).dt.month
big_frame['day'] = pd.to_datetime(big_frame['sent_time']).dt.day
big_frame['hour'] = pd.to_datetime(big_frame['sent_time']).dt.hour
t = big_frame.groupby(by=['date','hour'])['msg_count'].sum().copy()
df = pd.DataFrame(t)
df.set_index(pd.to_datetime(df.index.get_level_values(0) ) +
             pd.to_timedelta(df.index.get_level_values(1), unit='H'),
             inplace=True)
new_idx = pd.date_range(df.index.min(), df.index.max(), freq='H')
df['msg_count']=df.reindex(new_idx, fill_value=0)
df_2015_hourly = df[df.index.year == 2015]

#find minimum value of msg_count for year 2015
df_2015_hourly['msg_count'].min()
#find minimum value of msg_count for year 2015
df_2015_hourly['msg_count'].max()
#find mean of msg_count for year 2015
df_2015_hourly['msg_count'].mean()
#find standard deviation of msg_count for year 2015
df_2015_hourly['msg_count'].std()
