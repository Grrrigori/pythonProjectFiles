import pandas as pd
import csv

df = pd.read_csv('2019.csv',  index_col= 'Social support', nrows = 11, header=1)
df = df.sort_values(by ='Social support', ascending= False)
# df= df.sort_values(by = 'Overall rank', ascending= True)
pd.set_option('display.max_columns', 9)
pd.set_option('display.max_rows', 157)


print(df.sort_index())

print(df[df['GDP per capita']>1])
print(df.head(15))
print(df.tail(15))

