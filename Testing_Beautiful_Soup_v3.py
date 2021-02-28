import collections
import string

import requests

from bs4 import BeautifulSoup
from Excluded_words_list import excluded_words_list


class Article:
    def __init__(self, article_xml):
        self.title = article_xml.title.string
        self.description = article_xml.description.string
        self.link = article_xml.guid.string


class NewsSite:
    def __init__(self, name, URL):
        self.name = name
        self.URL = URL


def article_list(URL):
    page = requests.get(URL)
    articles_list = []
    for article_xml in BeautifulSoup(page.content, 'html.parser').find_all('item'):
        articles_list.append(Article(article_xml))
    return articles_list



def articles_html_generator(name, URL, top_n_articles):

    # Extracts top 10
    top_n_articles = article_list(URL)[:top_n_articles]

    # Create article_body html template
    article_body = f'<p><b><u>{name}</u></b>'
    for article in top_n_articles:
        article_body += f'''<p>
        <a href='{article.link}'>{article.title}</a>
        <br>{article.description}
        </p>'''
    article_body += '</p>'

    return article_body

def title_keyword_summariser_html(news_sites_list, excluded_words_list, top_n_results):
    article_titles = []
    for news_site in news_sites_list:
        article_list_news = article_list(news_site.URL)
        for i in article_list_news:
            article_titles.append(i.title)

    article_title_keywords = []

    for title in article_titles:
        a = title.split()
        for word in a:
            translator = str.maketrans('', '', string.punctuation + '‘' + '’')
            article_title_keywords.append(word.translate(translator).lower())


    keyword_counter = collections.Counter(article_title_keywords).most_common()
    refined_keywords_list = [i for i in keyword_counter if i[0] not in excluded_words_list]

    keyword_html_summary_table = '''<table style="width: 106px;" border="1" cellpadding="4">
    <tbody>'''

    for keyword in refined_keywords_list[0:top_n_results]:
        keyword_html_summary_table += f'''<tr>
        <td style="width: 62px;">&nbsp;{keyword[0]}</td>
        <td style="width: 43px;">&nbsp;{keyword[1]}</td>
        </tr>'''

    keyword_html_summary_table += '''</tbody>
    </table>'''
    return keyword_html_summary_table

def write_to_html(article_body, title_keyword_summariser_html):
    # html_file = open('webpage.html','r') #Read File
    html_file = open('webpage.html','w') #Write to file File

    html_main = f"""<html>
    <meta http-equiv="refresh" content="5">
    <head></head>
    <body>

    <p><strong><center>Welcome to Viren's News Headline Summary!</center></strong></p>

    {article_body}
    <p><strong><center>Keyword Counter</center></strong></p>
    {title_keyword_summariser_html}
    </p>
    </body>
    </html>"""

    html_file.write(html_main)
    html_file.close()


if __name__ == "__main__":
    news_sites_list = [
        NewsSite('BBC News', 'http://feeds.bbci.co.uk/news/rss.xml'),
        NewsSite('Sky News', 'http://feeds.skynews.com/feeds/rss/home.xml'),
        NewsSite('Metro News', 'https://metro.co.uk/news/feed/')
        ]

    article_body = ''
    for news_site in news_sites_list:
        article_body += articles_html_generator(news_site.name, news_site.URL, 10)


    title_keyword_summariser_html = title_keyword_summariser_html(news_sites_list, excluded_words_list, 10)

    write_to_html(article_body, title_keyword_summariser_html)
