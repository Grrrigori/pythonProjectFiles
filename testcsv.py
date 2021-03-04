import csv

with open('test.csv', 'r', encoding="UTF8") as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)

    next(csv_reader)

    for line in csv_reader:
        # print(line)
        print(line[0])
with open('test.csv', 'r') as csv_file
    csv_reader= csv.reader(csv_file)


    with open('test_copy.csv','w') as new_file:
        csv_writer = csv.writer(new_file, delimeter='-', linetermination='\n')
