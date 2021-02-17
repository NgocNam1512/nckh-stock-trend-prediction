import requests
from bs4 import BeautifulSoup


def get_links(url:str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.findAll("h2", {"class":"title-news"})
    links = []
    for title in titles:
        links.append(title.a['href'])

    return links

# url = 'https://vnexpress.net/kinh-doanh/chung-khoan-p501'
# print(get_links(url))