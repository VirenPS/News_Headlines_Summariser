import collections

import requests
from bs4 import BeautifulSoup


class Article:
    def __init__(self, article_xml):
            self.title = article_xml.title.string
            self.description = article_xml.description.string
            self.link = article_xml.guid.string

def headline_summariser(url, top_n_articles):
    page = requests.get(url)
    articles_list = []
    for article_xml in BeautifulSoup(page.content, 'html.parser').find_all('item'):
        articles_list.append(Article(article_xml))

    # Extracts top 10
    top_n_articles = articles_list[:top_n_articles]

    html_body = ''
    for article in top_n_articles:
        html_body += f'''<p>
        <a href='{article.link}'>{article.title}</a>
        <br>{article.description}
        </p>'''
    return html_body

    # Keyword Summariser
    # title_keyword_list = []
    # for article in top_n_articles:
    #     colon_char = article.title.find(':')
    #     if colon_char != -1:
    #         title_keyword_list.append(article.title[0:colon_char])
    # keyword_counter = collections.Counter(title_keyword_list)

    # # Append html table.
    # keyword_html_summary_table = ''
    # for keyword in keyword_counter:
    #     # print(keyword, ': ', keyword_counter[keyword])
    #     keyword_html_summary_table += f'''<tr>
    #     <td style="width: 62px;">&nbsp;{keyword}</td>
    #     <td style="width: 43px;">&nbsp;{keyword_counter[keyword]}</td>
    #     </tr>'''


def write_to_html():
    # html_file = open('webpage.html','r') #Read File
    html_file = open('webpage.html','w') #Write to file File

    # sky_headlines

    message = f"""<html>
    <meta http-equiv="refresh" content="5">
    <head></head>
    <body>

    <p><strong><center>Welcome to Viren's News Headline Summary!</center></strong></p>

    <p><b><u>BBC News</u></b>
    {headline_summariser('http://feeds.bbci.co.uk/news/rss.xml', 10)}
    </p>

    <p><b><u>Sky News</u></b>
    {headline_summariser('http://feeds.skynews.com/feeds/rss/home.xml', 10)}
    </p>

    </body>
    </html>"""

    html_file.write(message)
    html_file.close()

write_to_html()

# Summary Table HTML
# <table style="width: 106px;" border="1" cellpadding="4">
#     <tbody>
#     {keyword_html_summary_table}
#     </tbody>
#     </table>

# print(headline_summariser('http://feeds.skynews.com/feeds/rss/home.xml','Sky',10))
