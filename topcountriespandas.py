import pandas as pd

df = pd.read_csv('countries.csv', header = 1)
pd.set_option("display.max_columns", 9)
pd.set_option('display.max_rows', 156)
for titles in df:
    print(titles)
 # printed 'Country or region' title which I don't need
user_input = input('type the name  of the category from the list above(exactly as presented):')
user_input2 = input('type the amount of results You want to see(starting from the top):')
df2 = df.sort_values(by=user_input, ascending=False,)
df2 = df2.reset_index(drop=True,)

print(df2.loc[0:int(user_input2)-1], [user_input]) #- 1 potomu chto indexacija nachinaetsja s 0


# df2.to_csv('csv_files//new_noindex.csv', index=False) #popitka zapisat fail s rezultatom


# df2=(df2.loc[0:int(user_input2)-1], [user_input])#pochemy to ne rabotaet
# print(df2) #- 1 potomu chto indexacija nachinaetsja s 0
# df2.to_csv('files//results//new_noindex.csv', index=False)

# print(df2)



# for c in df.columns:
#     d=(c.split('\n'))
#     print(d.remove('Country or region'))
# #     popitka udalit Country or region ne udalos


# ne ponjatno kak sdelat tak chto bi otobrazhalsja odin column a ne vse i/ili hotja bi chtobi vse razom so scrllom vpravo a ne odin nad drugim
# ne ponjatno pro dvojnie kvadratnie skobki i iloc loc
# ne ponjatno kak ispolzovat commandu index_col= chto bi vistroit po zadannamu polzovatelem parametru
# df = pd.read_csv('2019.csv',  index_col= 'Social support'/user_input, nrows = 11, header=1)
# bil kakoj-to prostoj metod ubrat ciferki indeksi sleva

