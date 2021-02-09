import requests
from bs4 import BeautifulSoup
from crawl_one import crawl_one_page, save

URL = 'https://vietstock.vn'
posturl = 'https://vietstock.vn/StartPage/ChannelContentPage'

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}
form_data = {
    'channelID':'1636',
    'page':'1'
}

# loop date
for year in range(2016,2022):
    for month in range(1,13):
        for day in range(1, 32):
            date = str(year) + f"{month:02d}" + f"{day:02d}"
            try:
                print(date)
                form_data['date'] = str(year) + "-" + f"{month:02d}" + "-" + f"{day:02d}"

                page = requests.post(posturl, headers=headers, data=form_data)
                soup = BeautifulSoup(page.content, 'html.parser')
                resultSet = soup.findAll("h2", {"class":"channel-title"})
                for h2 in resultSet:
                    link = h2.a['href']
                    main_content = crawl_one_page(URL+link)

                    data_foder = "vietstock-data"
                    filename = link.replace("/", "") + ".txt"
                    save(filename, main_content, date, data_foder)
            except:
                print("error", date)