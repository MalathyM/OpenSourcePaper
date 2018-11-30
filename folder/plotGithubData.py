import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('/Users/mohitdedhe/Downloads/finalresult.csv')
df1=pd.pivot_table(df, index=['RepName','EventName'], values='Hour',aggfunc=len)

#Change the string value to int

dfFinal['Hour'] = pd.to_numeric(dfFinal['Hour'])
#Plotting the Cube plot 
plots1 = dfFinal.pivot('EventName', 'RepName', 'Hour')
f, ax = plt.subplots(figsize=(10, 9))
sns.heatmap(plots1, annot=True,  linewidths=.5, ax=ax)
plt.show()
