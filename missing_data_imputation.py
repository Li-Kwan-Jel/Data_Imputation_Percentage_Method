#This module if the percentage of missing values is above 80%
#it will remove it else it will replace the values

import pandas as pd
df = pd.read_csv("convertcsv.csv")
#total = df.isnull().sum()
#drop = df.dropna(axis=1 , thresh = 2)


df = df.loc[:,df.isnull().mean() < .9]
df=df.fillna("OK")
#above fill NaN values
#test the percentage of missing values , if over then remove from column
print (df.head())

