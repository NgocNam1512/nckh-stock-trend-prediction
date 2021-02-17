import requests
import os
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup

def get_links(soup):
    links = []
    titles = soup.findAll('a', {'class':'story__title'})
    for link in titles:
        links.append("https://thanhnien.vn/tai-chinh-kinh-doanh" + link['href'])

    return links

def get_content(soup):
    sapo = soup.find('div', {"id":"chapeau"}).text
    content = soup.find('div', {"id":"abdf"})

    main_content = sapo + "\n"
    for p in content.findAll("p"):
        main_content += p.text + "\n"
    
    return main_content


def get_date(soup):
    datetime = soup.find('time').text
    date = datetime.split("-")[1].strip()
    day, month, year = date.split("/")
    datestring = year + month + day
    
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


if __name__ == "__main__":
    for i in tqdm(range(1, 102)):
        url = f'https://thanhnien.vn/chung-khoan/trang-{i}.html'
        try:
            souplink = get_soup(url)
            links = get_links(souplink)
            for link in links:
                try:
                    soup = get_soup(link)
                    content = get_content(soup)
                    date, year = get_date(soup)
                    save(link.split("/")[-1].replace("html", "txt"), content, year, date, "thanhnien-data")
                except Exception as e:
                    print("error at", link)
                    print(e)
        except Exception as e:
            print("Error at", url)
            print(e)