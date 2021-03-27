import string

word = "'''12312'^£!@£$^"
# a = word.strip(punctuation).strip(punctuation)

# print(a)

# temp_list = ["‘unstinting", "support’"]

# for i in temp_list:
#     translator = str.maketrans('', '', i.punctuation)
#     word = i.translate(translator)
#     print(word)
#     # word = clean.append(w)


a = "‘unstinting"


translator = str.maketrans('', '', string.punctuation+'‘')

# s = 'string with "punctuation" inside of it! Does this work? I hope so.'

print(a.translate(translator))
