import requests
from bs4 import BeautifulSoup
import os


def get_html(url:str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def get_content(soup):
    title_detail = soup.find('h1', {'class':'title-detail'}).text
    description = soup.find('p', {'class':'description'}).text
    detail = soup.find('article', {'class':'fck_detail'})

    main_content = title_detail + "\n" + description + "\n"
    for p in detail.findAll('p'):
        main_content += p.text + "\n"

    return main_content

def get_date(soup):
    datetime = soup.find('span', {'class':'date'}).text
    date = datetime.split(",")[1].strip()
    day, month, year = date.split("/")
    datestring = year + f"{int(month):02d}" + f"{int(day):02d}"
    
    return datestring, year
    

def save(name:str, content:str, year:str, datetime:str, path:str):
    path_year = os.path.join(path, year)
    if not os.path.exists(path_year):
        os.makedirs(path_year)

    path_datetime = os.path.join(path_year, datetime)
    if not os.path.exists(path_datetime):
        os.makedirs(path_datetime)

    save_path = os.path.join(path_datetime, name)
    with open(save_path, "w", encoding='utf8') as writer:
        writer.write(content)

# url = 'https://vnexpress.net/nikkei-leo-cao-2736252.html'
# soup = get_html(url)
# print(get_date(soup))
