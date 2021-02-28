import collections

import requests
from bs4 import BeautifulSoup

# a = ArticleList('http://feeds.bbci.co.uk/news/rss.xml')


class Article:
    def __init__(self, article_xml):
        self.title = article_xml.title.string
        self.description = article_xml.description.string
        self.link = article_xml.guid.string

url = 'http://feeds.bbci.co.uk/news/rss.xml'

page = requests.get(url)
article_summary = []

for article_xml in BeautifulSoup(page.content, 'html.parser').find_all('item'):
    article_summary.append(Article(article_xml))


