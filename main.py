



# # tut metod is stackoverflow cherez filter isalpha
# unique_words = set()
# descartes = open('files/Descartes.txt', 'r', encoding='ANSI')


# for line in descartes:
#     line = [word.lower() for word in line.split()]
#     line = [word for word in filter(str.isalpha, line)]
#     unique_words.update(line)
#
# descartes.close()
#
# print("{} unique words".format(len(unique_words)))
#
# punctuation = "?,.!"
# descartes = open('files/Descartes.txt', 'r', encoding='ANSI')
# print(descartes.split( ))


# ascend = "bob, mod, pot, rot, cod, nod"
# print(ascend.strip(","))
text ='aa, aa bb cc'

def unique_words(text):
    words = text.replace('"','').replace(',', '').split()
    unique = list(set(words))
    return len(unique)

unique_words(text)
# for letter in ascend:
#     if letter == '"' or letter in punctuation:
#         descartes = ascend.replace(letter, '')
# text = list(ascend.split())
# unique_text = ascend.strip("','?!.;")
# print(len(text))
# print(text)
#
# print(unique_text)
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