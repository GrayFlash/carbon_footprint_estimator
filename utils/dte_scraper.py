import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

def make_soup(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')

dte = "https://www.downtoearth.org.in/category/climate-change/news"

def scrap():
    news_blocks = make_soup(dte).find_all('div', {'class':'block-with-img-description mb-30'})

    news_list = []
    for block in news_blocks:
        img = block.find('img')['data-original']
        href = block.find('a')['href']
        title = block.find('a').find('strong').text
        description = block.find('p').text
        post_date = block.find('span').text
        news_list.append({'title':title,'img': img,'href': href,'descr': description, 'date':post_date})

    # print(news_list)
    return news_list

# scrap()



