import numpy as np
import pandas as pd
import os

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

#create OS path
os.path.join('C:/', 'Users/', '17605/', 'Downloads/', 'california.xls')

#read in the data
data = pd.read_excel(os.path.join('C:/', 'Users/', '17605/', 'Downloads/', 'california.xls'), header=4)

#data information
data.info()

#clean up column names by removing the \n charater
data.columns = [x.replace("\n", " ") for x in data.columns.to_list()]

# Min-Max Normalization
df = data.drop('City', axis=1)
df_norm = (df-df.min())/(df.max()-df.min())
df_norm = pd.concat((data.City, df_norm), 1)
del df