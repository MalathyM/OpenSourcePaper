import numpy as np
import pandas as pd
git_hub = pd.read_csv("D:/GitHub/Gitter/githubGittercollection.csv")
gitter=pd.read_csv("D:/GitHub/Gitter/sampled_data_2017.csv")
df=pd.merge(git_hub, gitter, how='inner', left_on=['UserID','Month'], right_on=['UserID','Month'])
df.to_csv("D:/GitHub/Gitter/Final_github_gitter_panel.csv")
