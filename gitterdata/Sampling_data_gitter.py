import os
import glob
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import csv
import datetime
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
#######Included Question column########
#Update the column 'questions' if ? is present in msg column
sub='\?'
big_frame['question'] = big_frame['msg'].str.contains(sub) 
big_frame['question'] = big_frame['question'].map({True: 1, False: 0})
#######End########
year_2017 = big_frame[big_frame['year'] == 2017]
#Fill the month with first day of the respective months
year_2017['month_first'] = year_2017['date'].values.astype('datetime64[M]')
month=year_2017.groupby(by=['uname','month_first'])['msg_count'].sum().copy()
uname_month=pd.DataFrame(month)
uname_indexed = uname_month.reset_index()
#This data contains the data of 5000 sample users from gitter, taken from year 2017
sampled_data = pd.read_csv("D:/GitHub/Gitter/user_name_2017_sampled_5000.csv") 
#Seggregating data for the sampled users
df1 = pd.merge(sampled_data.reset_index(), uname_indexed.reset_index(), on='uname')
df = df1.drop(columns=['index_x', 'index_y'])
#fill the missing month and their corresponding message count value as 0
df.month_first = pd.to_datetime(df.month_first)
dates = pd.date_range(datetime.datetime(df.month_first.dt.year.min(), 1, 1),datetime.datetime(df.month_first.dt.year.max(), 12, 1), freq = 'MS')
idx = pd.MultiIndex.from_product([df.uname.unique(), dates], names = ['uname','month_first'])
new_data_msgcount=df.set_index(['uname', 'month_first']).reindex(idx).fillna(0).astype(int).reset_index()
#######Included Question column########
ques=year_2017.groupby(by=['uname','month_first'])['question'].sum().copy()
uname_ques=pd.DataFrame(ques)
uname_indexed_ques = uname_ques.reset_index()
df2 = pd.merge(sampled_data.reset_index(), uname_indexed_ques.reset_index(), on='uname')
df_ques = df2.drop(columns=['index_x', 'index_y'])
df_ques.month_first = pd.to_datetime(df_ques.month_first)
dates_ques = pd.date_range(datetime.datetime(df_ques.month_first.dt.year.min(), 1, 1),datetime.datetime(df_ques.month_first.dt.year.max(), 12, 1), freq = 'MS')
idx_ques = pd.MultiIndex.from_product([df_ques.uname.unique(), dates], names = ['uname','month_first'])
new_data_ques=df_ques.set_index(['uname', 'month_first']).reindex(idx_ques).fillna(0).astype(int).reset_index()
#######End########
#Merging both the dataframes
final_df = pd.merge(new_data_msgcount, new_data_ques, on=['uname','month_first'])
#Writing (final gitter)data to final csv
final_df.to_csv('D:/GitHub/Gitter/sampled_data_2017.csv',encoding='utf-8', index=False)
