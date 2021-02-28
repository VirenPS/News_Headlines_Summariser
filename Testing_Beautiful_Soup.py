import collections

import requests
from bs4 import BeautifulSoup


class Article:
    def __init__(self, source, article_xml):
            self.title = article_xml.title.string
            self.description = article_xml.description.string
            if source == 'BBC':
                self.link = article_xml.guid.string
            elif source =='Sky':
                self.link = article_xml.link.string


URL = 'http://feeds.bbci.co.uk/news/rss.xml'
page = requests.get(URL)

bbc_articles_list = []
for article_xml in BeautifulSoup(page.content, 'html.parser').find_all('item'):
    bbc_articles_list.append(Article('BBC', article_xml))

# Extracts top 10
top_10_articles_list = bbc_articles_list[:10]


bbc_html_body = ''
for article in top_10_articles_list:
    bbc_html_body += f'''<p>
    <a href='{article.link}'>{article.title}</a>
    <br>{article.description}
    </p>'''

title_keyword_list = []
for article in top_10_articles_list:
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


def write_to_html():
    # html_file = open('webpage.html','r') #Read File
    html_file = open('webpage.html','w') #Write to file File

    message = f"""<html>
    <meta http-equiv="refresh" content="5">
    <head></head>
    <body>

    <p>Welcome to Viren's News Headline Summary!</p>

    <table style="width: 106px;" border="1" cellpadding="4">
    <tbody>
    {keyword_html_summary_table}
    </tbody>
    </table>



    <p><b><u>BBC Headlines</u></b></p>

    {bbc_html_body}

    </body>
    </html>"""

    html_file.write(message)
    html_file.close()

write_to_html()
