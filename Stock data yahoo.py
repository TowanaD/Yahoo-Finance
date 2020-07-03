import datetime as dt #date module
import matplotlib.pyplot as plt      #graphing
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web  #pulls data

#graph style from matplotlib
style.use('seaborn')

# set date interval for data, shows daily data
start=dt.datetime(2020,1,1)
end=dt.datetime(2020,7,3)

#df means dataframe/spreadsheet
df=web.DataReader('PLUG','yahoo',start,end)

#tail() prints last 5 data rows by default, vice versa for head()
print(df[['Open','High']].head())
# #shows graph
df[['Open','High']].head().plot()
# #need this to show to graph if you're not using an interactive text editor(i.e. Sublime)
plt.show() 
