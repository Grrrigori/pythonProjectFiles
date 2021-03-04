import pandas as pd

df= pd.read_csv('2019.csv', skiprows = 1)

# people={
#     'first':['Roman', 'Bob','John'],
#     'second':['Kutselpea', 'Norton', 'Ivanov'],
#     'email':['roman@xmaple.ee','gregoryest@gmail.com', 'kolya@vasya.ee']
# }
# df = pd.DataFrame(people)
# print(df['email'])
# print(df.email)
# # dva odinakovih pochti sposoba
#
#
# for x in df['email']:
#
#     print(x)

# print(df.iloc[[0, 5, 10,],[7,2,5]])
# print(df.loc[[0, 5, 10,],['Country or region']])
# iloc dlja integerov loc dlja po nazvanijam

# print(df.shape[[0, 1, 3, 6],[3, 6]])
# shape nepravilno zapisal
# print(df['Country or region'].value_counts())
# print(df[['Score', 'Country or region']].value_counts(ascending =True))

# print(df.loc[0:16],['Country or region':'Freedom to make live choices'])
# opjat oshibka kakaja to

df.to_csv('2019new.csv', index= False)
# mozhno header=true/false, columns = 'nazvanie teh stolbcov kotorie nam nuzhni'
print(df.columns)
for titles in df.columns:
    print(titles)
