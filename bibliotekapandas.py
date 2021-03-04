import pandas as pd

# import json
# with open('sample2.json', 'r', encoding='UTF8') as file:
#     data=json.load(file)
#
#
# df = pd.DataFrame(data['people'])
# print(df)
# print(type(df))

df= pd.read_csv('2019.csv', skiprows = 1)
#  mozhno bilo header ispolzovat nrows names

pd.set_option('display.max_columns', 9)
pd.set_option('display.max_rows',157)

print(df[['Score', 'Country or Region']].value.counts(ascending =True))