punctuation = "?,.!"



# with open('files/Descartes.txt', 'r', encoding='ANSI') as file:
#     file_content = file.read()
#     print(len(file_content))
#     # print(set(file_content))
#     print(len(set(file_content)))
#     # file_ammount = [line.split(',')for line in file_content]
#     # print (file_ammount)
# text = str(file_content)
# unique_text = text.strip("','?!.;")
# print(len(set(unique_text.split())))
# print(unique_text)


with open('files/Descartes.txt', 'r', encoding='ANSI') as file:
    file_content = file.read()
    print(len(file_content))
    # print(set(file_content))
    print(len(set(file_content)))
    # file_ammount = [line.split(',')for line in file_content]
    # print (file_ammount)
text = str(file_content)
unique_text = text.replace(',', '').replace('!', '').replace('.', '').replace('«','').replace('»','')
lowertext = unique_text.lower()
print(len(set(lowertext.split())))
print(lowertext)


#
# text_punct_removed = raw_text.replace(".", "")
# text_punct_removed = raw_text.replace("!", "")
# print("\ntext with punctuation characters removed:\n", text_punct_removed)






# print(file_content.split( ))
# print(len(set(file_content.split())))
unique_words = set(file_content.split())
# print(unique_words)



# for letter in descartes:
#     if letter == '"' or letter in punctuation:
#         descartes = descartes.replace(letter, '')
# text= set(descartes.split( ))
# print(len(text))


#
# with open('files/Descartes.txt', 'r', encoding='ANSI') as file:
#     file_content = file.read()
#     print(len(file_content))
#     # print(set(file_content))
#     # print(len(set(file_content)))
#     file_ammount= [line.split(',')for line in file_content]
#     print (file_ammount)



#
# ascend = "bob, mod, pot, rot, cod, nod"
# for letter in ascend:
#     if letter == '"' or letter in punctuation:
#         descartes = ascend.replace(letter, '')
# text= set(ascend.split( ))
# print(len(text))
#
# print (ascend.split( ))