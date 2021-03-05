import pandas as pd

df = pd.read_csv('countries.csv', header = 1)
pd.set_option("display.max_columns", 9)
pd.set_option('display.max_rows', 156)
for titles in df:
    print(titles)
 # printed 'Country or region' title which I don't need
user_input = input('type the name  of the category from the list above(exactly as presented):')
user_input2 = input('type the amount of results You want to see(starting from the top):')
df2=df[['Country or region', user_input]]
df2=df2.sort_values(by=user_input,ascending=False)
df2=df2.reset_index(drop=True)
print(df2.loc[0:int(user_input2)-1])








#
#
# df3=(df2.loc[0:int(user_input2)-1], [user_input])
# df3[[user_input]]