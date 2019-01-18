import os
import glob
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import csv
path = "D:/GitHub/GitHub/csv"
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
#filter the data for year 2017
year_2017 = big_frame[big_frame['year'] == 2017]
#create empty array
uname_2017 = []
uname_2017 = (year_2017['uname'].unique())
#convert array to df for easy writing to csv
df=pd.DataFrame(uname_2017)
df.columns=['user_name']
#write the data frame to csv
df.to_csv('D:/GitHub/GitHub/uname/user_name_2017.csv',encoding='utf-8', index=False)
#find the total number of unique user names
df.count()
#find the total number of messages in the year 2017
year_2017.groupby(by=['year'])['msg_count'].sum()
