from bs4 import BeautifulSoup
import requests
import os

# url = 'https://vietstock.vn/2017/02/phan-tich-ky-thuat-phien-chieu-2802-dao-dong-hep-1636-520076.htm'

def crawl_one_page(url:str):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    article = soup.findAll("div", {"class":"col-xs-12 col-lg-10 width_medium"})[0]

    main_content = ""
    for p in article.div.findAll('p'):
        main_content += p.text + "\n"

    return main_content


def save(name:str, content:str, datetime:str, path:str):
    path_datetime = os.path.join(path, datetime)
    if not os.path.exists(path_datetime):
        os.makedirs(path_datetime)

    save_path = os.path.join(path_datetime, name)
    with open(save_path, "w", encoding='utf8') as writer:
        writer.write(content)

# print(crawl_one_page(url))
