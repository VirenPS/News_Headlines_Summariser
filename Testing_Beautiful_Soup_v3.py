import collections

import requests
from bs4 import BeautifulSoup


class Article:
    def __init__(self, article_xml):
        self.title = article_xml.title.string
        self.description = article_xml.description.string
        self.link = article_xml.guid.string


class NewsSite:
    def __init__(self, name, URL):
        self.name = name
        self.URL = URL







def articles_html_generator(name, URL, top_n_articles):
    page = requests.get(URL)

    articles_list = []
    for article_xml in BeautifulSoup(page.content, 'html.parser').find_all('item'):
        articles_list.append(Article(article_xml))

    # Extracts top 10
    top_n_articles = articles_list[:top_n_articles]

    # Create article_body html template
    article_body = f'<p><b><u>{name}</u></b>'
    for article in top_n_articles:
        article_body += f'''<p>
        <a href='{article.link}'>{article.title}</a>
        <br>{article.description}
        </p>'''
    article_body += '</p>'

    return article_body

def keyword_summariser(URL, top_n_articles):


    # Keyword Summariser
    title_keyword_list = []
    for article in top_n_articles:
        colon_char = article.title.find(':')
        if colon_char != -1:
            title_keyword_list.append(article.title[0:colon_char])
    keyword_counter = collections.Counter(title_keyword_list)

    # Append html table.
    keyword_html_summary_table = ''
    for keyword in keyword_counter:
        # print(keyword, ': ', keyword_counter[keyword])
        keyword_html_summary_table += f'''<tr>
        <td style="width: 62px;">&nbsp;{keyword}</td>
        <td style="width: 43px;">&nbsp;{keyword_counter[keyword]}</td>
        </tr>'''

def write_to_html(article_body):
    # html_file = open('webpage.html','r') #Read File
    html_file = open('webpage.html','w') #Write to file File

    message = f"""<html>
    <meta http-equiv="refresh" content="5">
    <head></head>
    <body>

    <p><strong><center>Welcome to Viren's News Headline Summary!</center></strong></p>

    {article_body}

    </body>
    </html>"""

    html_file.write(message)
    html_file.close()

def article_tile_list_generator(URL):


if __name__ == "__main__":
    news_sites_list = [
        NewsSite('BBC News', 'http://feeds.bbci.co.uk/news/rss.xml'),
        NewsSite('Sky News', 'http://feeds.skynews.com/feeds/rss/home.xml'),
        NewsSite('Metro News', 'https://metro.co.uk/news/feed/')
        ]

    article_body = ''
    for news_site in news_sites_list:
        article_body += articles_html_generator(news_site.name, news_site.URL, 10)

    write_to_html(article_body)

# Summary Table HTML
# <table style="width: 106px;" border="1" cellpadding="4">
#     <tbody>
#     {keyword_html_summary_table}
#     </tbody>
#     </table>

# print(articles_html_generator('http://feeds.skynews.com/feeds/rss/home.xml','Sky',10))
