import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/Users/mohitdedhe/Downloads/finalresult.csv')
df1=pd.pivot_table(df, index=['RepName','EventName'], values='Hour',aggfunc=len)
df1
