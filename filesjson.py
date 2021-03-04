import json
# json_string ='''
# {
#   "people": [
#     {
#       "name": "Jack Sumers",
#       "phone": "555-555-555",
#       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
#       "has_licence": false
#     },
#     {
#       "name": "Mary Smith",
#       "phone": "777-777-777",
#       "emails": null,
#       "has_licence": true
#     }
#   ]
# }'''
#
# data =json.loads(json_string)
#
# # print(type(data['people']))
# # print(data['people'])
# # print(type(data))
# # print(data)
# # for person in data['people']:
# #     # print(person)
# #     print(person['emails'][0])
#
# people =data['people'][1]
# print (people['name']), people['phone']
# print(people)
#
# for person in data['people']:
#     del person['phone']
#     print(person)
#
#
# new_string = json.dumps(data, indent=2, sort_kesy=True)

with open('sample2.json', 'r', encoding = 'UTF8') as file:
    data = json.load(file)
    print(data)

for person in data ['people']:
    if person['has_licence'] == False:
        del person['has_licence']


with open('sample_edited.json', 'w') as file:
        json.dump(data, file, indent=2)