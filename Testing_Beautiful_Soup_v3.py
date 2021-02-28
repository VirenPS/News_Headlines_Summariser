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

def keyword_summariser_html(article_list):
    # print(article_list)
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






if __name__ == "__main__":
    news_sites_list = [
        NewsSite('BBC News', 'http://feeds.bbci.co.uk/news/rss.xml'),
        NewsSite('Sky News', 'http://feeds.skynews.com/feeds/rss/home.xml'),
        NewsSite('Metro News', 'https://metro.co.uk/news/feed/')
        ]

    article_body = ''
    for news_site in news_sites_list:
        article_body += articles_html_generator(news_site.name, news_site.URL, 10)

    article_titles = []

    for news_site in news_sites_list:
        article_list_news = article_list(news_site.URL)
        for i in article_list_news:
            article_titles.append(i.title)

    article_title_keywords = []
    for title in article_titles:
        a = title.split()
        article_title_keywords += a

    keyword_counter = collections.Counter(article_title_keywords)
    keyword_counter_ordered = collections.Counter(article_title_keywords).most_common()

    print(keyword_counter_ordered[1])


    for keyword in keyword_counter_ordered:
        # print(keyword, ': ', int(keyword_counter[keyword]))
        print(keyword[0], ': ', keyword[1])


    # print(article_titles[5])
#         article_titles.append(news_site.title)

#     for i in range(0,5):
#         print(article_titles[i].title)

#     keyword_counter = collections.Counter(article_titles.title)

#     for keyword in keyword_counter:
#         print(keyword, ': ', keyword_counter[keyword])


#     write_to_html(article_body)

# Summary Table HTML
# <table style="width: 106px;" border="1" cellpadding="4">
#     <tbody>
#     {keyword_html_summary_table}
#     </tbody>
#     </table>

# print(articles_html_generator('http://feeds.skynews.com/feeds/rss/home.xml','Sky',10))
