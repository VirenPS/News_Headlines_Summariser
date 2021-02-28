# import collections
# import string

# import requests
# from bs4 import BeautifulSoup

# URL = r'https://www.thefreedictionary.com/List-of-pronouns.htm#:~:text=Pronouns%20are%20classified%20as%20personal,%2C%20yours%2C%20his%2C%20hers%2C'

# page = requests.get(URL)
# pronoun_list = []
# for pronoun in BeautifulSoup(page.content, 'html.parser').find_all('li'):
#     # pronoun_list.append(pronoun)
#     print(pronoun.string)

excluded_words_list_duplicates = []

pronouns = ['I', 'i' 'we', 'he', 'she', 'it', 'they', 'me', 'us', 'you', 'her', 'him', 'it', 'them', 'mine', 'ours', 'yours', 'hers', 'his', 'theirs', 'my', 'our', 'your', 'her', 'his', 'their', 'myself', 'yourself', 'herself', 'himself', 'itself', 'ourselves', 'yourselves', 'themselves', 'myself', 'yourself', 'herself', 'himself', 'itself', 'ourselves', 'yourselves', 'themselves', 'all', 'another', 'any', 'anybody', 'anyone', 'anything', 'both', 'each', 'either', 'everybody', 'everyone', 'everything', 'few', 'many', 'most', 'neither', 'nobody', 'none', 'no', 'one', 'nothing', 'one', 'other', 'others', 'several', 'some', 'somebody', 'someone', 'something', 'such', 'such', 'that', 'these', 'this', 'those', 'what', 'whatever', 'which', 'whichever', 'who', 'whoever', 'whom', 'whomever', 'whose', 'as', 'that', 'what', 'whatever', 'which', 'whichever', 'who', 'whoever', 'whom', 'whomever', 'whose', 'thou', 'thee', 'thy', 'thine', 'ye', 'all', 'another', 'any', 'anybody', 'anyone', 'anything', 'as', 'aught', 'both', 'each', 'each', 'other', 'either', 'enough', 'everybody', 'everyone', 'everything', 'few', 'he', 'her', 'hers', 'herself', 'him', 'himself', 'his', 'I', 'idem', 'it', 'its', 'itself', 'many', 'me', 'mine', 'most', 'my', 'myself', 'naught', 'neither', 'no', 'one', 'nobody', 'none', 'nothing', 'nought', 'one', 'one', 'another', 'other', 'others', 'ought', 'our', 'ours', 'ourself', 'ourselves', 'several', 'she', 'some', 'somebody', 'someone', 'something', 'somewhat', 'such', 'suchlike', 'that', 'thee', 'their', 'theirs', 'theirself', 'theirselves', 'them', 'themself', 'themselves', 'there', 'these', 'they', 'thine', 'this', 'those', 'thou', 'thy', 'thyself', 'us', 'we', 'what', 'whatever', 'whatnot', 'whatsoever', 'whence', 'where', 'whereby', 'wherefrom', 'wherein', 'whereinto', 'whereof', 'whereon', 'wherever', 'wheresoever', 'whereto', 'whereunto', 'wherewith', 'wherewithal', 'whether', 'which', 'whichever', 'whichsoever', 'who', 'whoever', 'whom', 'whomever', 'whomso', 'whomsoever', 'whose', 'whosever', 'whosesoever', 'whoso', 'whosoever', 'ye', 'yon', 'yonder', 'you', 'your', 'yours', 'yourself', 'yourselves']
excluded_words_list_duplicates += pronouns

preposition = ['aboard', 'about', 'above', 'across', 'after', 'against', 'along', 'amid', 'among', 'anti', 'around', 'as', 'at', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between', 'beyond', 'but', 'by', 'concerning', 'considering', 'despite', 'down', 'during', 'except', 'excepting', 'excluding', 'following', 'for', 'from', 'in', 'inside', 'into', 'like', 'minus', 'near', 'of', 'off', 'on', 'onto', 'opposite', 'outside', 'over', 'past', 'per', 'plus', 'regarding', 'round', 'save', 'since', 'than', 'through', 'to', 'toward', 'towards', 'under', 'underneath', 'unlike', 'until', 'up', 'upon', 'versus', 'via', 'with', 'within', 'without']
excluded_words_list_duplicates += preposition

determiners = ['the', 'a', 'an', 'this', 'that', 'these', 'those', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'few', 'a', 'little', 'much', 'many', 'lot', 'most', 'some', 'any', 'enough', 'one', 'ten', 'thirty', 'all', 'both', 'half', 'either', 'neither', 'each', 'every', 'other', 'another', 'such', 'what', 'rather', 'quite']
excluded_words_list_duplicates  += determiners

conjunctions = ['for', 'not', 'and', 'but', 'yet', 'so', 'nor', 'after', 'until', 'before', 'since', 'because', 'as', 'though', 'although', 'whereas', 'while', 'either', 'or', 'neither', 'nor', 'both', 'and', 'not', 'but', 'whether', 'or', 'just', 'as', 'so', 'the', 'as', 'much', 'sooner', 'than', 'rather', 'than', 'no']
excluded_words_list_duplicates  += conjunctions

others = ['have', 'a', 'will']
excluded_words_list_duplicates  += others

excluded_words_list = list(set(excluded_words_list_duplicates))

