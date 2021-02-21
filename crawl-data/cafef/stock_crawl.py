from bs4 import BeautifulSoup
import requests
from utils import pdate2date, save

URLcafef = "https://cafef.vn"
URL = 'https://cafef.vn/timeline/31/trang-1.chn'

for i in range(2000, 4001):
    print(i, "--------------------------")
    URL = 'https://cafef.vn/timeline/31/trang-' + str(i) +'.chn'
    page = requests.get(URL)

    # crawl chúng khoán
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll("a", {"class":"avatar show-popup visit-popup"})

    for result in results:
        print(result.get('href'))
        link = result.get('href')
        URLpage = URLcafef + link
        article = requests.get(URLpage)
        soup2 = BeautifulSoup(article.content, 'html.parser')
        try:
            date = soup2.findAll("span", {"class":"pdate"})[0]
            date = pdate2date(date.text)

            sumary = soup2.findAll("h2", {"class":"sapo"})[0].text.strip()
            results2 = soup2.find(id="mainContent")
            all_p = results2.findAll('p')
            main_content = sumary
            for p in all_p:
                main_content += p.text
            # print(main_content + "\n----------------------------------------")
            
            #save file
            data_foder = "crawl-data"
            filename = link.replace("/", "") + ".txt"
            save(filename, main_content, date, data_foder)
        except:
            print("error:", link)

