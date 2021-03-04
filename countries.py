import csv

def sort_value(some_list):
    return(sorted(some_list, key=lambda x: x[2], reverse= True))
data_list=[]
with open('countries.csv', 'r', encoding= "UTF8") as csv_file:
    next(csv_file)
    csv_reader= csv.DictReader(csv_file)
    for line in csv_reader:
        data_list.append(line)




result_list=[]
top_string=''
top_list = []
for x in data_list:
    top_list.appenxd(x['GDP per capita'])
while len result
def square(x):
    result=x*x
    return result

square2 = lambda x: x*x
print(square2(5))

print(type(square2))
print(type(square))