import requests
from bs4 import BeautifulSoup
import textwrap

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://allo.ua/ru/products/internet-planshety/p-' + str(page) + '/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class':'product-name'}):
            href = link.get('href')
            title = textwrap.dedent(link.string)
            print(title)
            print(href)
        page += 1

trade_spider(1)