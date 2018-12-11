import glob
import pandas as pd
import os
path = r'D:\Data\Github\csv'                     
all_files = glob.glob(os.path.join(path, "*.csv")) 
df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
#len(concatenated_df['UserName'].unique().tolist())
print((concatenated_df['UserName'].unique().tolist()))
